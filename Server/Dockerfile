# docker build -f Dockerfile -t food_trainer:test0-gpu_server .
# docker run --gpus all --rm -it -d -p 8080:8080 food_trainer:test0-gpu_server

FROM tensorflow/tensorflow:latest-gpu

WORKDIR /usr/src/app

COPY . .

RUN mkdir /usr/src/app/static

RUN pip3 install --upgrade pip && pip3 install flask gunicorn opencv-python

RUN apt-get update && apt-get install -y libgl1-mesa-dev

CMD exec gunicorn --bind :8080 --workers 1 --threads 8 --timeout 90 predictor:app


