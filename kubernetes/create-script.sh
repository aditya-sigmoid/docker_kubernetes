kubectl create -f deployment-airflow.yaml
kubectl create -f deployment-postgres.yaml
kubectl create -f service-airflow.yaml
kubectl create -f service-postgres.yaml

# to tackle fernet key error

# FERNET_KEY=$(python -c "from cryptography.fernet import Fernet; FERNET_KEY = Fernet.generate_key().decode(); print(FERNET_KEY)")
# export FERNET_KEY=$FERNET_KEY