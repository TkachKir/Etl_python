sqlCheck = """SELECT VERSION()"""

sqlForFaker = """INSERT INTO public.people (first_name, last_name, email, zipcode, city, birthdate, flag)
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s');"""

sqlForFakerCreate = """CREATE TABLE IF NOT EXISTS public.people (
                        pk serial4 NOT NULL,
                        uniid uuid NOT NULL DEFAULT uuid_generate_v4(),
                        first_name varchar(25) NOT NULL,
                        last_name varchar(25) NOT NULL,
                        email varchar(50) NOT NULL,
                        zipcode int NOT NULL,
                        city varchar(25) NOT NULL,
                        birthdate date NULL,
                        flag int NOT NULL,
                        create_dat timestamp NOT NULL DEFAULT now(),
                        activ bool NULL
                        );"""

sqlCreateMysqlTab = """CREATE TABLE IF NOT EXISTS fo_test.people (
                        pk int NOT NULL,
                        uniid char(255) NOT NULL,
                        first_name varchar(25) NOT NULL,
                        last_name varchar(25) NOT NULL,
                        email varchar(50) NOT NULL,
                        zipcode int NOT NULL,
                        city varchar(25) NOT NULL,
                        birthdate date NULL,
                        flag int NOT NULL,
                        create_dat timestamp NOT NULL DEFAULT now(),
                        activ char(25) NULL);"""

sqlInsertToMysql = """INSERT INTO fo_test.people (pk, uniid, first_name, last_name, email, zipcode, city, birthdate, flag, create_dat, activ)
                    VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s','%s','%s','%s','%s');"""

sqlSelectFromPg = """SELECT pk, uniid, first_name, last_name, email, zipcode, city, birthdate, flag, create_dat, activ
                       FROM public.people;"""

sqlTruncMysql = """TRUNCATE table fo_test.people;"""


# commands = (
#         """
#         CREATE TABLE IF NOT EXISTS toporders(
#             customername VARCHAR(255),
#             number_of_orders INTEGER
#         )
#         """,
#         """ CREATE TABLE IF NOT EXISTS product_demand(
#                 productName VARCHAR(255),
#                 quantity_ordered INTEGER
#                 )
#         """,
#         """
#         CREATE TABLE IF NOT EXISTS customer_spending(
#             customername VARCHAR(255),
#             total_amount_spent float8
#         )
#         """,
#         """
#         TRUNCATE TABLE toporders, product_demand, customer_spending;
#         """
#         )
#
# query1 = "SELECT productName , SUM(quantityOrdered) AS quantity_ordered\
#            FROM  products, orderdetails\
#            WHERE products.productCode = orderdetails.productCode\
#            GROUP BY productName\
#            ORDER BY quantity_ordered DESC\
#            LIMIT 20;"
#
# # toporders- customers that have the most orders
# query2 = "SELECT contactFirstName, contactLastName , COUNT(*) AS number_of_orders\
#        FROM  customers, orders\
#        WHERE customers.customerNumber = orders.customerNumber\
#        GROUP BY customerName\
#        ORDER BY number_of_orders DESC\
#        LIMIT 20;"
# # customer spending- ustomers that have spent more
# query3 = "SELECT contactFirstName , contactLastName, SUM(quantityOrdered*priceEach) AS total_amount_spent\
#        FROM  customers, orders, orderdetails\
#        WHERE customers.customerNumber = orders.customerNumber AND orderdetails.orderNumber= orders.orderNumber\
#        GROUP BY customerName\
#        ORDER BY total_amount_spent DESC\
#        LIMIT 10;"
