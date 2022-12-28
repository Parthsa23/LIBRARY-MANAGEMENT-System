# import date and time to get the current date and time 
from datetime import datetime,date,time


class Library():

    def __init__(self):
        # self.pin=pin
        self.lines=['1 Harry POtter','2 HOney sINGH','3 aJAY YADAV','4 PARTH SARASWAT','5 RISHABH SHARMA','6 GAURAV RAY']
        self.menu()
# ['1 Harry POtter','2 HOney sINGH','3 aJAY YADAV',
            #    '4 PARTH SARASWAT','5 RISHABH SHARMA','6 GAURAV RAY']
    def menu(self):
        user_input=input("""----------------------------------------------                              
                    1.  Enter 1 To Display Book
                    2.  Enter 2 To Issue A Book
                    3.  Enter 3 To Return A Book
                    4.  Enter 4 To Add A Book
                    5.  Enter 5 To Remove A Book
                    6.  Enter 6 To Update A Book
                    7.  Enter 7 To Get Current Date
                    8.  Enter 8 To Get Current Time
                    9. Enter 9 To Exit
                    """)
        # print(user_input)
        # checking Condition with provided user input
        if user_input == "1":
            self.Display()
        elif user_input == "2":
            self.Issue()
        elif user_input == "3":
            self.Return()
        elif user_input == "4":
            self.AddBook()
        elif user_input == "5":
            self.RemoveBook()
        elif user_input == "6":
            self.UpdateBook()
        elif user_input == "7":
            self.get_date()
        elif user_input == "8":
            self.get_time()
        else:
            print("Good Bye")
        

    def Display(self):
        # with open('books.txt',"r") as f:
        #     lines = f.readlines()

        print(self.lines)
        print ()

    def Issue(self):

        # with open('books.txt',"r") as f:
        #     lines = f.readlines()
        #     print(lines)

        print(self.lines)
        print("Note : If Intrested  in any of the above give input the first char. of the above mentioned")
        user_input=int(input("Enter the number : "))
        q=user_input -1
        ranges=self.lines[q][0]
        w=int(ranges)
        r=self.lines[w]  
        self.lines.remove(r)
        print("Books Available are ", self.lines, "as the user selected" , r ,"book  for issue")
# ___________________________________________________

        if  w == user_input:
            print("Succeded")
            print(self.lines)
        else:
            self.menu()
            
    def Return(self):
        pass
    def AddBook(self):
        pass
    def RemoveBook(self):
        pass

    def UpdateBook(self):
        pass
    def get_date(self):
        # Returns the current local date
        print(datetime.now())
    def get_time(self):                          #Issue with printing only date and time seperately will check later
         print(datetime.time.now)
