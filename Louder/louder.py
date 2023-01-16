import sqlCommand as sqlC
import db_connect as dbC

curPg, connPG = dbC.get_conn_postgres()


# curMs, connMs = dbC.get_conn_mysql()


class Loader:

    def check_conn():
        curPg.execute(sqlC.sqlCheck)
        resultConnection = curPg.fetchone()
        print('Connected to ' + str(resultConnection))
        # connPG.close()

    def createTab():
        curPg.execute(sqlC.sqlCreated)
        connPG.commit()
        print('Creste table')

    def insertData():
        print('Insert data')

    def closeConn():
        connPG.close()
        print("Connect close")


