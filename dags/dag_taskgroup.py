
from airflow import DAG
from airflow.operators.bash_operator import BashOperator
from datetime import datetime
from airflow.utils.task_group import TaskGroup

dag =  DAG('dag_task_group', description="TaskGroup",
        schedule_interval=None,start_date=datetime(2023,7,24),
        catchup=False)

task1 = BashOperator(task_id="task1",bash_command="sleep 5",dag=dag )
task2 = BashOperator(task_id="task2",bash_command="sleep 5",dag=dag )
task3 = BashOperator(task_id="task3",bash_command="sleep 5",dag=dag )
task4 = BashOperator(task_id="task4",bash_command="sleep 5",dag=dag )
task5 = BashOperator(task_id="task5",bash_command="sleep 5",dag=dag )
task6 = BashOperator(task_id="task6",bash_command="sleep 5",dag=dag )

task_group = TaskGroup("tsk_group", dag=dag)

task7 = BashOperator(task_id="task7",bash_command="sleep 5",dag=dag,task_group=task_group)
task8 = BashOperator(task_id="task8",bash_command="sleep 5",dag=dag,task_group=task_group)
task9 = BashOperator(task_id="task9",bash_command="sleep 5",dag=dag, trigger_rule='one_failed',task_group=task_group )

task1 >> task2
task3 >> task4
[task2,task4] >> task5 >> task6
task6 >> task_group