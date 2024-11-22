import pandas as pd
import pytest
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

@pytest.mark.skip
def test_data_transform_ename_to_upperCase():
    query_expected = """select upper(ename) as upper_name from staging_employees"""
    df_expected = pd.read_sql(query_expected, mysql_engine).astype('str')
    query_actual = """select upper_name from employees_detail"""
    df_actual = pd.read_sql(query_actual,mysql_engine).astype('str')
    assert df_actual.equals(df_expected), "ename is not converted to upper case - please investigate"

def test_data_transform_total_salary_derivation():
    query_expected = """select salary+ifnull(commission,0) as total_salary from staging_salary"""
    df_expected = pd.read_sql(query_expected, mysql_engine)
    query_actual = """select total_salary from employees_detail"""
    df_actual = pd.read_sql(query_actual,mysql_engine)
    assert df_actual.equals(df_expected), "Total_salary is not derived correctly - please investigate"
