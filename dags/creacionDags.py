from airflow import DAG
from airflow.decorators import dag
from airflow.operators.empty import EmptyOperator

from datetime import datetime

# Definición del primer DAG utilizando 'with'
with DAG(
    dag_id="dag1",
    description="dag1",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@once",
) as dag1:
    # Definición de una tarea vacía para el primer DAG
    op = EmptyOperator(task_id="dummy")


# Definición del segundo DAG como una variable
dag2 = DAG(
    dag_id="dag2",
    description="2dag2",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@once",
)
# Definición de una tarea vacía asociada al segundo DAG
op2 = EmptyOperator(task_id="dummy2", dag=dag2)


# Definición del tercer DAG utilizando un decorador
@dag(
    dag_id="dag3",
    description="dag3",
    start_date=datetime(2022, 10, 31),
    schedule_interval="@once",
)
def generate_dag():
    # Definición de una tarea vacía dentro de la función decorada
    op3 = EmptyOperator(task_id="dummy3")

# Llamada a la función que devuelve el tercer DAG
dag3 = generate_dag()
