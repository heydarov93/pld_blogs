#!/bin/usr/python3
from flask import Flask, render_template, request

app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route("/")
def home():
  return "HOME page"


@app.route("/blog/<id>")
def blog_post(id):
  return f"Post with id: {id}"


@app.route("/add", methods=['GET', 'POST'])
def add_post():
  return "ADD post page"

@app.route("/edit", methods=['GET', 'PUT'])
def edit_post():
  return "EDIT post page"

@app.route("/delete", methods=['GET', 'DELETE'])
def delete_post():
  return "DELETE post page"







if __name__ == "__main__":
  app.run(host="0.0.0.0", debug=True)