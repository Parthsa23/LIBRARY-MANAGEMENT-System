import mysql.connector


class Database:

    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS"
        )
        self.mycursor = self.mydb.cursor()
        self.menu()

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Create Database
                        2. Enter 2 to Create Table BOOK
                        3. Enter 3 to Create Table USER                        
                        4. Enter 4 to Insert Entries
                        5. Enter 5 to Display Table 
                        6. Enter 6 to Exit 
                        7. ENTER 7 TO CREATE TABLE LATE PAY
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
        elif user_input == "7":
            self.create_table_late()
        else:
            self.menu()
            # print("BYe")

    # CODE TO CREATE A NEW DB

    def create_db(self):
        self.mycursor.execute("CREATE DATABASE LMS")
        print('Database Created Successfully')

    # creating table for books

    def create_table_book(self):
        self.mycursor.execute(
            "CREATE TABLE BOOKS ( ID MEDIUMINT NOT NULL AUTO_INCREMENT ,BOOK_NAME VARCHAR(255), AUTHOR_NAME VARCHAR("
            "255) , QUANTITY INTEGER(3),  PRIMARY KEY (ID))")
        print("Table Created Successfully")

    # Creating table User

    def create_table_user(self):
        self.mycursor.execute(
            "CREATE TABLE `USERS` (`ID` INT NOT NULL AUTO_INCREMENT,`USER_NAME` VARCHAR(255) NULL,`USER_MOBILE` INT "
            "NULL,"
            "`USER_EMAIL` VARCHAR(255) NULL,`USER_ROLL_NO` INT NULL,`USER_CLASS` INT NULL,`"
            "USER_SECTION` VARCHAR(45) NULL,BOOK_ID INT NULL,`BOOK_NAME` VARCHAR(255) NULL,`AUTHOR_NAME` VARCHAR(255) "
            "NULL,"
            "`BOOK_QUANTITY` INT NULL,`ISSUE_DATE` DATE NULL,`RETURN_DATE` DATE NULL DEFAULT NULL,"
            "`IS_RETURNED` VARCHAR(45) NULL DEFAULT 'PENDING', PRIMARY KEY(`ID`));")
        print("Table Created Successfully")

        # command to insert a table

    def create_table_late(self):

        self.mycursor.execute(
            "CREATE TABLE LATE (`ID` INT NOT NULL AUTO_INCREMENT,`USER_NAME` VARCHAR(45) NULL DEFAULT NULL,"
            "`BOOK_NAME` VARCHAR(45) NULL DEFAULT NULL,`AUTHOR_NAME` VARCHAR(45) NULL DEFAULT NULL,"
            "`ISSUE_DATE` DATE NULL DEFAULT NULL,`RETURN_DATE` DATE NULL DEFAULT NULL,"
            "`date_difference` VARCHAR(45) NULL,PRIMARY KEY (ID))")
        print("Table Created Successfully")
    def insert_data(self):
        sql = "INSERT INTO BOOKS ( BOOK_NAME,AUTHOR_NAME,QUANTITY) VALUES ( ?,?,?)",
        val = [('Dummy', 'Dummy Data ', 1)]
        self.mycursor.executemany(sql, val)
        print(self.mydb.commit())
        print(self.mycursor, " entries are inserted.")

    def display_table(self):
        self.mycursor.execute("SELECT * FROM BOOKS")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)


sbi = Database()
sbi.menu()
