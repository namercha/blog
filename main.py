from flask import Flask, render_template
import requests
from post import Post

app = Flask(__name__)

posts = requests.get(url="https://api.npoint.io/6749c13772056218ba47").json()
post_object_list = []
for post in posts:
    post_object = Post(post["id"], post["title"], post["subtitle"], post["body"])
    post_object_list.append(post_object)


@app.route('/')
def get_all_posts():
    return render_template("index.html", all_posts=post_object_list)


@app.route('/post/<int:index>')
def show_post(index):
    requested_post = None
    for blog_post in post_object_list:
        if blog_post.id == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)
