from storage.db import get_connection


class BaseRepository:

    def get_connection(self):
        return get_connection()