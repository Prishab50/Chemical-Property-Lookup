#!/bin/bash

echo "Building docker image"
docker build -t chemical-lookup:latest .

echo "Running unit tests inside Docker"
docker run --rm chemical-lookup:latest \
  python -m unittest tests/unit-tests.py


echo "Running docker container"
docker run --rm -p 5000:5000 chemical-lookup:latest &


sleep 2

echo "Running health check"
curl http://localhost:5000/health