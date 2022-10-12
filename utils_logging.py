import logging


api_logger = logging.getLogger("one")
api_logger2 = logging.getLogger("two")

console_handler = logging.StreamHandler()
file_handler = logging.FileHandler("logs/api.log")

logging.basicConfig(level=logging.INFO)
formatter_one = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s", datefmt='%d-%m-%Y %H:%M:%S')

console_handler.setFormatter(formatter_one)
file_handler.setFormatter(formatter_one)

api_logger.addHandler(file_handler)
api_logger2.addHandler(console_handler)
