from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator

# Definición de la función a ser ejecutada por el PythonOperator
def print_hello():
    print("Hola desde el PythonOperator")

# Definición del DAG
with DAG(
    dag_id='PythonOperator',  # Identificador del DAG
    description='Hello_with_PythonOperator',  # Descripción del DAG
    schedule_interval='@once',  # Frecuencia de ejecución del DAG (@once significa que se ejecutará solo una vez)
    start_date=datetime(2024, 1, 13)  # Fecha de inicio del DAG
) as dag:

    # Definición de la tarea PythonOperator
    t1 = PythonOperator(
        task_id='Task1',  # Identificador de la tarea
        python_callable=print_hello  # Función de Python que se ejecutará
    )
