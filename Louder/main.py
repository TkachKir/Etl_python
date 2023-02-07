import louder as ld
import db_connect
import psycopg2

# This class performs initialisations loads
def load_run():
    print('Begin load data')
    ld.check_conn()
    ld.load_data()
    print('Load end')


if __name__ == "__main__":
    load_run()


