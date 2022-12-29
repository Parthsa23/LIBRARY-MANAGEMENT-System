from datetime import datetime,date,time   # import date and time to get the current date and time 
from mysql.connector import connection
class Library():
    def __init__(self):
        self.pin=int(input("Enter the Pin :  "))
        self.lines=['Harry POtter','HOney sINGH','aJAY YADAV','PARTH SARASWAT','RISHABH SHARMA','GAURAV RAY']
        self.menu()
# class Menu(Library):
    def menu(self):
        user_input=int(input("""----------------------------------------------                              
                    1.  Enter 1 To Display Book
                    2.  Enter 2 To Issue A Book
                    3.  Enter 3 To Return A Book
                    4.  Enter 4 To Add A Book
                    5.  Enter 5 To Remove A Book
                    6.  Enter 6 To Update A Book
                    7.  Enter 7 To Get Current Date
                    # 8.  Enter 8 To Get Current Time
                    9. Enter 9 To Exit """))      
        # checking Condition with provided user input
        if user_input == 1:
            # self.Display()
            Display.display(self)
        elif user_input == 2:
            # self.Issue()
            Issue.issue(self)
        elif user_input == 3:
            # self.Return()
            Return.ret(self)
        elif user_input == 4:
            # self.AddBook()
            AddBook.add(self)
        elif user_input == 5:
            # self.RemoveBook()
            Remove.remove(self)
        elif user_input == 6:
            # self.UpdateBook()
            Update.update(self)
        elif user_input == 7:
            # self.get_date()
            Date.get_date(self)
        # elif user_input == 8:
        #     self.get_time()
        else:
            self.menu()
# ___________________________________________________      
class Display(Library):
    def display(self):
        # with open('books.txt',"r") as f:
        #     lines = f.readlines()
        print(self.lines)
        print ("Available list is displaying above")
        self.menu()
# ___________________________________________________
class Issue():
    def __init__(self):
            self.r=""
    def issue(self):
        print(self.lines)
        print("Note : If Intrested  in any of the above give input the first char. of the above mentioned")
        user_input=int(input("Enter the number : "))
        b=user_input-1 # deducting one value as the index always starts with zero
        r=self.lines[b] # Selecting the book and storing it in a variable named r
        # print(r)
        a=self.lines.index(r)  # checking the index  value of book selected by user 
        # print(a)  
        self.lines.remove(r) # removing the selected book with help of index 
        print("You have selected " , r ,"book  for issue")
        if b==a:
            # print("Succeded")
            print("Congratulation the Book Is Issued ")
            self.lines
            self.menu()
        else:
            print("your method is failed and now redirecting back to start")
            self.Issue()
# ___________________________________________________
class Return(Issue,Library): 
    def __init__(self): 
        print(self.r)
    def ret(self):
        print(self.r)
        print("done bro")
        self.menu()
    
# ___________________________________________________
class AddBook(Library):
    def add(self):
        confirm_pin=int(input("Enter the pin  "))
        if self.pin==confirm_pin:
            user_input=input("Add  the Book Details : - ")
            self.lines.append(user_input)
            # print(ADD)
            print(self.lines)
            self.menu()
        else:
            print("There is some issue with the method")

# ___________________________________________________
class Date(Library):
    def get_date(self):
        # Returns the current local date
        print(datetime.now())
        self.menu()
# ___________________________________________________
    def get_time(self):                          #
         print(datetime.time.now)
         self.menu()