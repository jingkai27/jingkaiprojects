from flask import Flask, render_template, request
import requests
BLOG_POSTS_ENDPOINT="https://api.npoint.io/f9cdde98f31756d428b6"

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

@app.route('/contact', methods=["GET", "POST"])
def dis_contact():
    if request.method == 'POST':
        print(request.form["name"])
        print(request.form["email"])
        print(request.form["phone"])
        print(request.form["message"])
        return render_template("contact.html", msg_sent=True)
    else:
        return render_template("contact.html",msg_sent=False)

@app.route('/post<id>')
def get_post(id):
    num = int(id)
    return render_template("post.html", data=blog_posts[num-1])

if __name__ == "__main__":
    app.run(debug=True)