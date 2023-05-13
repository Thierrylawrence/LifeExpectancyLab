# flask --app data_server run
from flask import Flask
from flask import render_template
from flask import request
import json


app = Flask(__name__, static_url_path='', static_folder='static')

@app.route('/')
def index():
    f = open("templates/life_expectancy.json", "r")
    data = json.load(f)
    f.close()

    selected_option = 2001
    return render_template('index.html', data = data, selected_option=selected_option)

@app.route('/year')
def year():


    requested_year = request.args.get('year')
    return render_template('year.html', year = requested_year)

app.run(debug=True)
