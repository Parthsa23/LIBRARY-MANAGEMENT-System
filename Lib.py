# import db
import mysql.connector


class Library:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")
        self.mycursor = self.mydb.cursor()

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Display Book
                        2. Enter 2 to Add Book
                        3. Enter 3 to Delete Data
                        4. Enter 4 to Display User Log
                        5. Enter 5 to Display User Late Payment Log
                        6. Enter 6 to Exit 
        ''')
        if user_input == "1":
            self.Display_Data()
        elif user_input == "2":
            self.Add_Book()
        elif user_input == "3":
            self.Delete_Book()
        elif user_input == "4":
            self.Display_User_LOG()
        elif user_input == "5":
            self.Display_User_TABLE_LATE_LOG()
        else:
            self.menu()

    def Display_Data(self):
        print("displaying the book")
        # mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM BOOKS")
        myresult = self.mycursor.fetchall()
        for x in myresult:
            print(x)
        # print(Display_data)
        self.menu()

    def Add_Book(self):
        print("Adding the book")
        BOOK_NAME = input("Enter Book Name :  ")
        AUTHOR_NAME = input("Enter Author Name :  ")
        QUANTITY = int(input("Enter Quantity :  "))
        # mycursor = self.mydb.cursor()
        sql = "INSERT INTO BOOKS ( BOOK_NAME,AUTHOR_NAME,QUANTITY) \
              VALUES (%s,%s,%s)"
        val = (BOOK_NAME, AUTHOR_NAME, QUANTITY)
        self.mycursor.execute(sql, val)

        self.mydb.commit()
        print(self.mycursor.rowcount, " entry were inserted.")
        self.Display_Data()
        self.menu()

    def Delete_Book(self):

        delete_id = int(input("Enter the ID  you want to delete : "))
        sql = "DELETE FROM BOOKS WHERE ID =  %s "
        # val = [('delete_id')]
        self.mycursor.execute(sql, (delete_id,))
        self.mydb.commit()
        print(self.mycursor.rowcount, "record(s) deleted")

        self.menu()

    def Display_User_LOG(self):
        print("displaying the USER LOG")
        # mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM USER")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
        # print(Display_data)
        self.menu()

    def Display_User_TABLE_LATE_LOG(self):
        print("displaying the USER LATE LOG")
        # mycursor = self.mydb.cursor()
        self.mycursor.execute("SELECT * FROM LATE")
        myresult = self.mycursor.fetchall()

        for x in myresult:
            print(x)
        # print(Display_data)
        self.menu()

a = Library()
a.menu()
