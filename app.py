
from flask import Flask,render_template
app = Flask(__name__)



@app.route("/")

def fun():
    return "Hey dhruvesh"


@app.route("/two")

def fun2():
    return "Hey kalpak"




if __name__== "__main__":
    app.run(debug=True)



