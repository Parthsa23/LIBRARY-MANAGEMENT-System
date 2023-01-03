from datetime import datetime


class Library:
    def __init__(self):
        self.pin = int(input("Enter  Pin :  "))
        self.books = ['Harry Potter', 'Honey Singh', 'Ajay Yadav', 'Parth Saraswat', 'RISHABH SHARMA', 'GAURAV RAY']
        self.Cpin = int(input("Confirm Pin :  "))
        self.book_issued = ""
        # self.current_datetime = datetime.datetime.now()
        self.issued_time = None
        self.return_time = None
        # self.menu()

    def menu(self):
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. Enter 1 to Display Book
                        2. Enter 2 to Add Book
                        3. Enter 3 to Remove the book
                        4. Enter 4 to Update Book 
                        5. Enter 5 to Exit 
        ''')
        # print(user_input)
        if user_input == "1":
            self.display()
        elif user_input == "2":
            self.add()
        elif user_input == "3":
            self.remove()
        elif user_input == "4":
            self.update()
        else:
            # self.menu()
            print("BYe")

    def display(self):
        user_input = input("Press Y if want to DISPLAY book. Press N if No.")  # asking if you want to enroll this function
        if self.pin == self.Cpin and user_input == 'Y':
            print("The Available book are available below ")
            print(self.books)
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")

    def add(self):
        user_input = input("Press Y if want to add book. Press N if No.")  # asking if you want to enroll this function
        if self.pin == self.Cpin and user_input == 'Y':
            user_input = input("Add  the Book Details : - ")  # Entering the details of the user
            self.books.append(user_input)  # appending or adding the book details to the list
            print(self.books)  # printing the  book details to check it is added or not
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")

    def remove(self):
        user_input = input("Press Y if want to add book. Press N if No.")  # asking if you want to enroll this function
        if self.pin == self.Cpin and user_input == 'Y':
            print(self.books)
            remove_book = input("Enter the  name of the book you want to remove:  ")
            self.books.remove(remove_book)
            print("Successfully Removed ")
            print(self.books)
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")

    def update(self):
        user_input = input("Press Y if want to add book. Press N if No.")  # asking if you want to enroll this function
        if self.pin == self.Cpin and user_input == 'Y':
            print(self.books)
            book_index_number = int(input("Enter the book number  you want to update : "))
            update1 = book_index_number - 1
            update2 = input("Enter the name of updated book  :    ")
            self.books[update1] = update2
            print("Hi There! The", self.books[update1], "is updated to", update2)
            print(self.books)
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")


class User(Library):
    def display(self):
        user_input = input("Press Y if want to DISPLAY book. Press N if No.")
        if self.pin == self.Cpin and user_input == 'Y':
            print("The Available book are available below  -------------------^^^^^^^^^^--------------------")
            print(self.books)
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")
        print("-----------------------------------------------------------")

    def issue(self):
        print(self.books)
        user_input = input("Press Y if want to issue book. Press N if No.")
        if self.pin == self.Cpin and user_input == 'Y':

            print(self.books)
            print("Note : If Interested  in any of the above give input the book number  of the above mentioned")
            user_input = int(input("Enter the number : "))
            b = user_input - 1  # deducting one value as the index always starts with zero
            self.book_issued = self.books[b]  # Selecting the book and storing it in a variable named r
            # print(self.book_issued ,"yeh wali issue ki h")
            a = self.books.index(self.book_issued)  # checking the index  value of book selected by user
            self.books.remove(self.book_issued)  # removing the selected book with help of index
            print("You have selected ", self.book_issued, "book  for issue")
            if b == a:
                print("Congratulation the ", self.book_issued, "Book Is Issued ")
                currentDateAndTime = datetime.now()  # importing current datetime  and storing that in a variable
                self.issued_time = currentDateAndTime.minute  # importing only minutes from current datetime
                print(self.issued_time)  # printing current minute for comparison
            else:
                print("Something Went  Wrong ....!!!!!!!!!!!!!!")
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")
        print(self.books)
        print("___________________________________________________________________")

    def ret(self):
        # super(self.book_issued)
        user_input = input("Press Y if want to return book. Press N if No.")
        if self.pin == self.Cpin and user_input == 'Y':
            currentDateAndTime = datetime.now()  # importing current datetime  and storing that in a variable
            self.return_time = currentDateAndTime.minute  # importing only minutes from current datetime
            print(self.return_time)  # printing current minute for comparison
            print("The book issued by you was ", self.book_issued)  # printing the name of the book issued  by you.
            ret_book = self.book_issued  # storing the return book in a variable
            self.books.append(ret_book)  # adding return book to the list so that  it gets append in the list of stocks
            print("Thanks for returning the book .  Have A Great Day Ahead")

        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")
        print(self.books)

        print("___________________________________________________________________")
        print("___________________________________________________________________")

    def book_ret_time(self):
        diff_return_issue_time = self.return_time - self.issued_time  # calculating the difference in issued time and return time  and storing it in a variable
        print(diff_return_issue_time)
        if diff_return_issue_time >= 1:  # comparing  the variable with  1 minute to check for late payment
            print("Hey Mate ! You Are Late.... The return deadline is within 2 minutes and you have returned in ",
                  diff_return_issue_time, " So Fine will be charged  of rs 200")
        else:
            print("Something Went  Wrong ....!!!!!!!!!!!!!!")


hdfc = User()  # creating the variable for user class
hdfc.display()  # calling display function
hdfc.issue()  # calling issue function
hdfc.ret()  # calling return function
hdfc.book_ret_time()  # calling  book return time function
