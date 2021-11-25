# docker build -f Dockerfile -t food_trainer:test0 .
# docker run --gpus all --rm -it  food_trainer:test0-gpu

FROM tensorflow/tensorflow:latest-gpu

WORKDIR /usr/src/app

COPY . .

RUN apt-get update

RUN pip install -r /usr/src/app/requirements.txt

ENTRYPOINT [ "python3", "/usr/src/app/trainer.py" ]



