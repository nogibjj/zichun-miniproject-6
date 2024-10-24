
# Week 6 Mini Project

## Project Overview

This project demonstrates the design and execution of a complex SQL query based on the Titanic dataset. The project involves:
- **Joins**: Though not applicable for a single table like Titanic, complex queries can include join concepts for multi-table designs.
- **Aggregation**: Summarizing data using aggregate functions like `COUNT()`.
- **Sorting**: Ordering the result set by specific fields.

The SQL query is designed to process data in a Databricks environment using Python and the Databricks SQL API. The project also includes a CI/CD pipeline to automate the testing of the SQL query and its results.

## SQL Query Explanation

The query in this project analyzes the Titanic dataset to calculate the survival rate of passengers by their gender and class. The results are sorted by the survival rate in descending order.

### Query:

```sql
SELECT 
    Pclass,
    Sex,
    COUNT(CASE WHEN Survived = 1 THEN 1 END) AS SurvivedCount,
    COUNT(*) AS TotalPassengers,
    (COUNT(CASE WHEN Survived = 1 THEN 1 END) / COUNT(*)) * 100 AS SurvivalRate
FROM 
    Titanic
GROUP BY 
    Pclass, Sex
ORDER BY 
    SurvivalRate DESC;
```

### Explanation:

1. **Aggregation**:
   - `COUNT(CASE WHEN Survived = 1 THEN 1 END)` counts the number of passengers who survived (`Survived = 1`).
   - `COUNT(*)` counts the total number of passengers in each group (by `Pclass` and `Sex`).
   
2. **Calculation**:
   - The survival rate is calculated as `(COUNT(CASE WHEN Survived = 1 THEN 1 END) / COUNT(*)) * 100`, representing the percentage of passengers who survived in each group.
   
3. **Grouping**:
   - The `GROUP BY` clause groups the data by passenger class (`Pclass`) and gender (`Sex`).

4. **Sorting**:
   - The results are ordered by the calculated survival rate in descending order, so the groups with the highest survival rate appear first.

### Expected Results:
- This query returns the survival rate of passengers grouped by class and gender, along with the number of survivors and total passengers in each group.

### Sample Output:

| Pclass | Sex    | SurvivedCount | TotalPassengers | SurvivalRate |
|--------|--------|---------------|-----------------|--------------|
| 1      | female | 80            | 85              | 94.12%       |
| 3      | female | 90            | 165             | 54.55%       |
| 1      | male   | 40            | 180             | 22.22%       |

## CI/CD Pipeline

The project uses **GitHub Actions** to automate testing and validation. The pipeline is defined in the `.github/workflows/ci.yml` file, and it performs the following steps:

1. **Install dependencies**:
   - Sets up the Python environment and installs required packages (such as `databricks-sql-connector` and `pytest`).

2. **Run SQL query tests**:
   - Executes the `main.py` script to upload data to the Databricks database and test the SQL query.

3. **Run automated tests**:
   - Uses `pytest` to validate the SQL query results using a predefined test file (`test_main.py`).

### CI/CD Example Workflow:

```yaml
name: Databricks SQL Query CI

on:
  push:
    branches:
      - main

jobs:
  test_sql:
    runs-on: ubuntu-latest
    steps:
    - name: Checkout repository
      uses: actions/checkout@v2

    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.x'

    - name: Install dependencies
      run: |
        pip install -r requirements.txt

    - name: Run main.py to load CSV and create tables
      env:
        DATABRICKS_SERVER_HOSTNAME: ${{ secrets.DATABRICKS_SERVER_HOSTNAME }}
        DATABRICKS_HTTP_PATH: ${{ secrets.DATABRICKS_HTTP_PATH }}
        DATABRICKS_ACCESS_TOKEN: ${{ secrets.DATABRICKS_ACCESS_TOKEN }}
      run: |
        python src/main.py

    - name: Run SQL query tests
      env:
        DATABRICKS_SERVER_HOSTNAME: ${{ secrets.DATABRICKS_SERVER_HOSTNAME }}
        DATABRICKS_HTTP_PATH: ${{ secrets.DATABRICKS_HTTP_PATH }}
        DATABRICKS_ACCESS_TOKEN: ${{ secrets.DATABRICKS_ACCESS_TOKEN }}
      run: |
        pytest tests/test_main.py
```

## How to Run the Project Locally

1. **Clone the repository**:
   ```bash
   git clone https://github.com/nogibjj/zichun-miniproject-6.git
   ```

2. **Set up Python environment**:
   Make sure you have Python 3.x installed. You can create a virtual environment:

   ```bash
   python -m venv env
   source env/bin/activate  # On Windows use `env\Scriptsctivate`
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the `main.py` script** to upload the Titanic dataset and run the SQL query:
   ```bash
   python src/main.py
   ```

5. **Run tests**:
   You can run the tests using `pytest`:
   ```bash
   pytest tests/test_main.py
   ```

## Deliverables

1. **SQL Query**: The query is located in `src/main.py` and executed in Databricks.
2. **Explanation**: The query explanation and expected results are provided above.
3. **CI/CD Pipeline**: The pipeline is defined in `.github/workflows/ci.yml`.
