import socket

from peewee import *
from playhouse.mysql_ext import MySQLConnectorDatabase
import sqlite3
import _mysql_connector
import pymysql.cursors
from server import carros


# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.
DB_IP = "127.0.0.1"
DB_PORT = 1234
DB_HOST = "localhost"
DB_USER = "root"
DB_PASSWORD = "root"
DB_NAME = "a"

db = MySQLDatabase(
    host= DB_HOST,
    user= DB_USER,
    password= DB_PASSWORD,
    database= DB_NAME)

db.connect()

if db.is_connection_usable() == True:
    print(f'Connected to database "{DB_NAME}"')
    carros()

else:
	print("Im Sorry, Something when wrong, try it next time")