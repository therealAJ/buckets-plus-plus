from flask import Flask, request
from logistic_regression import helloworld

app = Flask(__name__)

@app.route('/', methods=["POST"])
def hello_world():
    #return helloworld()
    return request.form["hello"]

if __name__ == '__main__':
    app.run(debug=True)