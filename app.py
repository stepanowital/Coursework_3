from flask import Flask
from main.views import main_blueprint


app = Flask(__name__)

# Чтобы заработала кириллица
app.config['app.json.ensure_ascii'] = False

# Регистрируем main_blueprint
app.register_blueprint(main_blueprint)

# Добавляем путь к конфигу
app.config.from_pyfile("config.py")


# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run(debug=True)



