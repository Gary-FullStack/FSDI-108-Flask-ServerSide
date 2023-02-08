from flask import Flask
from data import tools

import json


app = Flask(__name__)


@app.get("/")
def index():
    return "Hiya folks!"


@app.get("/about")
def about():
    return "Gary!"


@app.get("/contact")
def contact():
    return "admin@fullstackscout.com"

    #################################################################
    ############  API --> JSOn ######################################
    #############################################################


# @app.get("/api/developer")
# def developer():
#     return json.dumps(tools)


app.get("/api/developer/address")


def dev_address():
    address = tools["address"]
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


app.run(debug=True)
