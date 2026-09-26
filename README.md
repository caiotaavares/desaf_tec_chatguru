## Simple http in golang

### Routes
- /healthz = Return if the application is alive
- /info = Return application version

### usage
to start locally (need go installed):
```
export DB=mysql.example.com:3306"
go run simplehttp.go 
```

### to start by the container on port 8080
```
export DB=mysql.example.com:3306"
docker run -d -p 8080:8080 simplehttp:"version"
```
