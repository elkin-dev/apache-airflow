from airflow import DAG
from datetime import datetime
from airflow.operators.bash import BashOperator

# Definición del DAG llamado 'BashOperator'
with DAG(
    dag_id='BashOperator',  # Identificador del DAG
    description='Dag con un BashOperator',  # Descripción del DAG
    start_date=datetime(2022, 7, 10)  # Fecha de inicio del DAG
) as dag:

    # Definición de la tarea Bash
    t1 = BashOperator(
        task_id='Hello_with_bash',  # Identificador de la tarea
        bash_command="echo 'Hola este es mi primer BashOperator'"  # Comando Bash a ejecutar
    )
