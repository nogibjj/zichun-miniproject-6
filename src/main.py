import pandas as pd
import os
from databricks import sql

# Databricks connection details
server_hostname = os.getenv("DATABRICKS_SERVER_HOSTNAME")
http_path = os.getenv("DATABRICKS_HTTP_PATH")
access_token = os.getenv("DATABRICKS_ACCESS_TOKEN")

# Function to read the titanic.csv file
def load_titanic_data():
    # Read the CSV file
    df = pd.read_csv('data/titanic.csv')
    return df

# Function to upload Titanic data to Databricks
def upload_to_databricks(df):
    df.dropna(inplace=True)


    # Connect to Databricks
    connection = sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    )
    
    cursor = connection.cursor()
    
    # Create Titanic table in Databricks
    create_table_query = """
    CREATE TABLE IF NOT EXISTS Titanic (
        PassengerId INT,
        Survived INT,
        Pclass INT,
        Name STRING,
        Sex STRING,
        Age DOUBLE,
        SibSp INT,
        Parch INT,
        Ticket STRING,
        Fare DOUBLE,
        Cabin STRING,
        Embarked STRING
    )
    """
    
    cursor.execute(create_table_query)
    
    # Insert data into the Titanic table
    for _, row in df.iterrows():
        insert_query = f"""
        INSERT INTO Titanic (PassengerId, Survived, Pclass, Name, Sex, Age, SibSp, Parch, Ticket, Fare, Cabin, Embarked)
        VALUES ({row['PassengerId']}, {row['Survived']}, {row['Pclass']}, '{row['Name']}', '{row['Sex']}', 
        {row['Age']}, {row['SibSp']}, {row['Parch']}, '{row['Ticket']}', {row['Fare']}, '{row['Cabin']}', 
        '{row['Embarked']}')
        """
        cursor.execute(insert_query)
    
    connection.commit()  # Commit the transaction
    connection.close()

# Function to query Titanic data from Databricks
def run_query():
    # Connect to Databricks
    connection = sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    )
    
    # SQL query to select passengers who survived and order by age
    query = """
    SELECT 
        PassengerId, Name, Survived, Pclass, Sex, Age
    FROM 
        Titanic
    WHERE
        Survived = 1
    ORDER BY 
        Age ASC
    """
    
    # Execute the query
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(result)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    # Load Titanic data from the CSV file
    df = load_titanic_data()
    
    # Upload the data to Databricks
    upload_to_databricks(df)
    
    # Run the query to fetch results
    run_query()
