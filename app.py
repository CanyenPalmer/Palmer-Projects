from flask import Flask, render_template, send_from_directory
import os
from utils.markdown_parser import load_posts

app = Flask(__name__)
POSTS_DIR = "posts"

@app.route("/")
def home():
    posts = load_posts(POSTS_DIR)
    return render_template("index.html", posts=posts)

@app.route("/blog")
def blog():
    posts = load_posts(POSTS_DIR)
    return render_template("blog.html", posts=posts)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/posts/<slug>")
def post(slug):
    filepath = os.path.join(POSTS_DIR, f"{slug}.md")
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            content = f.read()
        return render_template("blog_post.html", content=content)
    return "Post not found", 404

if __name__ == "__main__":
    app.run(debug=True)
