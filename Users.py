import mysql.connector
import datetime


class User:
    def __init__(self):
        self.display = None
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")
        self.mycursor = self.mydb.cursor()
        self.USER_NAME = input("Enter Your Name : ")
        self.USER_MOBILE = int(input("Enter Your Mobile : "))
        self.USER_EMAIL = input("Enter Your Email :  ")
        self.USER_ROLL_NO = int(input("Enter Your Roll Number  : "))
        self.USER_CLASS = int(input("Enter Your Class  : "))
        self.USER_SECTION = input("Enter Your Section : ")

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Display  Table Data
                        2. Enter 2 to Issue Book
                        3. Enter 3 to Return Book
                        4. Enter 4 to Check Penalty
                        5. Enter 5 to Exit .  
        ''')
        if user_input == "1":
            self.display_book_table()
        elif user_input == "2":
            self.Issue()
        elif user_input == "3":
            self.Return()
        elif user_input == "4":
            self.Penalty()
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
            # fetching current date to check the issue date for late payment check
            DATETIME = datetime.date.today()
            self.display_book_table()
            # printing the book details selected by user
            INPUT_BOOK_SNO = int(input("Enter the book S.no : "))
            try:
                self.mycursor.execute("SELECT * FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
                myresult = self.mycursor.fetchall()
                print(myresult)
            except Exception as e:
                print(e)
            # input of how much quantity user want to issue
            INPUT_BOOK_QUANTITY = int(input("Enter the book Quantity you want to issued : "))
            # fetching  book name and author name  from book table and storing it in a variable to post it in user table
            try:
                self.mycursor.execute("SELECT ID , BOOK_NAME,AUTHOR_NAME FROM BOOKS WHERE ID =%s", (INPUT_BOOK_SNO,))
                string2 = list(self.mycursor.fetchall())
                for y in string2:
                    print(y)
                string3 = y[0]
                print(string3)
                string4 = y[1]
                print(string4)
                string5 = y[2]
                print(string5)
            except Exception as e:
                print(e)
            try:
                sql = "INSERT INTO USER ( USER_NAME,USER_MOBILE,USER_EMAIL,USER_ROLL_NO,USER_CLASS,USER_SECTION," \
                      "BOOK_ID,BOOK_NAME,AUTHOR_NAME,BOOK_QUANTITY,ISSUE_DATE) VALUES(%s, %s, %s, %s, %s, %s, " \
                      " %s,%s, %s,%s, %s)"
                val = (self.USER_NAME, self.USER_MOBILE,
                       self.USER_EMAIL, self.USER_ROLL_NO, self.USER_CLASS, self.USER_SECTION,
                       string3, string4, string5, INPUT_BOOK_QUANTITY, DATETIME)
                self.mycursor.execute(sql, val)
                print(self.mycursor.rowcount, " entry were inserted.")
            except Exception as e:
                print(e)
            # updating the quantity in book table to maintain the stock by subtracting
            try:
                sql = "UPDATE BOOKS SET QUANTITY = QUANTITY - %s  WHERE ID = %s"
                val = (INPUT_BOOK_QUANTITY, INPUT_BOOK_SNO)
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "record(s) affected")
            except Exception as e:
                print(e)
            # -----------------
            print("congrats the book issued kindly return within 7 days")
        else:
            print("Thanks.  !!!!!!!!!!!")
        self.menu()
    def Return(self):
        user_input = input("enter (Y) IF YOU WANT TO return BOOK ELSE PRESS (ANY KEY) : ")
        if user_input == "Y" or user_input == "y":
            # fetching details if user name entered by user matches user name in database
            try:
                self.mycursor.execute(
                    "SELECT * FROM USER WHERE USER_NAME = %s and USER_EMAIL=%s and IS_RETURNED = 'PENDING'",
                    (self.USER_NAME, self.USER_EMAIL,))
                myresult = self.mycursor.fetchall()
                for x in myresult:
                    print(x)
            except Exception as e:
                print(e)
            # selecting the user table id  if there are 2 transaction by user
            user_trans_id = int(input("Enter the Book ID you want to return :  "))
            # fetching current date to check the return date for late payment check
            DATETIME = datetime.date.today()
            status = "DONE"
            # updating the return date  and status in user table
            try:
                sql = "UPDATE USER SET RETURN_DATE = %s,IS_RETURNED=%s WHERE ID = %s and USER_NAME= %s and " \
                      "USER_EMAIL= %s"
                val = (DATETIME, status, user_trans_id, self.USER_NAME, self.USER_EMAIL)
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "record(s) for return date  and return status updated")
            except Exception as e:
                print(e)
                # fetching the quantity   which matching the above provided details AND COMPARING WITH ABOVE
                # PROVIDED USER  UNIQUE ID ,NAME,EMAIL  COMPARING BOTH  THE TABLE AS WELL
            try:
                self.mycursor.execute(
                    "SELECT USER.BOOK_QUANTITY   FROM USER INNER JOIN BOOKS ON USER.USER_NAME = %s and "
                    "USER.USER_EMAIL=%s and BOOKS.ID=USER.BOOK_ID and USER.BOOK_NAME=BOOKS.BOOK_NAME and "
                    "USER.AUTHOR_NAME=BOOKS.AUTHOR_NAME and USER.ID=%s",
                    (self.USER_NAME, self.USER_EMAIL, user_trans_id))
                myresult = self.mycursor.fetchall()
                for x in myresult:
                    print(x)

                string8 = x[0]
            except Exception as e:
                print("there is some error in code  kindly check before you go")
                print(e)
                # APPLYING CROSS TABLE UPDATE
                # updating the quantity in book table to maintain the stock by ADDING
            try:
                sql = "UPDATE BOOKS  INNER JOIN  USER  ON BOOKS.ID = USER.BOOK_ID  AND USER.ID = %s " \
                      " SET BOOKS.QUANTITY = BOOKS.QUANTITY+ %s"
                val = [user_trans_id, string8]
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, "quantity/stock of book increased as the book is now returned")
            except Exception as e:
                print("there is some error in code  kindly check before you go")
                print(e)
            # fetching the details from user table  and storing it in a variable
            try:
                self.mycursor.execute(
                    "SELECT ID,USER_NAME, BOOK_NAME, AUTHOR_NAME, ISSUE_DATE, RETURN_DATE, DATEDIFF(RETURN_DATE, "
                    "ISSUE_DATE)AS date_difference FROM USER WHERE IS_RETURNED = 'DONE' and ID=%s", (user_trans_id,))
                myresult = self.mycursor.fetchall()
                for str9 in myresult:
                    print(str9)
                # INSERTING THE DETAILS IN LATE TABLE BY FETCHING IT FROM ANOTHER
                sql = "Insert into LATE(USER_ID,USER_NAME, BOOK_NAME, AUTHOR_NAME, ISSUE_DATE, RETURN_DATE, " \
                      "date_difference)VALUES(%s, %s, %s, %s, %s, %s,%s)"
                val = str9
                self.mycursor.execute(sql, val)
                self.mydb.commit()
                print(self.mycursor.rowcount, " entry were inserted.")
            except Exception as e:
                print("there is some error in code  kindly check before you go")
                print(e)
        else:
            print("Thanks")
        self.menu()


sbi = User()
sbi.menu()
