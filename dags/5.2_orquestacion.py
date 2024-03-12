from airflow import DAG
from airflow.operators.empty import EmptyOperator
from datetime import datetime

with DAG(
    dag_id="5.2_orquestacion",
    description="Probando orquestacion",
    schedule_interval="* 9 * * 1-5",
    start_date=datetime(2024, 3, 10),
    end_date=datetime(2024, 3, 15),
) as dag:
    t1 = EmptyOperator(task_id="t1")
    t2 = EmptyOperator(task_id="t2")
    t3 = EmptyOperator(task_id="t3")
    t4 = EmptyOperator(task_id="t4")
    t1 >> t2 >> t3 >> t4
