"""Загрузка фейковых даных"""
import random as rm
from faker import Faker
from Louder import db_connect as dbC
from Louder import sqlCommand as sql


curPg, connPG = dbC.get_conn_postgres()
Faker.seed()
fake = Faker()
rowNumMin = 0
rowNumMax = 10
row = {}


if connPG.status == 1:
    print('Connected complete for PG')
    print('Create table if not excepts')
    curPg.execute(sql.sqlForFakerCreate)
    print('Start load')
    while rowNumMin < rowNumMax:
        try:
            rm_num = rm.randint(0, 1)
            row = [fake.first_name(), fake.last_name(), fake.email(),
                   fake.postcode(), fake.city(), fake.date_of_birth()]
            curPg.execute(sql.sqlForFaker % (row[0], row[1], row[2], row[3], row[4], row[5], rm_num))
            connPG.commit()
            rowNumMin += 1

        except Exception:
            print('Error load on row insert:\n' + sql.sqlForFaker % (row[0], row[1], row[2], row[3], row[4], row[5], rm_num))
    print('Row load - ' + str(rowNumMin))
else:
    print('Connection filed to target DB!')

curPg.close()
connPG.close()










# create_table_sql = """
# CREATE TABLE `people` (
#   `id` int(11) NOT NULL AUTO_INCREMENT,
#   `first_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
#   `last_name` varchar(50) COLLATE utf8_unicode_ci NOT NULL,
#   `email` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
#   `zipcode` int(5) NOT NULL,
#   `city` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
#   `country` varchar(100) COLLATE utf8_unicode_ci NOT NULL,
#   `birthdate` date NOT NULL,
#   `added` timestamp NOT NULL DEFAULT current_timestamp(),
#   PRIMARY KEY (`id`),
#   UNIQUE KEY (`id`)
# ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;
# """
#
# db_host = os.environ.get('DB_HOST', 'localhost')
# db_name = os.environ.get('DB_NAME')
# db_user = os.environ.get('DB_USER_NAME')
# db_pass = os.environ.get('DB_USER_PASSWORD')
#
# try:
#     conn = mysql.connector.connect(host=db_host, database = db_name,
#                                    user=db_user, password=db_pass)
#
#     if conn.is_connected():
#         cursor = conn.cursor()
#
#         try:
#             cursor.execute(create_table_sql)
#             print("Table created")
#         except Exception as e:
#             print("Error creating table", e)
#         row = {}
#         n = 0
#
#         while True:
#             n += 1
#             row = [fake.first_name(), fake.last_name(), fake.email(), \
#                fake.postcode(), fake.city(), fake.country(), fake.date_of_birth()]
#
#            cursor.execute(' \
#                INSERT INTO `people` (first_name, last_name, email, zipcode, city, country, birthdate) \
#                VALUES ("%s", "%s", "%s", %s, "%s", "%s", "%s"); \
#                ' % (row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
#
#             if n % 100 == 0:
#                 print("iteration %s" % n)
#                 time.sleep(0.5)
#                 conn.commit()
# except Error as e :
#     print ("error", e)
#     pass
# except Exception as e:
#     print ("Unknown error %s", e)
# finally:
#     #closing database connection.
#     if(conn and conn.is_connected()):
#         conn.commit()
#         cursor.close()
#         conn.close()
