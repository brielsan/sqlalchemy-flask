from dotenv import load_dotenv
import os

load_dotenv()

user = os.environ["MYSQL_USER"]
password = os.environ["MYSQL_PASSWORD"]
host = os.environ["MYSQL_HOST"]
database = os.environ["MYSQL_DATABASE"]
secret_key = os.environ["SECRET_KEY"]

DATABASE_CONNECTION_URI = f"mysql://{user}:{password}@{host}/{database}"
SECRET_KEY = f"{secret_key}"
