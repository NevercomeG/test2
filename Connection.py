import threading
from peewee import Metadata

import os

from peewee import *
from playhouse.db_url import connect

# Connect to the database URL defined in the environment, falling
# back to a local Sqlite database if no database URL is specified.
db = connect(os.environ.get('DATABASE') or 'sqlite:///default.db')

class BaseModel(Model):
    class Meta:
        database = db


class ThreadSafeDatabaseMetadata(Metadata):
    def __init__(self, *args, **kwargs):
        # database attribute is stored in a thread-local.
        self._local = threading.local()
        super(ThreadSafeDatabaseMetadata, self).__init__(*args, **kwargs)

    def _get_db(self):
        return getattr(self._local, 'database', self._database)
    def _set_db(self, db):
        self._local.database = self._database = db
    database = property(_get_db, _set_db)


class BaseModel(Model):
    class Meta:
        # Instruct peewee to use our thread-safe metadata implementation.
        model_metadata_class = ThreadSafeDatabaseMetadata