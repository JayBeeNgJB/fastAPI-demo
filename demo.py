
from random import randrange
from fastapi import FastAPI
import winsound
from math import log10
import ipytone
import numpy as np
import matplotlib.pyplot as plt


from time import sleep
import sys
import time


print ("start fastapi")
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/data1")
async def beep():
    return {"message": "/data1"}
