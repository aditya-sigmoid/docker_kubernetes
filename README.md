# docker_kubernetes


# Docker task
                      
 Write a simple airflow dag to connect with db(postgres) and add entry in db for each execution (Time of dag execution)
 Add the given dag into the container and install dependencies.
 Use docker compose to launch airflow and postgres
 Schedule the dag
 Validate entry in postgres
 
 
 # Steps
  1. docker compose file up
  2. localhost webserver 
  3. trigger dag
 
                    
# Kubernetes Task

 Create deployment and service for above airflow and postgres (you can use postgres helm chart for postgres deployment)
 Deploy airflow and postgres
 Schedule the dag
 Validate entry in postgres
 
 # Steps
  1. minikube start
  2. mount our dags folder into the /mnt/airflow/dags folder by command ``` minikube mount ./dags:/mnt/airflow/dags ```.
  3. create deployment and service file by executing the script (create) ``` chmod +x ./create-script.sh ```  then ``` ./create-script.sh```
  4. ```kubectl get pods```
  5. then go to airflow container by ``` kubectl exec -it <pod-name> -- bash```.
  6. ```airflow initdb``` encounter an error by this command error-(raise InvalidToken cryptography.fernet.InvalidToken)
  
        ```FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")```
        
        ```export FERNET_KEY=$FERNET_KEY```
        
  7. ```kubectl get svc``` 
 
  8. ```kubectl port-forward svc/<airflow-service name> 8080:8080```
  9.   trigger the DAG.
