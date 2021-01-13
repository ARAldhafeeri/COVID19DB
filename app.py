from flask import Flask, request, render_template
from data import Data
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
#port = int(os.environ.get('PORT', 5000))

all_data = Data()
@app.route('/')
def index():
    print(all_data.get_cleaned_data())
    all_data.update_maps()
    all_data.update_lines()
    data = all_data.get_stats_data()
    return render_template("index.html", data = data)

@app.route('/map')
def map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)
