from airflow import DAG
from datetime import datetime
from airflow.operators.python import PythonOperator
from airflow.operators.bash import BashOperator

# Definición de la función a ser ejecutada por el PythonOperator
def print_hello():
    print("Hola desde el PythonOperator")

# Definición del DAG
with DAG(
    dag_id='Dependencias_tareas',  # Identificador del DAG
    description='Creación de dependencias entre varias tareas',  # Descripción del DAG
    schedule_interval='@once',  # Frecuencia de ejecución del DAG (@once significa que se ejecutará solo una vez)
    start_date=datetime(2022, 10, 2)  # Fecha de inicio del DAG
) as dag:

    # Definición de la tarea PythonOperator
    t1 = PythonOperator(
        task_id='task_1',  # Identificador de la tarea
        python_callable=print_hello  # Función de Python que se ejecutará
    )
    
    # Definición de la tarea BashOperator (t2)
    t2 = BashOperator(
        task_id='task2',  # Identificador de la tarea
        bash_command="echo 'tarea 1'"  # Comando Bash que se ejecutará
    )
    
    # Definición de la tarea BashOperator (t3)
    t3 = BashOperator(
        task_id='task_3',  # Identificador de la tarea
        bash_command="echo 'tarea 1'"  # Comando Bash que se ejecutará
    )
    
    # Definición de la tarea BashOperator (t4)
    t4 = BashOperator(
        task_id='task_4',  # Identificador de la tarea
        bash_command="echo 'tarea 1'"  # Comando Bash que se ejecutará
    )
    
    # Definición de las dependencias entre las tareas
    # t1 debe ejecutarse antes de t2, y t2 debe ejecutarse antes de t3 y t4
    t1 >> t2 >> [t3, t4]  # Esto es equivalente a t1.set_downstream(t2) y t2.set_downstream([t3, t4])

    # Esta es otra forma de medir dependencias
    # t1.set_downstream(t2)
    # t2.set_downstream([t3, t4])
