# Airflow Playground


This is a playground for Apache Airflow. The goal is to get more deep understanding of Airflow and its capabilities. I've played with Airflow in the past, but goal here is to get more hands-on experience with it.


## Tasks

- [x] Airflow docker starting
- [x] Postgres Database started
- [x] Create a DAG that runs a bash function
- [ ] Create a DAG that runs a Python function
- [ ] Create a DAG that reads table in Postgres
- [ ] Mock S3 with Minio or localstack
- [ ] Create a DAG that reads table in Postgres and outputs to S3


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