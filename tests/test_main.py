import pytest
from databricks import sql

# Databricks connection details (update with your actual credentials)
server_hostname = "<databricks-server-host>"
http_path = "<databricks-http-path>"
access_token = "<databricks-access-token>"

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
    query = """
    SELECT 
        c.customer_id,
        c.customer_name,
        c.country,
        SUM(o.total_amount) AS total_spent
    FROM 
        Customers c
    JOIN 
        Orders o 
    ON 
        c.customer_id = o.customer_id
    GROUP BY 
        c.customer_id, c.customer_name, c.country
    HAVING 
        SUM(o.total_amount) > 1000
    ORDER BY 
        total_spent DESC;
    """
    
    cursor = db_connection.cursor()
    cursor.execute(query)
    result = cursor.fetchall()
    
    # Example assertions
    assert len(result) == 1  # Expecting one customer to meet the threshold
    assert result[0][1] == 'Alice'  # Alice should be the customer
