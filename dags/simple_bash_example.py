

from __future__ import annotations

import datetime

import pendulum

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.empty import EmptyOperator

with DAG(
    dag_id="simple_bash_example",
    schedule="0 0 * * *",
    start_date=pendulum.datetime(2021, 1, 1, tz="UTC"),
    catchup=False,
    dagrun_timeout=datetime.timedelta(minutes=60),
    tags=["simple"],
    params={},
) as dag:

    
    run_this = BashOperator(
        task_id="run_this_1",
        bash_command="echo 1",
    )
    

    run_this


if __name__ == "__main__":
    dag.test()