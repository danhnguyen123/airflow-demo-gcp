from airflow import DAG
from airflow.operators.python import PythonOperator

from plugins.config import config
from plugins.modules import orders 

from plugins.modules import order_detail

from datetime import timedelta, datetime
import pendulum

local_tz = pendulum.timezone(config.TIME_ZONE)

list_table = ["table_orders", "table_order_detail"]

mapping_table = {
    "table_orders": orders,
    "table_order_detail": order_detail
}

default_args = {
    'owner': 'danh.nguyen',
    'depends_on_past': False,
    'trigger_rule' : 'all_done', #https://marclamberti.com/blog/airflow-trigger-rules-all-you-need-to-know/
    'email': ['de@datalize.cloud'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1 if config.ENV == "prod" else 0,
    'retry_delay': timedelta(minutes=1),
    'catchup' : False,
}


with DAG(
    'dag-etl-daily-copy-bar',
    default_args=default_args,
    description='ETL Data from ...',
    schedule_interval='*/5 * * * *',
    start_date=datetime(2024, 1, 1, 0, tzinfo=local_tz),
    catchup=False,
    tags=["5mins", 'elt','hubspot', 'dahahi', 'bigquery', 'lark'],
) as dag:
    
    for table in list_table:

        extract_task = PythonOperator(
            task_id=f"extract_task_{table}",
            python_callable=getattr(mapping_table.get(table), "extract"),
            provide_context=True,
            op_kwargs={
                "date": "2024-08-25"
                }
            )
        
        tranform_task = PythonOperator(
            task_id=f"tranform_task_{table}",
            python_callable=getattr(mapping_table.get(table), "transform"),
            provide_context=True,
            trigger_rule="all_success"
            )

        load_task = PythonOperator(
            task_id=f"load_task_{table}",
            python_callable=getattr(mapping_table.get(table), "load"),
            provide_context=True,
            trigger_rule="all_success"
            )
    
        extract_task >> tranform_task >> load_task