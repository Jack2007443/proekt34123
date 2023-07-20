from flask import Flask, render_template, request, flash

from sql_queries import *
from config import *

app = Flask(__name__) #створюємо Flask-додаток
app.config['SECRET_KEY'] = SECRET_KEY

@app.route("/")
@app.route("/index")
def index():
    posts = get_posts()
    category_list = get_categorys()
    return render_template("index.html", category_list = category_list, posts=posts)

@app.route("/category/<id>")
def category(id):
    posts = get_category_post(id)
    category = get_category_name(id)[0].upper()
    category_list = get_categorys()
    return render_template("category_posts.html", category_list = category_list, category = category, posts=posts)

@app.route("/post/<post_id>")
def post(post_id):
    post = get_post(post_id)
    category_list = get_categorys()
    return render_template("post.html", category_list = category_list, post=post)

@app.route("/post/new", methods=["POST", "GET"])
def new_post():
    category_list = get_categorys()
    if request.method == "POST":
        try:        
            image = request.files['image']
            image.save(PATH_IMG+image.filename)
            add_post(request.form['category'], request.form['title'], request.form['text'], image.filename)
            flash("Пост додано!", "alert-success")
        except:
            flash("Помилка додавання поста!", "alert-danger")

    return render_template("newpost.html", category_list = category_list)

if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True)

"""
venv\Scripts\activate
python app.py
"""