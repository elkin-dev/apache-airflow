from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="5.1_orequestacion",
    description="Probando orquestacion",
    schedule_interval="@daily",
    start_date=datetime(2024, 3, 12),
    end_date=datetime(2024, 3, 13),
    default_args={"depends_on_past": True},
    max_active_runs=1
) as dag:
    t1 = BashOperator(task_id="tarea1", bash_command='sleep 2 && echo "Tarea 1"')
    t2 = BashOperator(task_id="tarea2", bash_command='sleep 2 && echo "Tarea 1"')
    t3 = BashOperator(task_id="tarea3", bash_command='sleep 2 && echo "Tarea 1"')
    t4 = BashOperator(task_id="tarea4", bash_command='sleep 2 && echo "Tarea 1"')

t1 >> t2 >> [t3, t4]
