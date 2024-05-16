from datetime import datetime
from pprint import pprint
from flask import Flask, render_template
import requests

app = Flask(__name__)


# URL where the information about our blog is available in JSON format
url="https://api.npoint.io/d1d60738d43254255bdf"

def current_date():
    date=datetime.now()
    return date

  


def get_data():
    request= requests.get(url)
    
    request_json = request.json()
    
    pprint(request_json)

    return request_json


@app.route("/")
def home():
    
    
    my_data=get_data()
    
    return render_template("index.html", data=my_data, date=current_date())


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == '__main__':
    app.run(debug=True)