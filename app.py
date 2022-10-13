from flask import Flask

from main.views import main_blueprint
from api.views import api_blueprint


app = Flask(__name__)

# Чтобы заработала кириллица
app.config["JSON_AS_ASCII"] = False

# Регистрируем main_blueprint и api_blueprint
app.register_blueprint(main_blueprint)
app.register_blueprint(api_blueprint)

# Добавляем путь к конфиг
app.config.from_pyfile("config.py")


@app.errorhandler(404)
def page_not_found(e):
	return "Ошибка 404. Такой страницы не существует."


@app.errorhandler(500)
def page_database_not_found(e):
	return "Ошибка 500. Ошибка базы данных."


@app.errorhandler(ValueError)
def page_file_not_found(e):
	return f"Ошибка ValueError. Такой страницы не существует. {e}"


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
	# app.run(debug=True)
	app.run()
