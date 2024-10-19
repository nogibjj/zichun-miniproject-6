from databricks import sql

# Databricks connection details (update with your actual credentials)
server_hostname = "<databricks-server-host>"
http_path = "<databricks-http-path>"
access_token = "<databricks-access-token>"

def run_query():
    # Connect to Databricks
    connection = sql.connect(
        server_hostname=server_hostname,
        http_path=http_path,
        access_token=access_token
    )
    
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
    
    # Run the query
    cursor = connection.cursor()
    cursor.execute(query)
    results = cursor.fetchall()

    # Print the results
    for result in results:
        print(result)

    # Close the connection
    connection.close()

if __name__ == "__main__":
    run_query()
