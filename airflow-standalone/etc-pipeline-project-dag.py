from datetime import timedelta
from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.dates import days_ago
from datetime import datetime

from extract import extract

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'start_date': datetime(2023, 1, 1),
    'email': ['ashwinisoni10152@gmail.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=1)
}

dag = DAG(
    'etlpipelineproject_dag',
    default_args = default_args,
    description = "This is an etl pipeline project dag."
)

run_etl = PythonOperator(
    task_id = 'api_data_extract_etl',
    python_callable = extract,
    dag = dag
)

run_etl

