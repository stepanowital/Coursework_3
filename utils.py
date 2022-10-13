import json

from config import PATH_POSTS, PATH_COMMENTS
from json import JSONDecodeError


def get_posts_all():
	"""Возвращает все посты из файла posts.json"""
	try:
		with open(PATH_POSTS, "r", encoding="utf-8") as file:
			posts = json.load(file)
			return posts
	except FileNotFoundError:
		raise ValueError("Файл posts.json не найден или не удаётся преобразовать")
	except JSONDecodeError:
		raise ValueError("Файл posts.json не удалось преобразовать")


def get_posts_by_user(user_name):
	"""Возвращает все посты указанного пользователя"""
	user_posts = []
	posts = get_posts_all()
	for post in posts:
		if post["poster_name"] == user_name:
			user_posts.append(post)
	if not user_posts:
		raise ValueError("Ошибка 500. Такого пользователя не существует.")
	return user_posts


def get_comments_by_post_id(post_id):
	"""Возвращает все комментарии указанного поста"""
	posts = get_posts_all()
	is_post_real = False
	for post in posts:
		if post["pk"] == post_id:
			is_post_real = True
	if not is_post_real:
		raise ValueError("Ошибка 500. Такого поста не существует.")

	try:
		with open(PATH_COMMENTS, "r", encoding="utf-8") as file:
			comments = json.load(file)
	except FileNotFoundError:
		print("Файл comments.json не найден")
		raise FileNotFoundError("Файл comments.json не найден")
	except JSONDecodeError:
		print("Файл comments.json не удаётся преобразовать")
		raise TypeError("Файл comments.json не удаётся преобразовать")

	comments_by_post_id = []
	for comment in comments:
		if comment["post_id"] == post_id:
			comments_by_post_id.append(comment)
	return comments_by_post_id


def search_for_posts(query):
	"""Возвращает список постов по указанному слову"""
	posts = get_posts_all()
	posts_query = []
	if not type(query) == str:
		raise AttributeError("Введенный запрос не является типом 'STR'")
	query_lower = query.lower()
	for post in posts:
		if query_lower in post["content"].lower():
			posts_query.append(post)
	return posts_query


def get_post_by_pk(pk):
	"""Возвращает пост по указанному номеру"""
	posts = get_posts_all()
	for post in posts:
		if post["pk"] == pk:
			return post
	return {}
