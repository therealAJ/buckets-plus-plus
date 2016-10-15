from flask import Flask, request, render_template
from logistic_regression import predict


app = Flask(__name__)

@app.route('/') 
def home():
    return render_template('home.html')

@app.route('/prediction', methods=["POST"])
def startPrediction():
    combined_shot_type = request.form["combined_shot_type"]
    loc_x = request.form["loc_x"]
    loc_y = request.form["loc_y"]
    seconds_remaining = request.form["seconds_remaining"]
    period = request.form["period"]
    season = request.form["season"]
    shot_made = request.form["shot_made"]
    shot_type_flag = request.form["shot_type_flag"]
    game_date = request.form["game_date"]
    opponent = request.form["opponent"]
    predict(combined_shot_type, loc_x, loc_y, seconds_remaining, period, season, shot_made, shot_type_flag, game_date, opponent)
    return render_template('second.html', combined_shot_type = combined_shot_type)

if __name__ == '__main__':
    app.run(debug=True)