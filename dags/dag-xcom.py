from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

dag =  DAG('example_xcom', description="xcom",
        schedule_interval=None,start_date=datetime(2023,7,5),
        catchup=False)

def task_write(**kwarg):
    kwarg['ti'].xcom_push(key='valuexcom1',value=10200)

task1 = PythonOperator(task_id="task1",python_callable=task_write,dag=dag )

def task_read(**kwarg):
    valor = kwarg['ti'].xcom_pull(key='valuexcom1')
    print(f"Value : {valor}")

task2 = PythonOperator(task_id="task2",python_callable=task_read,dag=dag )

task1 >> task2