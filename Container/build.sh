#!/bin/bash
echo "Building Docker Image"
docker build . -t agrebin/prototype

echo "Pushing Docker Image"
docker push agrebin/prototype
