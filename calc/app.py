# Put your app in here.

from flask import Flask, request
from operations import add, sub, mult, div

app = Flask(__name__)

@app.route('/add')
def add_op():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = add(a, b)
    return f"{result}"

@app.route('/sub')
def sub_op():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = sub(a, b)
    return f"{result}"

@app.route('/mult')
def mult_op():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = mult(a, b)
    return f"{result}"

@app.route('/div')
def div_op():
    a = int(request.args["a"])
    b = int(request.args["b"])
    result = div(a, b)
    return f"{result}"

math_ops = {
        'add': add,
        'sub': sub,
        'mult': mult,
        'div': div
    }

@app.route('/math/<math_op>')
def any_math(math_op):

    a = int(request.args["a"])
    b = int(request.args["b"])
    result = math_ops[math_op](a, b)
    return f"{result}"