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
<<<<<<< HEAD
    app.run(debug=True)
=======
    circles_data.plot_maps()
    #circles_data.plot_bars()
    circles_data.plot_lines()
    app.run(host='0.0.0.0')
>>>>>>> cde8fc6849827f20213034504c75cfd57ca86826
