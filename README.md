## Simple http python application

### Routes
- /health = Return if the application is alive
- /info = Return application `version`, `db` variable content and `hostname`

### usage
to start locally (need python/python3 installed):
```
pip install -r requirements.txt
export DB=mysql.example.com:3306"
python3 main.py
curl http://localhost:8080/health
```
run: `curl http://localhost:8080/info` 

### to start by the container on port 8080
```
docker build -t simplehttp:1.0.0 .
export DB=mysql.example.com:3306"
docker run -d -p 8080:8080 simplehttp:1.0.0
```
run: `curl http://localhost:8080/info`

## to start by kustomize on minikube
Update your /etc/hosts (or windows equivalent): `$(minikube ip) desafio.candidato.local`
```
minikube image build -t simplehttp:1.0.0 .
kubectl apply -k overlays/staging
kubectl apply -k overlays/production
```
run: `curl http://desafio.candidato.local/info`