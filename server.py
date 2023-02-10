from flask import Flask, abort
from data import tools, mock_catalog

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


@app.get("/api/developer")
def developer():
    return json.dumps(tools)


@app.get("/api/developer/address")
def dev_address():
    address = tools["address"]
    return f'{address["street"]} #{address["number"]}, {address["city"]}, {address["zipcode"]}'


@app.get("/api/catalog")
def get_catalog():
    return json.dumps(mock_catalog)


@app.get("/api/catalog/count")
def count_products():
    count = len(mock_catalog)
    return json.dumps(count)


@app.get("/api/category/<cat>")
def prods_by_category(cat):
    results = []
    for prod in mock_catalog:
        if prod["category"] == cat:
            results.append(prod)

    return json.dumps(results)


@app.get("/api/product/<id>")
def prod_by_id(id):
    for prod in mock_catalog:
        if prod["_id"] == id:
            return json.dumps(prod)

    return abort(404, " we aint got none of that")


@app.get("/api/product/search/<text>")
def search_product(text):
    results = []
    for prod in mock_catalog:
        if text.lower() in prod["title"].lower():
            results.append(prod)

    return json.dumps(results)


# gave this a try, but it didn't work.

@app.get("/api/categories/<title>")
def checkKey(dic, key):
    for key, value in mock_catalog():
        return key
    else:
        return abort(404, " we no longer have any of those items")
        results.append(key)

    return json.dumps(results)


app.run(debug=True)
