import sqlite3


def get_connection():

    return sqlite3.connect("calls.db")

conn = get_connection()
