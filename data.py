import pymysql
from tabulate import tabulate

dbServerName = "localhost"
dbUser = "root"
dbPassword = "root123"
dbName = "german"
connection = pymysql.connect(host=dbServerName, user=dbUser, password=dbPassword, db=dbName)
cursor = connection.cursor()

def insert_(msg1, msg2):
    sql = ("""INSERT INTO german.zuklien (patterns, responses) VALUES (%s, %s)""")
    ne = (msg1, msg2)
    cursor.execute(sql, ne)
    connection.commit()


def show_data():
    qu = "SELECT * FROM german.zuklien "
    cursor.execute(qu)
    rows = cursor.fetchall()
    print(tabulate(rows, headers=['patterns', 'responses'], tablefmt='psql'))

def delete__(msg):
    qu = """DELETE FROM `german`.`zuklien` WHERE (patterns=%s);"""
    #qe = "delete from bot where pattern={}".format(msg)
    cursor.execute(qu, msg)
    print("delet")
    connection.commit()

