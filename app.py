# import mysql.connectors
class Library():
    def __init__(self):
        Pin=input("Enter the Pin : " )

class Menu(Library):
    def __init__(self,Pin):
        self.confirm_pin()


    def confirm_pin(self):
        Confirm_Pin=input("Enter the Confirm Pin : ")
        if Confirm_Pin==self.Pin:
            user_input=int(input("""                              
                    1.  Enter 1 To Display Book
                    2.  Enter 2 To Issue A Book
                    3.  Enter 3 To Return A Book
                    4.  Enter 4 To Add A Book
                    5.  Enter 5 To Remove A Book
                    6.  Enter 6 To Update A Book
                    7.  Enter 7 To Get Current Date
                    8.  Enter 8 To Get Current Time
                    9.  Enter 9 To Exit


                    """))
       
        # checking Condition with provided user input
        if user_input == 1:
            self.Display()
        elif user_input == 2:
            self.Issue()
        elif user_input == 3:
            self.Return()
        elif user_input == 4:
            self.AddBook()
        elif user_input == 5:
            self.RemoveBook()
        elif user_input == 6:
            self.UpdateBook()
        elif user_input == 7:
            self.get_date()
        elif user_input == 8:
            self.get_time()
        else:
            print("Good Bye")
