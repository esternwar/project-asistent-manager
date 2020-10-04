import psycopg2
from app.constants import dbname, user, password, host, port


def bd_connect():
    conn = psycopg2.connect(dbname=dbname, user=user,
                            password=password, host=host, port=port)
    return conn


def close_connect_cursor(conn, cur=None):
    if cur:
        cur.close()
    if conn:
        conn.close()

