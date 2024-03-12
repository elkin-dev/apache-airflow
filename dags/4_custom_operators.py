from airflow import DAG
from datetime import datetime
from hellooperator import HelloOperator

with DAG(
    dag_id="customoperator",
    description="DAG personalizado",
    start_date=datetime(2024, 11, 3),
) as dag:
    t1 = HelloOperator(task_id="hello", name="Elkin")
