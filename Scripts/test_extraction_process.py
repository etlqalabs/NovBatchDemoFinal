import pandas as pd
import pytest
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

# Test Extraction of employees.csv data
def test_dataExtractionFromEmployeesFile():
    df_expected = pd.read_csv('data/employees.csv')
    query = """select * from staging_employees"""
    df_actual = pd.read_sql(query,mysql_engine)
    assert df_actual.equals(df_expected),"Data Extrcation from employees.csv file is FAILED"

# Test Extraction of salary.json data
def test_dataExtractionFromSalaryFile():
    df_expected = pd.read_json('data/salary.json')
    query = """select * from staging_salary"""
    df_actual = pd.read_sql(query,mysql_engine)
    assert df_actual.equals(df_expected),"Data Extrcation from salary.json file is FAILED"
