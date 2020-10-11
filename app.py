from flask import Flask, request, render_template
from data import Data
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = 'kajlkafsdljhdsfaljkfhljk3398339p83293unw'
port = int(os.environ.get('PORT', 5000))
@app.route('/')
def index():
    return render_template("index.html")

@app.route('/map')
def map():
    return render_template("map.html")

@app.context_processor
def context_processor():
    return dict(circles_data= circles_data.get_circles_data())

if __name__ == "__main__":
    circles_data = Data()
    circles_data.plot_maps()
    circles_data.plot_bars()
    circles_data.plot_lines()
    app.run(debug=True, port=por)
