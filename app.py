from flask import Flask,request, url_for, redirect, render_template
import uvicorn
from fastapi import FastAPI
import pickle
import numpy as np

from pydantic import BaseModel

app=FastAPI()

@app.get('/')
def hello_world():
    return {'message': 'Hello, World'}

if __name__=='__main__':
     uvicorn.run(app,host="127.0.0.1",port=8000)
    