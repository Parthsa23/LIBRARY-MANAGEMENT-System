import mysql.connector
import datetime


# import Lib


class User:
    def __init__(self):

        self.display = None
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")
        self.mycursor = self.mydb.cursor()
        self.USER_NAME = "PARTH "  # input("Enter Your Name : ")
        self.USER_MOBILE = 7078440354  # int(input("Enter Your Mobile : "))
        self.USER_EMAIL = "SARASWATPARTH55@GMAIL.COM"  # input("Enter Your Email :  ")
        self.USER_ROLL_NO = 12  # int(input("Enter Your Roll Number  : "))
        self.USER_CLASS = 12  # int(input("Enter Your Class  : "))
        self.USER_SECTION = "C"  # input("Enter Your Section : ")

        # self.USER_NAME = input("Enter Your Name : ")
        # self.USER_MOBILE = int(input("Enter Your Mobile : "))
        # self.USER_EMAIL = input("Enter Your Email :  ")
        # self.USER_ROLL_NO = int(input("Enter Your Roll Number  : "))
        # self.USER_CLASS = int(input("Enter Your Class  : "))
        # self.USER_SECTION = input("Enter Your Section : ")

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Display  Table Data
                        2. Enter 2 to Issue Book
                        3. Enter 3 to Return Book
                        5. Enter 5 to Exit .  
        ''')
        if user_input == "1":
            self.display_book_table()
        elif user_input == "2":
            self.Issue()
        elif user_input == "3":
            self.Return()
        # elif user_input == "4":
        #     self.Penalty()
        else:
            self.menu()

    def display_book_table(self):
        user_input = input("enter (Y) IF YOU WANT TO check the available books ELSE PRESS (ANY KEY) : ")
        if user_input == "Y" or user_input == "y":
            # printing the book table
            self.mycursor.execute("SELECT * FROM BOOKS")
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)
        else:
            print("Thanks .....!!!!!!!!!")
        # self.menu()

    def Issue(self):
        user_input = input("enter (Y) IF YOU WANT TO ISSUE BOOK ELSE PRESS (ANY KEY) : ")
        if user_input == "Y" or user_input == "y":
            # saving the personal details entered by user

            # ----------------------------------
            # fetching current date to check the issue date for late payment check
            DATETIME = datetime.date.today()
            # -----------------
            self.display_book_table()
            # -----------------
            # printing the book details selected by user
            INPUT_BOOK_SNO = int(input("Enter the book S.no : "))
            self.mycursor.execute("SELECT * FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
            myresult = self.mycursor.fetchall()
            print(myresult)
            # -----------------
            # input of how much quantity user want to issue
            INPUT_BOOK_QUANTITY = int(input("Enter the book Quantity you want to issued : "))
            # ------------------------

            # # -----------------------
            # etching  book name and author name  from book table and storing it in a variable to post it in user table
            self.mycursor.execute("SELECT ID , BOOK_NAME,AUTHOR_NAME FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
            string2 = list(self.mycursor.fetchall())
            # print(string2)
            # print(type(string2))
            for y in string2:
                print(y)
            string3 = y[0]
            print(string3)
            string4 = y[1]
            print(string4)
            string5 = y[2]
            print(string5)

            sql = "INSERT INTO USER ( USER_NAME,USER_MOBILE,USER_EMAIL,USER_ROLL_NO,USER_CLASS,USER_SECTION," \
                  "BOOK_ID,BOOK_NAME,AUTHOR_NAME,BOOK_QUANTITY,ISSUE_DATE) VALUES(%s, %s, %s, %s, %s, %s, " \
                  " %s,%s, %s,%s, %s)"  # ------------------- str
            val = (self.USER_NAME, self.USER_MOBILE,
                   self.USER_EMAIL, self.USER_ROLL_NO, self.USER_CLASS, self.USER_SECTION,
                   string3, string4, string5, INPUT_BOOK_QUANTITY, DATETIME)  # ------------- list
            self.mycursor.execute(sql, val)
            print(self.mycursor.rowcount, " entry were inserted.")
            # -----------------
            # updating the quantity in book table to maintain the stock by subtracting
            sql = "UPDATE BOOKS SET QUANTITY = QUANTITY - %s  WHERE ID = %s"
            val = (INPUT_BOOK_QUANTITY, INPUT_BOOK_SNO)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record(s) affected")
            # -----------------
            print("congrats the book issued kindly return within 7 days")
        else:
            print("Thanks.  !!!!!!!!!!!")
        self.menu()

    def Return(self):
        user_input = input("enter (Y) IF YOU WANT TO return BOOK ELSE PRESS (ANY KEY) : ")
        if user_input == "Y" or user_input == "y":
            # fetching details if user name entered by user matches user name in database
            self.mycursor.execute(
                "SELECT * FROM USER WHERE USER_NAME = %s and USER_EMAIL=%s and IS_RETURNED = 'PENDING'",
                (self.USER_NAME, self.USER_EMAIL,))
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)
            # selecting the user table id  if there are 2 transaction by user
            user_book_id = int(input("Enter the Book ID you want to return :  "))
            # fetching current date to check the return date for late payment check
            DATETIME = datetime.date.today()
            status = "DONE"
            # updating the return date  and status in user table
            sql = "UPDATE USER SET RETURN_DATE = %s,IS_RETURNED=%s WHERE ID = %s and USER_NAME= %s and USER_EMAIL= %s "
            val = (DATETIME, status, user_book_id, self.USER_NAME, self.USER_EMAIL)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record(s) for return date  and return status updated")
            # fetching the quantity   which matching the above provided details
            self.mycursor.execute(
                "SELECT USER.BOOK_QUANTITY FROM USER INNER JOIN BOOKS ON  USER.ID = %s and USER.USER_NAME = %s and "
                "USER.USER_EMAIL=%s"
                "and BOOKS.ID=USER.BOOK_ID",
                (user_book_id, self.USER_NAME, self.USER_EMAIL,))
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)
            string8 = x[0]

            # APPLYING CROSS TABLE UPDATE

            # updating the quantity in book table to maintain the stock by subtracting
            sql = "UPDATE BOOKS  INNER JOIN  USER  ON BOOKS.ID = USER.BOOK_ID SET BOOKS.QUANTITY = BOOKS.QUANTITY+ %s  "
            val = [string8, ]
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "quantity/stock of book increased as the book is now returned")
        else:
            print("Thanks")
        # self.menu()
    # ISSUE IS EK BOOK RETURN KAR RAHE H TOH DOOSRE KA BI SOTKC UTTA HI UPDATE HO RHA H
    def Penalty(self):
        # pass
        # fetching some details and filling them in new table  late
        self.mycursor.execute(
            'SELECT USER_NAME ,BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,STATUS,DATEDIFF(RETURN_DATE,ISSUE_DATE) '
            'AS date_difference FROM  USER')
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
        sql = "INSERT INTO LATE (USER_NAME ,BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,date_difference ) VALUES (" \
              "?,?,?, ?,?,?)",
        val = [
            "SELECT USER_NAME ,BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,DATEDIFF(RETURN_DATE,ISSUE_DATE AS " "date_difference FROM USER"]
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print("table late pay updated ")

        # # if Penalty > 7:
        # #     print("OOPS..! Late Payment")
        # # else:
        # #     print("Good you return on time")


sbi = User()
sbi.menu()
