## Simple http in golang

### Routes
- /healthz = Return if the application is alive
- /info = Return application version

### usage
to start locally (need python/python3 installed):
```
export DB=mysql.example.com:3306"
python3 main.py
curl http://localhost:8080/health
```
run: `curl http://localhost:8080/health`

### to start by the container on port 8080
```
docker build -t simplehttp:1.0.0 .
export DB=mysql.example.com:3306"
docker run -d -p 8080:8080 simplehttp:1.0.0
```
run: `curl http://localhost:8080/health`

## to start by kustomize
Adicione essa linha no seu /etc/hosts (ou equivalente do windows): `$(minikube ip) desafio.candidato.local`
```
minikube image build -t simplehttp:1.0.0 .
kubectl apply -k overlays/staging
kubectl apply -k overlays/production
```
run: `curl http://desafio.candidato.local/info`

```
kubectl apply -f base/service.yaml -f base/deployment.yaml -f base/configmap.yaml -n staging
kubectl port-forward svc/demo 8080:8080 -n staging
minikube image build -t simplehttp:1.0.0 .
```