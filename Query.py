import requests
import hashlib
import datetime
from connection import connection
import flask
database = connection()

def Creating_new_user(database):
    try:
        with database.atomic():
            # Attempt to create the user. If the username is taken, due to the
            # unique constraint, the database will raise an IntegrityError.
            user = flask.User.create(
                username=requests.form['username'],
                password=hashlib.md5(requests.form['password']).hexdigest(),
                email=requests.form['email'],
                join_date=datetime.datetime.now())

        # mark the user as being 'authenticated' by setting the session vars
        flask.auth_user(user)
        return flask.redirect('homepage')

    except flask.IntegrityError:
        flask('That username is already taken')