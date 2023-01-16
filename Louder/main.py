import louder as ld
import db_connect


# This class performs initialisations loads
def load_run():
    print('Begin load data')
    ld.Loader.check_conn()    # Future klass and method, who performs load
    ld.Loader.createTab()
    ld.Loader.insertData()
    ld.Loader.closeConn()
    print('Load end')


if __name__ == "__main__":
    load_run()


