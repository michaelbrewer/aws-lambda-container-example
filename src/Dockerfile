FROM public.ecr.aws/lambda/python:3.9-arm64

RUN yum -y update && yum -y update --security && yum clean all

COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt  .
RUN  pip3 install -r requirements.txt --target "${LAMBDA_TASK_ROOT}"

CMD [ "app.handler" ]
