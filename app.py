from flask import Flask, request, render_template
from data import Data
app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret'

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
    circles_data.plot_map()
    app.run(debug=True)
