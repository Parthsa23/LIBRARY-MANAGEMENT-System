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
        user_input = "Y" #input("enter (Y) IF YOU WANT TO check the available books ELSE PRESS (ANY KEY) : ")
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
        user_input = "y"  # input("enter (Y) IF YOU WANT TO ISSUE BOOK ELSE PRESS (ANY KEY) : ")
        if user_input == "Y" or user_input == "y":
            # saving the personal details entered by user

            # ----------------------------------
            USER_NAME = "PARTH SARASWAT"  # input("Enter Your Name : ")
            USER_MOBILE = 7078440354  # int(input("Enter Your Mobile : "))
            USER_EMAIL = "SARASWATPARTH55@GMAIL.COM"  # input("Enter Your Email :  ")
            USER_ROLL_NO = 32  # int(input("Enter Your Roll Number  : "))
            USER_CLASS = 12  # int(input("Enter Your Class  : "))
            USER_SECTION = "C"  # input("Enter Your Section : ")
            print("detail filled in code only")
            # fetching current date to check the issue date for late payment check
            DATETIME = datetime.date.today()
            # -----------------
            self.display_book_table()
            # -----------------
            # printing the book details selected by user
            INPUT_BOOK_SNO = 1  # int(input("Enter the book S.no : "))
            self.mycursor.execute("SELECT * FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
            myresult = self.mycursor.fetchone()
            print(myresult)
            # -----------------
            # input of how much quantity user want to issue
            INPUT_BOOK_QUANTITY = 1  # int(input("Enter the book Quantity you want to issued : "))
            # ------------------------
            # fetching book name  from book table and storing it in a variable to post it in user table
            self.mycursor.execute("SELECT BOOK_NAME  FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
            string1 = self.mycursor.fetchone()
            for x in string1:
                print(x)

            # self.mycursor.fetchone()
            # print(type(string1))
            # mybookresult = (string1[0])  # ------------list
            # print(mybookresult)

            # print(string1)
            # -----------------------
            # fetching author name  from book table and storing it in a variable to post it in user table
            self.mycursor.execute("SELECT AUTHOR_NAME FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
            string2 = self.mycursor.fetchone()
            for y in string2:
                print(y)
            # self.mycursor.fetchone()
            # print(type(string2))
            # myauthorresult = (string2[0])  # ------------list
            # print(myauthorresult)
            # print(string2)
            # ----------------
            # self.mycursor.execute("SELECT  BOOK_NAME,AUTHOR_NAME FROM LMS.BOOKS WHERE ID = %s", (INPUT_BOOK_SNO,))
            # string3 = self.mycursor.fetchone()  #
            # print(string3)
            # string1 = string3[0]
            # string2 = string3[1]
            # print(string1)
            # print(type(string1))
            # string4 = list(string1)
            # print(string4)
            #
            # print(string2)
            # print(type(string2))
            # string5 = list(string2)
            # print(string5)
            # # print(string3)
            # inserting all the details entered by user above
            sql = "INSERT INTO USER ( USER_NAME,USER_MOBILE,USER_EMAIL," \
                  "USER_ROLL_NO,USER_CLASS,USER_SECTION,BOOK_NAME,AUTHOR_NAME,BOOK_QUANTITY,ISSUE_DATE) " \
                  "VALUES(%s, %d, %s, %d, %d, %s, %s, %s, %d, %s)"  # ------------------- str
            print(type(sql))
            val = [('USER_NAME', 'USER_MOBILE',
                    'USER_EMAIL', 'USER_ROLL_NO', 'USER_CLASS', 'USER_SECTION', 'x', 'y',
                    'INPUT_BOOK_QUANTITY', 'DATETIME')]  # ------------- list
            print(type(val))
            # c = self.mycursor.execute(sql, val)
            self.mycursor.execute(sql, val)

            # print(type(c))
            self.mydb.commit()
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
            USER_NAME = input("Enter Your Name : ")
            USER_EMAIL = input("Enter Your Email : ")
            # fetching details if user name entered by user matches user name in database
            self.mycursor.execute("SELECT * FROM USER WHERE USER_NAME =%s and USER_EMAIL=%s", (USER_NAME, USER_EMAIL,))
            myresult = self.mycursor.fetchall()
            for x in myresult:
                print(x)
            # selecting the user table id  if there are 2 transaction by user
            ret_book_id = int(input("Enter the Book ID you want to return :  "))
            # fetching current date to check the return date for late payment check
            DATETIME = datetime.date.today()
            status = "DONE"
            # updating the return date in user table
            sql = "UPDATE USER SET RETURN_DATE = %s WHERE ID = %s and USER_NAME= %s,USER_EMAIL= %s "
            val = (DATETIME, ret_book_id, USER_NAME, USER_EMAIL)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record(s) for return date updated")
            # updating the STATUS  in user table
            sql = "UPDATE USER SET STATUS = %s WHERE ID = %s"
            val = (status, ret_book_id)
            self.mycursor.execute(sql, val)
            self.mydb.commit()
            print(self.mycursor.rowcount, "record(s) for for book status updated")

            # this part is pending from line 132 to 141
            # a = self.mycursor.execute(
            #     "SELECT USER.BOOK_QUANTITY FROM USER INNER JOIN BOOKS ON BOOKS.BOOK_NAME=USER.BOOK_NAME")
            # myresult = self.mycursor.fetchall()
            # for x in myresult:
            #     print(x)
            # sql = "UPDATE BOOKS SET QUANTITY = QUANTITY + %s  WHERE ID = %s"
            # val = (a, ret_book_id)
            # self.mycursor.execute(sql, val)
            # self.mydb.commit()
            # print(self.mycursor.rowcount, "record(s) affected")

        else:
            print("Thanks")
        self.menu()

    def Penalty(self):
        pass
        # fetching some details and filling them in new table  late self.mycursor.execute( "SELECT USER_NAME ,
        # BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,STATUS,DATEDIFF(RETURN_DATE,ISSUE_DATE) " "AS date_difference
        # FROM " "USER") myresult = self.mycursor.fetchall() for x in myresult: print(x) sql = "INSERT INTO LATE
        # USER_NAME ,BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,date_difference  VALUES (?," \ "?,?, ?,?,?)",
        # val = [("SELECT USER_NAME ,BOOK_NAME,AUTHOR_NAME, ISSUE_DATE,RETURN_DATE,DATEDIFF(RETURN_DATE,ISSUE_DATE)
        # AS " "date_difference FROM USER")] self.mycursor.execute(sql, val) self.mydb.commit() print("table late pay
        # updated ")
        #
        # # if Penalty > 7:
        # #     print("OOPS..! Late Payment")
        # # else:
        # #     print("Good you return on time")


sbi = User()
sbi.menu()
