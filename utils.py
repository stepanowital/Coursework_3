import json
from json import JSONDecodeError

def get_posts_all():
	try:
		with open("data/posts.json", "r", encoding="utf-8") as file:
			posts = json.load(file)
			return posts
	except FileNotFoundError:
		print("Файл posts.json не найден")
	except JSONDecodeError:
		print("Файл posts.json не удаётся преобразовать")


# get_posts_all()


def get_posts_by_user(user_name):
	user_posts = []
	posts = get_posts_all()
	for post in posts:
		if post["poster_name"] == user_name:
			user_posts.append(post)
	if not user_posts:
		raise ValueError("Такого пользователя не существует")
	return user_posts


# print(get_posts_by_user("leo"))
# print(get_posts_by_user("leo")[1]['poster_name'])


def get_comments_by_post_id(post_id):
	posts = get_posts_all()
	is_post_real = False
	for post in posts:
		if post["pk"] == post_id:
			is_post_real = True
	if not is_post_real:
		raise ValueError("Такого поста не существует")

	try:
		with open("data/comments.json", "r", encoding="utf-8") as file:
			comments = json.load(file)
	except FileNotFoundError:
		print("Файл comments.json не найден")
	except JSONDecodeError:
		print("Файл comments.json не удаётся преобразовать")

	comments_by_post_id = []
	for comment in comments:
		if comment["post_id"] == post_id:
			comments_by_post_id.append(comment)
	return comments_by_post_id


# print(get_comments_by_post_id(5))


def search_for_posts(query):
	posts = get_posts_all()
	posts_query = []
	for post in posts:
		if query.lower() in post["content"].lower():
			posts_query.append(post)
	return posts_query


# print(search_for_posts(""))


def get_post_by_pk(pk):
	posts = get_posts_all()
	for post in posts:
		if post["pk"] == pk:
			return post


# print(get_post_by_pk(8))
