from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="5.3_orquestacion",
    description="Probando orquestacion",
    schedule_interval="@monthly",
    start_date=datetime(2023, 1, 1),
    end_date=datetime(2023, 12, 31),
) as dag:
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t1 >> t2 >> t3 >> t4
