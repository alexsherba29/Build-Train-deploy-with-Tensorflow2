# Build & train a neural network with Tensorflow 2 and Keras using GPU and deploy it using Flask and Gunicorn

This repository contains code for training an image recognition deep learning model to recognize different types of food. It also contains code about how to dockerize your code. 

## Installation

```bash
pip3 install -r requirements.txt 
```

## Usage
###  Part 1: Download the data 
In your web browser get in: https://www.kaggle.com/vermaavi/food11 and press download.

###  Part 2: Training 

Befor start edit in trainer.py the data dir path in the end of the script. 
```bash
cd Trainer
python3 trainer.py
```
After the training is finished copy the model dir to the server dir

To dockerize:
```bash
docker build -f Dockerfile -t food_detector:test0-trainer-gpu .
```
And to make it work write on the terminal:
``` bash
docker run --gpus all --rm -it  food_detector:test0-trainer-gpu
```
###  Part 3: Deploying 

```bash
cd Server
gunicorn -b 0.0.0.0:8080 predictor:app --timeout 90
```
In your web browser write: 0.0.0.0:8080
upload picture and press predict

To dockerize:
```bash
docker build -f Dockerfile -t food_detector:test0-server-gpu .
```
And to make it work write on the terminal:
``` bash
docker run --gpus all --rm -it -d -p 8080:8080 food_detector:test0-server-gpu
```
