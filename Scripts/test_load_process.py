import pandas as pd
import pytest
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

def test_data_transform_load_joiner():
    query_expected = """select e.eno, upper(e.ename) as upper_name,e.hiredate,s.salary,s.commission,s.salary+ifnull(s.commission,0) 
    as total_salary
     from staging_employees e join staging_salary s on e.eno = s.eno
    """
    df_expected = pd.read_sql(query_expected, mysql_engine)
    query_actual = """select * from employees_detail"""
    df_actual = pd.read_sql(query_actual,mysql_engine)
    assert df_actual.equals(df_expected), "ename is not converted to upper case - please investigate"
