#!/bin/bash
echo "Building Docker Image"
docker build . -t adriangrebin/prototype

echo "Pushing Docker Image"
docker push adriangrebin/prototype
