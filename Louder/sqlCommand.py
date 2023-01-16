
sqlCheck = """SELECT VERSION()"""

sqlCreated = ("""CREATE TABLE IF NOT EXISTS public.user(
                name varchar(50),
                sure_name varchar(50),
                age int);""")

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
