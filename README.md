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
docker run -v $(pwd)/
```