import psycopg2
import mysql.connector
from ConfigConn.config import configPg, configMysqp


def get_conn_postgres():
    params = configPg()
    conn = psycopg2.connect(**params)
    cur = conn.cursor()
    return cur, conn


def get_conn_mysql():
    params = configMysqp()
    conn = mysql.connector.connect(params)
    cur = conn.cursor()
    return cur, conn
