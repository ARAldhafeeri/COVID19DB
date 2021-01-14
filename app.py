from flask import Flask, request, render_template
from data import Data
import pandas as pd
import os
import json
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
#port = int(os.environ.get('PORT', 5000))

all_data = Data()
@app.route('/')
def index():
    all_data.update_maps()
    all_data.update_lines()
    data = all_data.get_stats_data()
    return render_template("index.html", data = data)

@app.route('/maps/deaths/')
def deaths_map():
    return render_template("deaths_map.html")

@app.route('/maps/recovered/')
def recovered_map():
    return render_template("recovered_map.html")


@app.route('/maps/confirmed/')
def confirmed_map():
    return render_template("confirmed_map.html")

@app.route('/lines/deaths/')
def deaths_lines():
    return render_template("fig_line_deaths.html")

@app.route('/lines/recovered/')
def recovered_lines():
    return render_template("fig_line_recovered.html")


@app.route('/lines/confirmed/')
def confirmed_lines():
    return render_template("fig_line_confirmed.html")

@app.route('/table/')
def display_table():
    table_data = all_data.get_cleaned_data()
    return render_template('table.html', tables=[table_data.to_html(classes='data')], titles=table_data.columns.values)

@app.route('/api/cleaned_data/')
def request_data():
    json_data = all_data.get_cleaned_data()
    return render_template('request.html', data = json_data.to_json())


if __name__ == "__main__":
    app.run(host="0.0.0.0")
