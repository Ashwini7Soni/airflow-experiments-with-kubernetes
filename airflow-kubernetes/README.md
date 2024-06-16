# Airflow in kubernetes

Use the helm chart above. Configure the externalDatabase and the volume mount storage class. If required in you use case configure externalRedis as well.\

Either use port forwarding or ingress or nodeport to expose the web ui and the flower ui to your local system.\

```bash
kubectl port-forward svc/airflow-web 8080:8080 --namespace airflow
kubectl port-forward svc/airflow-flower 5555:5555 --namespace airflow
```

#### Note: Most of the deployment errors will come in volume mount and external database configuration. Notice the storage classes. The storage classes for logs and dags will not wait for a pod while others will.