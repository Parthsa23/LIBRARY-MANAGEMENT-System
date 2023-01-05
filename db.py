# import pymysql
import mysql.connector


class Database:

    def __init__(self):
        #     self.mydb = mysql.connector.connect(
        #         host="localhost",
        #         user="root",
        #         password="Password@123",
        #         database="LMS"
        #     )
        self.menu()

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Create Database
                        2. Enter 2 to Create Table BOOK
                        3. Enter 3 to Create Table USER
                        4. Enter 3 to Insert Entries
                        5. Enter 4 to Display Table 
                        6. Enter 5 to Exit 
        ''')
        # print(user_input)
        if user_input == "1":
            self.create_db()
        elif user_input == "2":
            self.create_table_book()
        elif user_input == "3":
            self.create_table_user()
        elif user_input == "4":
            self.insert_data()
        elif user_input == "5":
            self.display_table()
        else:
            self.menu()
            # print("BYe")

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
        print('Database Created Successfully')

    # creating table for books

    @staticmethod
    def create_table_book():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )
        print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute(
            "CREATE TABLE BOOKS ( ID MEDIUMINT NOT NULL AUTO_INCREMENT ,BOOK_NAME VARCHAR(255), AUTHOR_NAME VARCHAR("
            "255) , QUANTITY INTEGER(3),  PRIMARY KEY (ID))")
        print("Table Created Successfully")

    # Creating table User
    @staticmethod
    def create_table_user():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )
        print(mydb)

        mycursor = mydb.cursor()

        mycursor.execute(
            'CREATE TABLE USER ( ID INT NOT NULL AUTO_INCREMENT ,USER_NAME VARCHAR(255) NULL, USER_MOBILE BIGINT  NULL,'
            'USER_EMAIL VARCHAR(255) NULL, USER_ROLL_NO INT NULL, USER_CLASS INT NULL,USER_SECTION CHAR(2)  NULL, '
            'BOOK_NAME VARCHAR(255)NULL ,AUTHOR_NAME VARCHAR(255)NULL ,BOOK_QUANTITY INT, ISSUE_DATE DATE  '
            ' NULL,'
            'RETURN_DATE DATE NULL,PRIMARY KEY(ID))')
        print("Table Created Successfully")

    # command to insert a table
    @staticmethod
    def insert_data():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")
        mycursor = mydb.cursor()
        sql = "INSERT INTO BOOKS ( BOOK_NAME,AUTHOR_NAME,QUANTITY) \
              VALUES ( ?,?,?)",
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
            ('Viola', 'Sideways', 133)
        ]
        mycursor.executemany(sql, val)

        print(mydb.commit())

        print(mycursor, " entries are inserted.")

    @staticmethod
    def display_table():
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )

        mycursor = mydb.cursor()

        mycursor.execute("SELECT * FROM BOOKS")

        myresult = mycursor.fetchall()

        for x in myresult:
            print(x)


sbi = Database()
sbi.menu()
# sbi.create_table()
# sbi.create_db()
# sbi.insert_data()
# sbi.display_table()
