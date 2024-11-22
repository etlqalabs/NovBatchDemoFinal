import pandas as pd
from sqlalchemy import create_engine
mysql_engine = create_engine('mysql+pymysql://root:Admin%40143@localhost:3308/demo')

#extraction of data from source systems to staging tables
df_emp = pd.read_csv('data/employees.csv')
df_emp.to_sql("staging_employees",mysql_engine,if_exists='replace',index=False)
df_sal = pd.read_json('data/salary.json')
df_sal.to_sql("staging_salary",mysql_engine,if_exists='replace',index=False)
print("extraction completed and loaded in staging tables")

#Transfromation rules

query = """select e.eno, upper(e.ename) as upper_name,e.hiredate,s.salary,s.commission,s.salary+s.commission 
as total_salary
 from staging_employees e join staging_salary s on e.eno = s.eno
"""
df = pd.read_sql(query,mysql_engine)
print("Transfromation completed ")

# Load in to target table in mYSQL database
df.to_sql("employees_detail",mysql_engine,if_exists='replace',index=False)
print("Loading completed ")