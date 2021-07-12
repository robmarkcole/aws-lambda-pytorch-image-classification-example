# aws-lambda-pytorch-image-classification-example
Example of implementing a pytorch image classifier service using AWS lambda. Cold start time can be 10-20 seconds. Subsequent inferences happen in approx 300-500 ms.

```
docker build -t lambda-pytorch-example .

docker run -p 9000:8080 \
-e AWS_ACCESS_KEY_ID=$AWS_ACCESS_KEY_ID \
-e AWS_SECRET_ACCESS_KEY=$AWS_SECRET_ACCESS_KEY \
aws-lambda-pytorch-image-classification-example:latest
```

To connect to the shell of the running container, check the container name with `docker container ls` then `docker exec -it <container_name> /bin/bash`. Run the `request.py` file to make a request.

## CICD
A github action is used to push the latest release to ECR, enter required credentials in repo secrets

## References
* https://github.com/gokavak/lambda-docker-image-pytorch-xgboost