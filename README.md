
# Week 6 Mini Project

## Project Overview

This project demonstrates the use of Databricks as an external database for running complex SQL queries. 
The SQL query involves:
- **Joins**: To combine data from the `Customers` and `Orders` tables.
- **Aggregation**: To calculate the total amount spent by each customer.
- **Filtering**: To include only customers who spent more than $1000.
- **Sorting**: To display customers in descending order of total amount spent.

## Files
- `databricks/query.sql`: Contains the SQL query.
- `src/main.py`: Python script to connect to Databricks and run the SQL query.
- `tests/test_main.py`: Contains the tests for validating the query.
- `ci.yml`: GitHub Actions workflow to automate testing.


## Setting up Databricks

1. Create a new cluster from the **Clusters** tab.
2. Create a new Notebook under the **Workspace** tab.
3. Use the following code to create the `Customers` and `Orders` tables in Databricks:
    ```python
    spark.sql("""
    CREATE OR REPLACE TEMP VIEW Customers AS
    SELECT * FROM VALUES 
    (1, 'Alice', 'USA'),
    (2, 'Bob', 'Canada')
    AS Customers(customer_id, customer_name, country)
    """)

    spark.sql("""
    CREATE OR REPLACE TEMP VIEW Orders AS
    SELECT * FROM VALUES 
    (1, 1, 1200),
    (2, 2, 800)
    AS Orders(order_id, customer_id, total_amount)
    """)
    ```

### 2. Running the SQL Query in Databricks

Once the tables are created, you can run the SQL query using the following Databricks code:
```python
result = spark.sql("""
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
    total_spent DESC
""")
result.show()
```

### 3. Python Setup for Databricks SQL API

Run the SQL query using Python's Databricks SQL API.

1. Install the Databricks SQL connector:
    ```bash
    pip install databricks-sql-connector
    ```

2. Run the Python script to execute the SQL query on Databricks:
    ```bash
    python src/main.py
    ```

## CI/CD Pipeline

The CI/CD pipeline is set up to automatically run the tests when a new commit is pushed to the `main` branch. The pipeline performs the following steps:
- Sets up the Python environment.
- Installs dependencies.
- Executes the tests in `test_main.py`, which connect to Databricks and run the SQL query.

## Expected Output

Running the query should return:
- Customers who have spent more than $1000.
- The results should be sorted in descending order of the total amount spent.

## How to Run

1. Clone the repository:
   ```bash
   git clone https://github.com/nogibjj/zichun-miniproject-6.git
   cd zichun-miniproject-6
   ```

2. Set up a Python environment and install dependencies:
   ```bash
   python3 -m venv env
   source env/bin/activate
   pip install -r requirements.txt
   ```

3. Run the tests:
   ```bash
   pytest tests/test_main.py
   ```

