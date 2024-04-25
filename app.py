#!/bin/usr/python3
from flask import Flask, render_template, request, redirect, url_for
from connect import DBStorage

app = Flask(__name__)
app.url_map.strict_slashes = False

db = DBStorage()

@app.route("/")
def home():
    posts = db.all_posts()
    return render_template("home.html", posts=posts)

@app.route("/blog/<id>")
def blog_post(id):
    return f"Post with id: {id}"

@app.route("/add", methods=['GET', 'POST'])
def add_post():
    if request.method == 'POST':
        # Handle form submission here
        post_title = request.form['title']
        post_text = request.form['text']
        db.add_post(post_title, post_text)
        return redirect(url_for('home'))
    else:
        return render_template("post_form.html")

@app.route("/edit", methods=['GET', 'PUT'])
def edit_post():
    return "EDIT post page"

@app.route("/delete", methods=['GET', 'DELETE'])
def delete_post():
    return "DELETE post page"


if __name__ == "__main__":
    app.run(host="0.0.0.0")