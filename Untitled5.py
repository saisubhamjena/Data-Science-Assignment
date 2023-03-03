#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Q1. What is Flask Framework? What are the advantages of Flask Framework?
"""
Flask is a micro web framework that has minimal dependencies on external libraries, written in Python, which was formed for a faster and easier use, and
also has the ability to scale up to complex applications.

Advantages of Flask Framework:
1.Flask is considered the best framework for light web application serving, it is a lightweight framework 
2.The Flask framework is easy to understand, that is why it is best for beginners. 
3.It is very flexible and easy.Almost all the parts of flask are open to change, unlike some other web frameworks.
4.Using Flask for web development allows for unit testing through its integrated support, built-in development server, fast debugger, and 
  restful request dispatching.
"""


# In[3]:


#Q2. Create a simple Flask application to display ‘Hello World!!’. Attach the screenshot of the output in Jupyter Notebook.

from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1>Hello world</h1>"

if __name__=="__main__":
    app.run(host="0.0.0.0")


# <img src="HW.png">

# In[ ]:


#Q3. What is App routing in Flask? Why do we use app routes?
"""
App Routing means mapping the URLs to a specific function that will handle the logic for that URL. Modern web frameworks use more meaningful URLs 
to help users remember the URLs and make navigation simpler.
App routing is used to map the specific URL with the associated function that is intended to perform some task.
"""


# In[ ]:


#Q4. Create a “/welcome” route to display the welcome message “Welcome to ABC Corporation” and a “/”.
#route to show the following details: Company Name: ABC Corporation Location: India Contact Detail: 999-999-9999

from flask import Flask

app = Flask(__name__)

@app.route("/welcome")
def welcome():
    return "Welcome to ABC Corporation"
@app.route("/")
def details():
    return "Company Name:ABC Corporation \nLocation: India \nContact Detail: 999-999-9999"

if __name__=="__main__":
    app.run(host="0.0.0.0")


# <img src="Welcome.png">

# <img src="Details.png">

# In[ ]:


#Q5. What function is used in Flask for URL Building? Write a Python code to demonstrate the working of the url_for() function.
"""
To build a URL to a specific function, use the url_for() function. It accepts the name of the function as its first argument and any number 
of keyword arguments, each corresponding to a variable part of the URL rule."""

from flask import url_for, Flask

appFlask = Flask(__name__)

@appFlask.route('/home')
def home():
   return 'We are in Home Page!'
with appFlask.test_request_context():
    print(url_for('login'))


# In[ ]:





# In[ ]:




