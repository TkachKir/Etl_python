import sqlCommand as sqlC
import db_connect as dbC
import datetime
import pandas as pd

curPg, connPG = dbC.get_conn_postgres()
curMs, connMs = dbC.get_conn_mysql()


def check_conn():
    curPg.execute(sqlC.sqlCheck)
    resultConnectionPG = curPg.fetchone()
    print('Connected to ' + str(resultConnectionPG))
    curMs.execute(sqlC.sqlCheck)
    resultConnectionMS = curMs.fetchone()
    print('Connected to ' + str(resultConnectionMS))


def load_data():
    curMs.execute(sqlC.sqlCreateMysqlTab)
    curMs.execute(sqlC.sqlTruncMysql)
    curPg.execute(sqlC.sqlSelectFromPg)
    while True:
        pg_result = curPg.fetchone()
        if pg_result:
            df = pd.DataFrame([pg_result])
            df.reset_index(drop=True, inplace=True)
            df[10] = df[10]. fillna('')
            #print(sqlC.sqlInsertToMysql % (df[0][0], df[1][0], df[2][0], df[3][0], df[4][0], df[5][0], df[6][0], df[7][0], df[8][0], df[9][0], df[10][0]))
            curMs.execute(sqlC.sqlInsertToMysql % (df[0][0], df[1][0], df[2][0], df[3][0], df[4][0], df[5][0], df[6][0], df[7][0], df[8][0], df[9][0], df[10][0]))
        else:
            connMs.commit()
            connPG.close()
            connMs.close()
            return print('Download done!')



