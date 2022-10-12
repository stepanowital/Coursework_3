import pytest

from utils import get_posts_all, get_posts_by_user, get_comments_by_post_id, search_for_posts, get_post_by_pk


def test_get_posts_all_list():
	assert type(get_posts_all()) == list, "Функция get_posts_all возвращает не список"


def test_get_posts_all_empty():
	assert get_posts_all() != [], "Функция get_posts_all возвращает пустой список"


def test_get_posts_by_user_leo():
	name = "leo"
	assert type(get_posts_by_user(name)) == list, "Функция get_posts_by_user возвращает не список"


def test_get_posts_by_user_leo_not_empty():
	name = "leo"
	assert get_posts_by_user(name) != [], 'Функция get_posts_by_user("leo") возвращает пустой список'


def test_get_posts_by_user_johnny():
	name = "johnny"
	assert type(get_posts_by_user(name)) == list, "Функция get_posts_by_user возвращает не список"


def test_get_posts_by_user_johnny_not_empty():
	name = "johnny"
	assert get_posts_by_user(name) != [], 'Функция get_posts_by_user("johnny") возвращает пустой список'


def test_get_posts_by_user_hank():
	name = "hank"
	assert type(get_posts_by_user(name)) == list, "Функция get_posts_by_user возвращает не список"


def test_get_posts_by_user_hank_not_empty():
	name = "hank"
	assert get_posts_by_user(name) != [], 'Функция get_posts_by_user("hank") возвращает пустой список'


def test_get_posts_by_user_larry():
	name = "larry"
	assert type(get_posts_by_user(name)) == list, "Функция get_posts_by_user возвращает не список"


def test_get_posts_by_user_larry_not_empty():
	name = "larry"
	assert get_posts_by_user(name) != [], 'Функция get_posts_by_user("larry") возвращает пустой список'


def test_get_posts_by_user_ValueError():
	with pytest.raises(ValueError):
		get_posts_by_user("")


def test_get_comments_by_post_id():
	comments = get_comments_by_post_id(1)
	assert type(comments) == list, "Функция get_comments_by_post_id возвращает не список"


def test_get_comments_by_post_id_empty():
	comments = get_comments_by_post_id(8)
	assert comments == [], "Функция get_comments_by_post_id возвращает не пустой список"


def test_get_comments_by_post_id_ValueError():
	with pytest.raises(ValueError):
		get_comments_by_post_id("")


def test_search_for_posts():
	query = search_for_posts("1")
	assert type(query) == list, "Функция search_for_posts возвращает не список"


def test_search_for_posts_empty():
	posts = search_for_posts("")
	assert posts != [], "Функция search_for_posts возвращает не пустой список"


def test_search_for_posts_AttributeError():
	with pytest.raises(AttributeError):
		search_for_posts(1)


def test_get_post_by_pk():
	post = get_post_by_pk(1)
	assert type(post) == dict, "Функция get_post_by_pk возвращает не словарь"


def test_get_post_by_pk_empty():
	post = get_post_by_pk("5")
	assert post == {}, "Функция get_post_by_pk возвращает не словарь"
