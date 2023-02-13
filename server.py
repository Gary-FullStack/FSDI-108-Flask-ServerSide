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


@app.get("/api/categories")
def get_categories():
    results = []
    for prod in mock_catalog:
        cat = prod["category"]
        if cat not in results:
            results.append(cat)

    return json.dumps(results)


@app.get("/api/total")
def get_total():
    total = 0
    for prod in mock_catalog:
        total += prod["price"]

    return json.dumps(total)


@app.get("/api/lower/<price>")
def get_lower(price):
    price = float(price)
    results = []
    for prod in mock_catalog:
        if prod["price"] <= price:
            results.append(prod)
    return json.dumps(results)


    # challenge,  find and return least costly items
# create a cheapest = mock_catalog[0]
# for loop to travel the list
# get every prod from the list
# if the price of prod is lower than the price of cheapest
# then update cheapest to be the prod (cheapest = prod)
app.run(debug=True)
