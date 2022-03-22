from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.postgres_operator import PostgresOperator
from airflow.operators.bash_operator import BashOperator



default_args = {
    'owner': 'Aditya Gupta',
    'start_date': datetime(2022, 3, 21),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

dag = DAG('Docker_assignment',
          default_args=default_args,
          schedule_interval=timedelta(1)
          )

t1 = BashOperator(task_id="Hello_world", bash_command="echo HI ALL, HOW ARE YOU ?",dag=dag)

t2 = PostgresOperator(task_id='create_postgres_table', postgres_conn_id='postgres_conn', sql="sql/create_table.sql", dag=dag)

t1 >> t2
