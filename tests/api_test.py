from app import app


keys_should_be = {"poster_name", "poster_avatar", "pic", "content", "views_count", "likes_count", "pk"}

def test_app_posts():
	""" Проверяем, получается ли нужный статус-код """
	response = app.test_client().get('/api/posts', follow_redirects=True)
	assert response.status_code == 200, "Статус-код всех постов неверный"
	assert type(response.json) == list, "Получен не список"
	assert response.json[1].keys() == keys_should_be, "Ключи в списке неверные"
	assert len(response.json) > 0, "Список постов пуст"


def test_app_post_id():
	""" Проверяем, получается ли нужный статус-код """
	response = app.test_client().get('/api/posts/1', follow_redirects=True)
	assert response.status_code == 200, "Статус-код всех постов неверный"
	assert type(response.json) == dict, "Получен не словарь"
	assert response.json.keys() == keys_should_be, "Ключи в списке неверные"
	assert len(response.json) > 0, "Список постов пуст"
