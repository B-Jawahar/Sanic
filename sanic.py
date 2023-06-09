# -*- coding: utf-8 -*-
"""
Created on Fri Feb 17 14:54:06 2023

"""
from sanic import Sanic, json
from sanic.response import text
import datetime

def get_datetime():
    """
    Returns a string of the current date and time
    """
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def sum_x_y(x, y):
    """
    Returns the sum of x and y
    """
    return x + y

app = Sanic("CodeToAPI")

@app.route('/')
async def test(request):
    return json({'hello': 'world'})

@app.route('/getdatetime')
async def getdatetime(request):
    return json({'now': get_datetime()})

@app.get('/sumxy')
async def sumxy(request):
    parameters = request.args
    result = sum_x_y(int(parameters['x'][0]), int(parameters['y'][0]))
    return json({'result': result})

if __name__ == "__main__":
    app.run(host=HOST, port=PORT, debug=True,auto_reload=True)
