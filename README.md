# Lambda Container example

Python 3.9 arm function using a container image

## Build and deploy using AWS SAM

> [SAM guideline](https://aws.amazon.com/blogs/compute/using-container-image-support-for-aws-lambda-with-aws-sam/)

```script
sam build
sam deploy --guided
```

## Manual building and deploying

```script
cd src/
ACCOUNT_ID=<YOUR_AWS_ACCOUNT_ID>
AWS_REGION=us-west-2
docker build -t hello-world .
aws ecr get-login-password --region $AWS_REGION | docker login --username AWS --password-stdin $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com
aws ecr create-repository --repository-name hello-world --image-scanning-configuration scanOnPush=true --image-tag-mutability MUTABLE
docker tag  hello-world:latest $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-world:latest
docker push $ACCOUNT_ID.dkr.ecr.$AWS_REGION.amazonaws.com/hello-world:latest
```
