from peewee import *
from server import carros


# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.
DB_IP = "127.0.0.1"
DB_PORT = 1234
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "nasdaq_db"


db = MySQLDatabase(
        host= DB_HOST,
        user= DB_USER,
        password= DB_PASSWORD,
        database= DB_NAME)

def connection():
        db.connect()
        return (db)   

print(f'Connected to database "{DB_NAME}"')
carros()