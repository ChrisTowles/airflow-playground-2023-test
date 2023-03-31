# Airflow Playground


This is a playground for Apache Airflow. The goal is to get more deep understanding of Airflow and its capabilities. I've played with Airflow in the past, but goal here is to get more hands-on experience with it.


## Tasks

- [x] Airflow docker starting
- [x] Postgres Database started
- [x] Create a DAG that runs a Python function
- [x] Create a DAG that reads table in Postgres
- [x] Mock S3 with Minio or localstack
- [x] create connection to S3
- [x] create connection to postgres
- [x] Create a DAG that reads table in Postgres and outputs to S3

## Pre-requisites

### Docker

- [Docker on Ubuntu](https://docs.docker.com/engine/install/ubuntu/)
  - https://docs.docker.com/engine/install/linux-postinstall/#manage-docker-as-a-non-root-user


### Python

```bash
pyenv install 3.10.6

pyenv virtualenv 3.10.6 airflow-playground

pyenv local airflow-playground

pyenv activate airflow-playground

```

```bash
pip install -r requirements/requirements-local.txt
```


Configure VS code with `Python: Select Interpreter` and chose `airflow-playground`. 


## Setup

```bash
docker compose up
```

Open <http://localhost:8080> in browser


```
Username: airflow
password: airflow
```

## References

- https://airflow.apache.org/docs/apache-airflow/2.5.2/docker-compose.yaml
- https://github.com/mrn-aglic/examples/tree/main/airflow-new-features
- https://github.com/apache/airflow/tree/main/airflow/example_dags
- Found python tool didn't know about `pip-compile-multi`
  - https://towardsdatascience.com/end-python-dependency-hell-with-pip-compile-multi-56eea0c55ffe
- Datasets in airflow
  - https://airflow.apache.org/docs/apache-airflow/2.5.2/authoring-and-scheduling/datasets.html
- Manning book Data Pipelines with Apache Airflow. 
  - [Examples](https://github.com/BasPH/data-pipelines-with-apache-airflow)

# Minio Configure

test using aws cli against minio https://min.io/docs/minio/linux/integrations/aws-cli-with-minio.html

Setup AWS CLI profile for minio.

```bash
aws configure --profile locals3

# answers
AWS Access Key ID [None]: user
AWS Secret Access Key [None]: password
Default region name [None]: us-east-1
Default output format [None]: ENTER

# ... 

#set signature version
aws configure set default.s3.signature_version s3v4 --profile locals3

#list buckets
aws --profile locals3 --endpoint-url http://localhost:9000 s3 ls 

# Note the IP may and is differnt from inside the docker containsers
aws --profile locals3 --endpoint-url http://locals3:9000 s3 ls 
```

To connect to an interactive shell in the docker container

```bash
docker compose exec webserver bash
```

S3 issue - https://github.com/apache/airflow/discussions/26979#discussioncomment-3928659

add to run `chmod 777 airflow-logs` to fix permission issue

- [S3 to Redshift](https://airflow.apache.org/docs/apache-airflow-providers-amazon/1.0.0/_modules/airflow/providers/amazon/aws/example_dags/example_s3_to_redshift.html)