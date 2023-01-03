# import pymysql
import mysql.connector


class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )

    # CODE TO CREATE A NEW DB
    @staticmethod
    def create_db():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
        )
        print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute("CREATE DATABASE LMS")

    # COMMAND TO CREATE TABLE IN CREATED DB

    @staticmethod
    def create_table():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )
        print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute(
            "CREATE TABLE BOOKS ( ID MEDIUMINT NOT NULL AUTO_INCREMENT ,BOOK_NAME VARCHAR(255), AUTHOR_NAME VARCHAR(255) , QUANTITY INTEGER(3),  PRIMARY KEY (ID))")

    # command to insert a table
    @staticmethod
    def insert_table():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")
        mycursor = mydb.cursor()

        sql = "INSERT INTO BOOKS ( BOOK_NAME,AUTHOR_NAME,QUANTITY) VALUES ( %s,%s, %s)"
        val = [
            ('Peter', 'Low street ', 4),
            ('Amy', 'Apple st ', 652),
            ('Hannah', 'Mountain ', 21),
            ('Michael', 'Valley ', 345),
            ('Sandy', 'Ocean blvd ', 2),
            ('Betty', 'Green Grass ', 1),
            ('Richard', 'Sky st ', 331),
            ('Susan', 'One way ', 98),
            ('Vicky', 'Yellow Garden ', 2),
            ('Ben', 'Park Lane ', 38),
            ('William', 'Central st ', 954),
            ('Chuck', 'Main Road ', 989),
            ('Viola', 'Sideways', 133)]
        mycursor.executemany(sql, val)

        print(mydb.commit())

        print(mycursor.rowcount, "was inserted.")

    @staticmethod
    def display_table(self):
        # mydb = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     password="Password@123",
        #     database="LMS"
        # )

        mycursor = self.mydb.cursor()

        mycursor.execute("SELECT * FROM BOOKS")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)


sbi = Database()
# sbi.create_table()
# # sbi.create_db()
# sbi.insert_table()
sbi.display_table()
