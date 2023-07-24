from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime

dag =  DAG('pool', description="Poll usage example",
        schedule_interval=None,start_date=datetime(2023,3,5),
        catchup=False)

task1 = BashOperator(task_id="task1",bash_command="sleep 5",dag=dag, pool="mypool"  )
task2 = BashOperator(task_id="task2",bash_command="sleep 5",dag=dag, pool="mypool",priority_weight=5 )
task3 = BashOperator(task_id="task3",bash_command="sleep 5",dag=dag , pool="mypool")
task4 = BashOperator(task_id="task4",bash_command="sleep 5",dag=dag , pool="mypool", priority_weight=10 )