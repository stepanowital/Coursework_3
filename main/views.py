from flask import Blueprint, render_template, request
from utils import get_posts_all, get_post_by_pk, get_comments_by_post_id, search_for_posts
main_blueprint = Blueprint('main_blueprint', __name__)


@main_blueprint.route('/')
def page_index():
    posts = get_posts_all()
    return render_template("index.html", posts=posts)


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