import psycopg2
import mysql.connector


def get_conn_postgres():
    conn = psycopg2.connect(host="localhost", port=5432, user="postgres", password="postgres", database="mytestdb")
    cur = conn.cursor()
    return cur, conn


def get_conn_mysql():
    conn = mysql.connector.connect()
    cur = conn.cursor()
    return cur, conn
