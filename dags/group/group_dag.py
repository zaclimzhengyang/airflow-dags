# group_dag.py
from groups.group_donwloads import download_tasks
from datetime import datetime

from dags.group_dag import dag

with DAG('group_dag', start_date=datetime(2022, 1, 1), schedule_interval'@daily', catchup=False) as dag:
    args = {'start_date': dag.start_date, 'schedule_interval': dag.schedule_interval, 'catchup': dag.catchup}

    downloads = download_tasks()

    check_files = BashOperator(
        task_id='check_files',
        bash_command='sleep 10'
    )

    downloads >> check_files