import mysql.connector


class User:
    def __init__(self):
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
                        4. Enter 4 to CHeck Penalty
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
        print("displaying the book")
        # mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM BOOKS")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)

    def Issue(self):
        sql = "INSERT INTO USER ( USER_NAME,USER_MOBILE,USER_EMAIL," \
              "USER_ROLL_NO,USER_CLASS,USER_SECTION) \
              VALUES (%s,%s,%s,%s,%s,%s)"
        val = (self.USER_NAME, self.USER_MOBILE,
               self.USER_EMAIL, self.USER_ROLL_NO, self.USER_CLASS, self.USER_SECTION)
        self.mycursor.execute(sql, val)
        self.mydb.commit()
        print(self.mycursor.rowcount, " entry were inserted.")
    def Return(self):
        pass

    def Penalty(self):
        pass


sbi = User()
sbi.menu()
