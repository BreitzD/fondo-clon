from flask import Flask, render_template, request, redirect
from bson import ObjectId
from pymongo import MongoClient

app= Flask(__name__)

client = MongoClient("mongodb://localhost:27017")
bd = client.fondos_flask
miexercicio = bd.fondos


@app.route("/")
def aportar_page():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)