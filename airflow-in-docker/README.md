# Airflow in docker

The airflow is not supported in windows. Can run it in a docker container.

## Prerequisites

Make sure that docker is installed.

## Steps

Go to the folder airflow-in-docker
```bash
cd airflow-in-docker
```

Run the airflow container using docker compose. It is using the official airflow image.

```bash
 docker compose -f docker-compose.yml up -d --build
```
Go to ```localhost:8080``` in browser. Login using the username - admin and password will be visible in logs. This password will be stored in the local mount folder airflow as well.

Make sure that the ```dag``` folder is in the mounted airflow folder. Store all the python dag files there. It will be visible in the UI.

