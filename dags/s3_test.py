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



def s3_extract():
#    source_s3_key = "user"
   source_s3_bucket = "datalake"
   hook = S3Hook(aws_conn_id=AWS_S3_CONN_ID)
   

   keys = hook.list_keys(source_s3_bucket, prefix='test')
   print(keys)
   




cid = "dev_s3"                       # the airflow connection id
b_url = 's3://datalake'   # remote_base_log_folder

hook = S3Hook(cid, transfer_config_args={
    'use_threads': False,
})

parsed_loc = hook.parse_s3_url(b_url)[0]
# 'airflow-logs-dev'
b, k = hook.parse_s3_url(b_url)
# b == 'airflow-logs-dev', k == 'logs'
#hook.get_s3_bucket_key('airflow-logs-dev', 'logs', b, k)
# ('airflow-logs-dev', 'logs')

hook.check_for_bucket(parsed_loc)  # parsed_loc == 'airflow-logs-dev'
# [2022-10-20T16:28:15.808+0000] {base.py:71} INFO - Using connection ID 'amazon_s3' for task execution.
# [2022-10-20T16:28:15.868+0000] {connection_wrapper.py:306} INFO -
#       AWS Connection (conn_id='amazon_s3', conn_type='aws') credentials retrieved from extra.
# True
hook.check_for_bucket(b)
# True
hook.check_for_bucket(k)
# [2022-10-20T16:31:37.605+0000] {s3.py:223} ERROR - Bucket "logs" does not exist
# False
# Expected - k is a key, not a bucket

print(hook.list_keys(b))
# ['hello.txt'] -- only if you uploaded the file like in the comment above and that's all that's in there
   	 
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