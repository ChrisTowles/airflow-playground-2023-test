import logging
from airflow import DAG
from datetime import datetime, timedelta
from airflow.providers.postgres.hooks.postgres import PostgresHook
from airflow.operators.python import PythonOperator

from tempfile import NamedTemporaryFile
from typing import TYPE_CHECKING, Dict, List, Optional, Sequence, Union

from airflow.exceptions import AirflowException
from airflow.models import BaseOperator
from airflow.providers.amazon.aws.hooks.s3 import S3Hook

# Change these to your identifiers, if needed.
AWS_S3_CONN_ID = "dev_s3"

# Troubleshooting mino issues with S3
# https://github.com/apache/airflow/discussions/26979#discussioncomment-3928659

def s3_extract():
   source_s3_bucket = "datalake"
   hook = S3Hook(aws_conn_id=AWS_S3_CONN_ID)
   
   b_url = 's3://datalake'
   parsed_loc = hook.parse_s3_url(b_url)[0]
   result = hook.check_for_bucket(parsed_loc)
   print(f'$"s3 bucket "{source_s3_bucket}" exists: {result}')
   

with DAG(
	dag_id="s3_extract",
	start_date=datetime(2022, 2, 12),
	schedule_interval=timedelta(days=1),
	catchup=False,
) as dag:

  t1 = PythonOperator(
    	task_id="s3_extract_task",
    	python_callable=s3_extract)
  t1