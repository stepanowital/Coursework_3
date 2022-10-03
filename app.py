from flask import Flask
from main.views import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

# Запускаем сервер, только если файл запущен, а не импортирован
if __name__ == "__main__":
    app.run()