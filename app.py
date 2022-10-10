from flask import Flask
from main.views import main_blueprint


app = Flask(__name__)

# Чтобы заработала кириллица
app.config['app.json.ensure_ascii'] = False


app.register_blueprint(main_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run(debug=True)
