from flask import Flask,render_template, request, flash

from sql_queries import *
app = Flask(__name__) # Створюємо веб–додаток Flask

@app.route("/") # Вказуємо url-адресу для виклику функції
def index():
    posts = get_posts()
    category_list = get_categorys()
    return render_template("index.html",category_list = category_list, posts=posts) #Результат, що повертається у браузер
@app.route("/post/<post_id>") # Вказуємо url-адресу для виклику функції
def post(post_id):
    post = get_post(post_id)
    category_list = get_categorys()
    return render_template("post.html",category_list = category_list, post=post)

@app.route("/category/<id>") # Вказуємо url-адресу для виклику функції
def category(id):
    posts = get_category_post(id)

    category = get_category_name(id)[0].upper()
    category_list = get_categorys()
    return render_template("category_posts.html",category_list = category_list,category = category, posts=posts)

@app.route("/post/new", methods= ["POST", "GET"])
def new_post():
    category_list = get_categorys() 
    if request.method == "POST": 
       image = request.files['image']
       image.save(PATH_IMG+image.filename)
       add_post(request.form['category'], request.form['title'], request.form['text'])
       flash("Пост додано"), "alert-success")
    return render_template("newpost.html", category_list = category_list)
if __name__ == "__main__":
    app.config['TEMPLATES_AUTO_RELOAD'] = True  # автоматичне оновлення шаблонів
    app.run(debug=True) # Запускаємо веб-сервер з цього файлу

"""
venv/Scripts/activate
python app.py
"""


