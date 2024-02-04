
from flask import Flask,render_template
app = Flask(__name__)



@app.route("/")

def fun():
    return "Hey dhruveshnew"


@app.route("/two")

def fun2():
    return "Hey kalpak"

@app.route("/three",methods=["POST"])
def fun3():
    value1 = int(request.form["value1"])
    value2 = int(request.form["value2"])
    return str(value1+value2)



