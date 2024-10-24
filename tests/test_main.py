import pytest
import os
from databricks import sql

# Databricks connection details
server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
access_token = os.getenv("DATABRICKS_ACCESS_TOKEN")

@pytest.fixture(scope="module")
def db_connection():
    # Connect to Databricks
    connection = sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    )
    yield connection
    connection.close()

def test_query(db_connection):
    # Query for passengers who survived
    query = """
    SELECT 
        PassengerId, Name, Survived, Pclass, Sex, Age
    FROM 
        Titanic
    WHERE
        Survived = 1
    ORDER BY 
        Age ASC;
    """
    
    cursor = db_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Example assertions
    assert len(result) > 0  # Expecting at least one survivor
    assert result[0][2] == 1  # The 'Survived' column should be 1 (true)
    assert result[0][4] in ['male', 'female']  # Gender should be 'male' or 'female'
