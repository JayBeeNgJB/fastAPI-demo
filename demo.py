# main.py

from random import randrange
from fastapi import FastAPI
import winsound
from math import log10
import numpy as np
import matplotlib.pyplot as plt


from time import sleep
import sys
import time

LED_status = 0

print ("start fastapi")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/onLed")
async def onLED():
    global LED_status
    LED_status = 1
    return {}

@app.get("/offLed")
async def onLED():
    global LED_status
    LED_status = 0
    return {}

@app.get("/{url}")
async def returnURL():
    return {LED_status}
#uvicorn demo:app --host 0.0.0.0 --port 80
