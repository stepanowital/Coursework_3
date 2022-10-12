from flask import Blueprint, jsonify

from utils import get_posts_all, get_post_by_pk
from utils_logging import api_logger


api_blueprint = Blueprint('api_blueprint', __name__)


@api_blueprint.route("/api/posts")
def get_posts_json_page():
	data = get_posts_all()
	api_logger.info(f'Запрос /api/posts')
	return jsonify(data)


@api_blueprint.route("/api/posts/<int:post_id>")
def get_post_json_page(post_id):
	post = get_post_by_pk(post_id)
	api_logger.info(f'Запрос /api/posts/{post_id}')
	return jsonify(post)
