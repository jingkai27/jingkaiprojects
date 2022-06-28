from flask import Flask, render_template
import requests
BLOG_POSTS_ENDPOINT =  "https://api.npoint.io/33005ada6dbbdb807cd1"

app = Flask(__name__)

r = requests.get(BLOG_POSTS_ENDPOINT)
r.raise_for_status()
blog_posts = r.json()

@app.route('/')
def home():
    return render_template("index.html", posts=blog_posts)

@app.route('/about')
def dis_about():
    return render_template("about.html")

@app.route('/contact')
def dis_contact():
    return render_template("contact.html")

@app.route('/post<id>')
def get_post(id):
    num = int(id)
    return render_template("post.html", data=blog_posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)