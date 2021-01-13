from flask import Flask, request, render_template
from data import Data
import os
app = Flask(__name__)
app.config['SECRET_KEY'] = ''
#port = int(os.environ.get('PORT', 5000))

data = Data()
@app.route('/')
def index():
    print(data.get_cleaned_data())
    print(data.get_circles_data())
    circles_data = data.get_circles_data()
    return render_template("index.html", circles_data = circles_data)

@app.route('/map')
def map():
    return render_template("map.html")

if __name__ == "__main__":
    app.run(debug=True)