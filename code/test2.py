#script python insert mysql 
import mysql.connector
from mysql.connector import Error

try:
    connection = mysql.connector.connect(host='ubuntu221',
                                         database='test',
                                         user='root',
                                         password='mysql')
    if connection.is_connected():
        db_Info = connection.get_server_info()
        print("==Connected to MySQL Server version ", db_Info)
        cursor = connection.cursor()
        cursor.execute("select database();")
        record = cursor.fetchone()
        print("==You're connected to database: ", record)
    mySql_insert_query = """INSERT INTO tlog (mess) VALUES ('test log python') """
    cursor = connection.cursor()
    cursor.execute(mySql_insert_query)
    connection.commit()
    print("==Record inserted successfully into log table:",cursor.rowcount)
    cursor.close()
except Error as e:
    print("==Error while connecting to MySQL", e)
finally:
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("==MySQL connection is closed")