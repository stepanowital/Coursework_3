import logging
from flask import Blueprint, render_template, request, jsonify
from utils import *
main_blueprint = Blueprint('main_blueprint', __name__)


api_logger = logging.getLogger("one")
api_logger2 = logging.getLogger("two")

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/api.log")

formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt='%d-%m-%Y %H:%M:%S')

console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)

api_logger.addHandler(file_handler)
api_logger2.addHandler(console_handler)


@main_blueprint.route('/')
def page_index():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


@main_blueprint.route('/<blabla>')
def page_empty_index(blabla):
    raise FileNotFoundError(f'Страницы с индексом "{blabla}" не существует - ошибка 404')


@main_blueprint.route('/post/<int:postid>')
def page_posts(postid):
    post = get_post_by_pk(postid)
    comments = get_comments_by_post_id(postid)
    comments_len = len(comments)
    return render_template("post.html", post=post, comments=comments, comments_len=comments_len)


@main_blueprint.route('/search/')
def search_page():
    s = request.args.get("s")
    posts = search_for_posts(s)
    posts_len = len(posts)
    return render_template("search.html", posts=posts, s=s, posts_len=posts_len)


@main_blueprint.route('/users/<username>')
def user_page(username):
    user_posts = get_posts_by_user(username)
    user_name = user_posts[1]['poster_name']
    return render_template("user-feed.html", posts=user_posts, name=user_name)


@main_blueprint.route("/api/posts")
def get_posts_json_page():
    data = get_posts_all()
    api_logger.warning(f'Запрос /api/posts')
    return jsonify(data)


@main_blueprint.route("/api/posts/<int:post_id>")
def get_post_json_page(post_id):
    post = get_post_by_pk(post_id)
    api_logger.warning(f'Запрос /api/posts/{post_id}')
    return jsonify(post)


@main_blueprint.errorhandler(404)
def page_not_found(e):
    # Если запрос находится в пространстве URL блога
    if request.path.startswith('/'):
        # то возвращаем кастомную 404 ошибку для блога
        print("Cтатус-код 404 - страница не найдена")
    else:
        # в противном случае возвращаем
        # общую 404 ошибку  для всего сайта
        return render_template("404.html"), 404
