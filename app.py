from flask import Flask
from main.views import main_blueprint


app = Flask(__name__)

# Чтобы заработала кириллица
# app.config['JSON_AS_ASCII'] = False
app.config['app.json.ensure_ascii'] = False


app.register_blueprint(main_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()


# @app.route("/")
# def demo_json():
#     return "it works"

# response = app.test_client().get('/')
#
# print(response.status_code)
# print(response.data)
