from flask import Flask, request, render_template
from predict import makeprediction

app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/prediction', methods=["POST"])
def startPrediction():
    #time_remaining, loc_x, loc_y
    time_remaining = request.form["time_remaining"]
    loc_x = request.form["loc_x"]
    loc_y = request.form["loc_y"]
    result = makeprediction(time_remaining, loc_x, loc_y)
    print str(result)
    return str(result)
    #return render_template('second.html', combined_shot_type = combined_shot_type)

if __name__ == '__main__':
    app.run(debug=True)