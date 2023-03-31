

from __future__ import annotations
import csv
import datetime

import pendulum

from airflow import DAG

from airflow.operators.python import PythonOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook
from airflow.providers.postgres.hooks.postgres import PostgresHook
import pendulum

# Example of using Postgres and S3
#https://betterdatascience.com/apache-airflow-postgres-database/


with DAG(
    dag_id="postgres_to_s3",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["simple"],
    params={},
) as dag:

    temp_path = "temp_path.csv"
    # Define Postgres query
    query = 'SELECT dag_id FROM dag;'
    

    def get_data():
        sql_stmt = "SELECT dag_id FROM dag;"
        
        pg_hook = PostgresHook(
            postgres_conn_id='dev_db',
            schema='airflow'
        )
        pg_conn = pg_hook.get_conn()
        cursor = pg_conn.cursor()
        cursor.execute(sql_stmt)
        result = cursor.fetchall()

        # Write to CSV file
        
        print(f'Writing to {temp_path}...')
        with open(temp_path, 'w') as fp:
            a = csv.writer(fp, quoting = csv.QUOTE_MINIMAL, delimiter = ',')
            a.writerow([i[0] for i in cursor.description])
            a.writerows(result)

    # Get data from a table in Postgres
    task_get_data = PythonOperator(
        task_id='get_data',
        python_callable=get_data,
        do_xcom_push=True
    )

    # Define Python operator to write to S3
    def write_to_s3():
        s3_hook = S3Hook(aws_conn_id='dev_s3')
        result = s3_hook.load_file(
            filename=temp_path,
            key='my_dag_file.csv',
            bucket_name='datalake',
            replace=True
        )
        print(f'File written to S3: {result}')

    s3_operator = PythonOperator(
        task_id='write_to_s3',
        python_callable=write_to_s3,
        dag=dag
    )

    # Set task dependencies
    task_get_data >> s3_operator

if __name__ == "__main__":
    dag.test()