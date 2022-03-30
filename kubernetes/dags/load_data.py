from airflow import DAG
from datetime import datetime, timedelta
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator

import psycopg2



default_args = {
    'owner': 'Aditya Gupta',
    'start_date': datetime(2022, 3, 30),
    'retries': 1,
    'retry_delay': timedelta(seconds=5)
}

def query_result():
    try:
        print("connection to airflow database established ")
        conn=psycopg2.connect(host="postgres-service",database="airflow",user="airflow",password="airflow",port="5432")
        cursor=conn.cursor()
        drop_table='drop table if exists assignment_data;'
        cursor.execute(drop_table)
        conn.commit()
        create_table="create table assignment_data as select dag_id,execution_date from dag_run order by execution_date;"
        cursor.execute(create_table)
        conn.commit()
        cursor.execute('select * from assignment_data;')
        print(cursor.fetchall())
    except Exception as e:
        print(e)
    finally:
        conn.close()


dag = DAG("Aditya_kubernetes_dag",
          default_args=default_args,
          schedule_interval='0 6 * * *',
          catchup=False
          )

t1 = DummyOperator(task_id="hello_world",dag=dag)

t2 = PythonOperator(task_id='create_table', python_callable=query_result,dag=dag)

t1 >> t2
