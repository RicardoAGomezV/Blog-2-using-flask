from datetime import datetime
from email.message import EmailMessage
from pprint import pprint
from flask import Flask, render_template, request
import requests
import smtplib

from parameters import MY_EMAIL, MY_PASSWORD

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


# @app.route("/contact")
# # Defining the route for the contact page
# def contact():
    
#     # Rendering the contact.html template
#     return render_template("contact.html")


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


# Define a route for the contact form, allowing both GET and POST methods
@app.route("/contact", methods=['POST', 'GET'])
def read_contact_form():
    
    # If the request method is POST, it means the user has submitted the form
    if request.method == 'POST':
        
        # Get the form data. The request.form object is an ImmutableMultiDict 
        # that you can use to access the submitted form data.
        data = request.form 
    
        # Extract the individual form fields into a dictionary
        data_user= { 
            'user_name'     : data['name'], 
            'email' : data['email'], 
            'phone_number'    : data['phone'], 
            'msg'      : data['message'] , 
        } 
        
        # Set a flag to indicate that the form has been sent
        sent=True  
                  
        # Print the user data to the console for debugging purposes
        pprint(data_user)    
        
        # creates SMTP session
        s = smtplib.SMTP('smtp.gmail.com', 587)

        # start TLS for security
        s.starttls()

        # Authentication
        s.login(MY_EMAIL, MY_PASSWORD)

        # create an instance of EmailMessage class. 
        msg = EmailMessage()
        msg['Subject'] = 'User from your blog sent you a message'
        msg['From'] = MY_EMAIL
        msg['To'] = MY_EMAIL
        content=f"Name: {data_user['user_name']}\nEmail: {data_user['email']}\nPhone: {data_user['phone_number']}\nMessage:{data_user['msg']}"
        msg.set_content(content)

        # sending the mail
        s.send_message(msg)

        # terminating the session
        s.quit()        
        
        # Render the contact form template and pass the 'sent' flag to it
        return render_template("contact.html", sent_form=sent)   
    
    # If the request method is GET, it means the user is loading the form page
    else:
        
        # Render the contact form template
        return render_template("contact.html")

   


if __name__ == '__main__':
    app.run(debug=True)
    # Running the Flask application in debug mode
