## Aplicação http python simples

### Rotas
- /health = Retorna se a aplicação está rodando
- /info = Retorna as variáveis `version`, `db` e `hostname`

### uso
#### local
para iniciar localmente (precisa python/python3 instalado):
```
pip install -r requirements.txt
export DB=mysql.example.com:3306"
python3 main.py
curl http://localhost:8080/health
```
run: `curl http://localhost:8080/info`

#### para iniciar no container na porta `8080`
```
docker build -t simplehttp:1.0.0 .
export DB=mysql.example.com:3306"
docker run -d -p 8080:8080 simplehttp:1.0.0
```
run: `curl http://localhost:8080/info`

#### para iniciar pelo kustomize no `minikube`
Atualize o /etc/hosts (ou windows/minikube equivalente): `$(minikube ip) desafio.candidato.local` ou `$(minikube ip) staging.desafio.candidato.local`
```
minikube image build -t simplehttp:1.0.0 .
kubectl apply -k overlays/staging
kubectl apply -k overlays/production
```
run: `curl http://desafio.candidato.local/info` ou `curl http://staging.desafio.candidato.local/info`

### Estrutura
#### Aplicação de código fonte
- `main.py` Servidor web construído com FastAPI e que expõe as rotas /health e /info
- `test_main.py`Suite de testes com pytest
- `requirements.txt` Lista de bibliotecas necessárias

#### Empacotamento
- `Dockerfile` Constrói a imagem
- `ci.yaml` Pipeline automatizado do github actions com: `run-tests`, `kustomize-lint` e `build-and-push`

#### Recursos de infraestrutura base
- `base/*` Contém o modelo etstrutural da aplicação
- `deployment.yaml` Controla o ciclo de vida do deployment da aplicação, bem como recursos e injeção de variáveis de ambiente
- `service.yaml` Exposição interna da aplicação via ClusterIP, redirecionando o tráfego da pota 80 para a 8080
- `configMap.yaml` Guarda variáveis de ambiente que são injetadas na aplicação
- `ingress.yaml` Controla e entrada do tráfego HTTP externo usando nginx e associa hosts aos serviços
- `namespace.yaml` Cria o namespace necessário para rodar a aplicação (isolamento lógico de rede e recursos)

#### overlay
##### /staging
Adiciona o prefixo `staging-` aos nomes dos recursos e aplica a label `variant: staging`.
- `namespace.yaml` Cria e direciona os recursos para o namespace `staging`
- `configMap.yaml` Aponta mysqlDB para a string correspondente ao "banco de staging".
- `ingress.yaml` configura o host de staging

##### /production
Adiciona o prefixo `production-` aos nomes dos recursos e aplica a label `variant: production`.
- `namespace.yaml` Cria e direciona os recursos para o namespace `prod`
- `configMap.yaml` Aponta mysqlDB para a string correspondente ao "banco de produção".
- `ingress.yaml` configura o host de produção
- `deployment.yaml` escala o número de réplicas para 2