# Running the ETL pipeline in Airflow

## Prerequisites

Execute the below installations:

```bash
apt install python3
apt install python3-pip
pip install apache-airflow
pip install apify_client
```

## Steps

Run the below command to check if airflow is installed

```bash
airflow
```
Execute the below command to start airflow

```bash
airflow standalone
```

## Prepare the DAG

### Common Default Arguments

#### owner:

Description: The owner of the DAG. This is typically used for notifications and permissions.\
Type: String\
Example: 'owner': 'airflow'

#### depends_on_past:

Description: If set to True, a task instance will not run unless the previous instance of the task has succeeded. This can be useful for tasks that depend on the successful completion of previous runs.\
Type: Boolean\
Default: False\
Example: 'depends_on_past': False


#### start_date:

Description: The start date for the DAG. Tasks will not run before this date.\
Type: datetime.datetime\
Example: 'start_date': datetime(2023, 1, 1)\


#### email:

Description: A list of email addresses to send alerts to if the task fails.\
Type: List of strings\
Example: 'email': ['your_email@example.com']\

#### email_on_failure:

Description: Whether to send an email when a task fails.\
Type: Boolean\
Default: True\
Example: 'email_on_failure': True\


#### email_on_retry:

Description: Whether to send an email when a task is retried.\
Type: Boolean\
Default: True\
Example: 'email_on_retry': True\


#### retries:

Description: The number of times to retry the task in case of failure.\
Type: Integer\
Default: 0\
Example: 'retries': 3\

#### retry_delay:

Description: The delay between retries.\
Type: datetime.timedelta\
Default: timedelta(minutes=5)\
Example: 'retry_delay': timedelta(minutes=10)\

#### retry_exponential_backoff:

Description: If set to True, retries will use an exponential backoff algorithm to determine the delay between retries.\
Type: Boolean\
Default: False\
Example: 'retry_exponential_backoff': True\

#### max_retry_delay:

Description: The maximum delay between retries when using exponential backoff.\
Type: datetime.timedelta\
Example: 'max_retry_delay': timedelta(hours=1)\

#### end_date:

Description: The end date for the DAG. Tasks will not run after this date.\
Type: datetime.datetime\
Example: 'end_date': datetime(2023, 12, 31)\

#### execution_timeout:

Description: The maximum time a task is allowed to run before it is marked as failed.\
Type: datetime.timedelta\
Example: 'execution_timeout': timedelta(hours=2)\

#### dagrun_timeout:

Description: The maximum time a DAG run is allowed to run before it is marked as failed.\
Type: datetime.timedelta\
Example: 'dagrun_timeout': timedelta(days=1)\

#### on_failure_callback:

Description: A callback function to be executed when a task fails.\
Type: Callable\
Example: 'on_failure_callback': my_failure_callback_function\

#### on_success_callback:

Description: A callback function to be executed when a task succeeds.\
Type: Callable\
Example: 'on_success_callback': my_success_callback_function\

## Back to running airflow pipeline

Get the airflow dags location from the below file 
```bash
vim /mnt/wslg/distro/root/airflow/airflow.cfg
```

Copy the dag python files and extract.py to the airflow dag location. In WSL ubuntu it will be ```/root/airflow/```.

You will be able to see your dag and run it from the airflow UI.

##### Note: In this standalone version of airflow, a lot of example pipelines are given. Checkout the UI. Explore the code as per your use case and reuse. Local location: ```/usr/local/lib/python3.10/dist-packages/airflow/example_dags/```




