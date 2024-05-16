from datetime import datetime
from pprint import pprint
from flask import Flask, render_template
import requests


# Initializing the Flask application
app = Flask(__name__)

# URL where the information about our blog is available in JSON format
url = "https://api.npoint.io/d1d60738d43254255bdf"

def current_date():
    # Getting the current date and time
    date = datetime.now()
    
    # Returning the current date and time
    return date

def get_data():
    # Making a GET request to the URL
    request = requests.get(url)
    
    # Converting the response to JSON format
    request_json = request.json()
    
    # pprint(request_json)  # Uncomment to print the JSON data in a pretty format (optional)
    
    # Returning the JSON data
    return request_json


@app.route("/")
# Defining the route for the homepage
def home():
    
    # Getting the data from the URL
    my_data = get_data()
    
    # Rendering the index.html template with data and current date
    return render_template("index.html", data=my_data, date=current_date())


@app.route("/contact")
# Defining the route for the contact page
def contact():
    
    # Rendering the contact.html template
    return render_template("contact.html")


# Defining the route for the about page
@app.route("/about")
def about():

    # Rendering the about.html template
    return render_template("about.html")


# Defining the route for individual blog posts
@app.route("/post/<id_num>")
def post(id_num):
    
    print(type(id_num))
    # Printing the type of the id_num variable
    
    # Getting the current date and time
    today_date = current_date()
    
    
    # Getting the data from the URL
    my_data = get_data()

    for post in my_data:
        
        # In the API, the id value is an integer
        if post['id'] == int(id_num):
            
            post_data = post
            # Storing the post data if the id matches

    return render_template("post.html", post=post_data, current_date=today_date)
    # Rendering the post.html template with the post data and current date

if __name__ == '__main__':
    app.run(debug=True)
    # Running the Flask application in debug mode
