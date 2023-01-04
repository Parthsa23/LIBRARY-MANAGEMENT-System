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
        self.USER_SECTION = input("Enter Your Section")

    def display_user_table(self):
        print("displaying the book")
        # mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM USER")
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

    def Return(self):
        pass

    def Penalty(self):
        pass


sbi = User()
sbi.display_user_table()
sbi.Issue()
