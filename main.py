import datetime
class Library():
    def __init__(self):
        # self.pin=pin
        self.menu()

    def menu(self):
        user_input=input("""----------------------------------------------                              
                    1.  Enter 1 To Display Book
                    2.  Enter 2 To Issue A Book
                    3.  Enter 3 To Return A Book
                    4.  Enter 4 To Add A Book
                    5.  Enter 5 To Remove A Book
                    6.  Enter 6 To Update A Book
                    7.  Enter 7 To Add A Book
                    8.  Enter 8 To Get Current Date
                    9.  Enter 9 To Get Current Time
                    10. Enter 10 To Exit
                    """)
        # print(user_input)
        # checking Condition with provided user input
        if user_input == "1":
            self.display()
        elif user_input == "2":
            print ("Issue A Book")
        elif user_input == "3":
            print ("Return A Book")
        elif user_input == "4":
            print ("Add A Book")
        elif user_input == "5":
            print ("Remove A Book")
        elif user_input == "6":
            print ("Update A Book")
        elif user_input == "7":
            print ("Add A Book")
        elif user_input == "8":
            self.get_date
        elif user_input == "9":
            self.get_time 
        else:
            print("Good Bye")
        

    def display(self):
        with open('books.txt',"r") as f:
            lines = f.readlines()
            print(lines,end=" ")
    
    # def get_date(self):
    #     d = datetime.datetime.now()
    #     print (self.get_date)
    # def get_time(self):
    #     e = time.time.now()
    #     print (self.e)