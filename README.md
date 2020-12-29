# CONTENTS:

## Build Phase 
* Entrypoint
* CMD
```
docker build .
docker build -t app_image:branch .
docker build -t app_image:v1 . 
```

## ENV
```
docker run -e HELLO_VAL
```
## VOLUME
```
docker run -p 5000:5000 -v $(pwd)/data/:/opt/ volume-test:latest
```
### Example Request:
```
curl --header "Content-Type: application/json" \
  --request POST \
  --data '{"username":"xyz","password":"xyz"}' \
  http://localhost:5000/index
```

## docker-compose 
File sync for development environment:
```
    volumes:
      - .:/code
```
```
docker-compose restart
```

## Docker Context:

```
head -c 1G </dev/urandom >myfile
```