FROM public.ecr.aws/lambda/python:3.8

COPY requirements.txt ./
RUN python3.8 -m pip install -r requirements.txt

COPY model model
COPY app.py ./
COPY utils.py ./

CMD ["app.lambda_handler"]