import datetime
import mysql.connector


class Library:
    def __init__(self):
        self.pin = int(input("Enter  Pin :  "))

        self.cnx = mysql.connector.connect(
                                           user='root',
                                           password='Password@123',
                                           host='127.0.0.1',
                                           database='LMS'
        )
        # self.cnx.close()
        self.books = ['Harry Potter', 'Honey Singh', 'Ajay Yadav', 'Parth Saraswat', 'RISHABH SHARMA', 'GAURAV RAY']
        self.Cpin = int(input("Confirm Pin :  "))
        self.book_issued = ""
        self.current_time = datetime.datetime.now()
        # # my_books = self.cnx.cursor()
        #
        # # my_books.execute("SHOW DATABASES")
        # #
        # # for x in my_books:
        # #     print(x)
        # my_books = self.cnx.cursor()
        #
        # my_books.execute("SHOW TABLES")
        #
        # for x in my_books:
        #     print(x)


class Display(Library):
    print("Displaying the Book")

    def __init__(self):
        Library.__init__(self)

    def display(self):

        if self.pin == self.Cpin:
            print("The Available book are available below ")
            # print(self.books)
            print(self.cnx)
            # print(self.cnx('AUTHOR_NAME'))
        else:
            print("Wrong Pin")


class Issue(Library):
    print("Issuing the book")

    def __init__(self):
        Library.__init__(self)
        self.book_issued=""

    def issue(self):

        if self.pin == self.Cpin:
            print(self.books)
            print("Note : If Interested  in any of the above give input the book number  of the above mentioned")
            user_input = int(input("Enter the number : "))
            b = user_input - 1  # deducting one value as the index always starts with zero
            book_issued = self.books[b]  # Selecting the book and storing it in a variable named r
            print(book_issued)
            # print(book_issued ,"yeh wali issue ki h")
            a = self.books.index(book_issued)  # checking the index  value of book selected by user
            self.books.remove(book_issued)  # removing the selected book with help of index
            print("You have selected ", book_issued, "book  for issue")
            if b == a:
                print("Congratulation the ", book_issued, "Book Is Issued at", self.current_time)
            else:
                print("your method is failed and now redirecting back to start")
                # while True:
                #     self.books = self.books.remove(book_issued)
                #     print(self.books)

        else:
            print("Wrong Pin")
class Return(Issue):
    print("Returning the book")

    def __init__(self):
        # Library.__init__(self)
        Issue.__init__(self)

    def ret(self):
        if self.pin == self.Cpin:
            print(self.book_issued)
            print(self.books)
            print("Thanks for return the book at", self.current_time)
        else:
            print("Wrong Pin")


class AddBook(Library):
    print("Adding new book to stock")

    def __init__(self):
        Library.__init__(self)

    def add(self):
        if self.pin == self.Cpin:
            user_input = input("Add  the Book Details : - ")
            self.books.append(user_input)
            print(self.books)
        else:
            print("There is some issue with the method")


class Remove(Library):
    print("Removing the book from library")

    def __init__(self):
        Library.__init__(self)

    def remove(self):
        if self.pin == self.Cpin:
            print(self.books)
            remove_book = input("Enter the  name of the book you want to remove:  ")
            self.books.remove(remove_book)
            print("Successfully Removed ")
            print(self.books)
        else:
            print("There is some issue with the method")


class Update(Library):
    print("Updating the book  in library")

    def __init__(self):
        Library.__init__(self)

    def update(self):
        if self.pin == self.Cpin:
            print(self.books)
            book_index_number = int(input("Enter the book number  you want to update : "))
            update1 = book_index_number - 1
            update2 = input("Enter the name of updated book  :    ")
            self.books[update1] = update2
            print("Hi There! The", self.books[update1], "is updated to", update2)
            print(self.books)
        else:
            print("There is some issue with the pin you entered")


# canara = Display()
# canara.display()
hdfc = Return()
hdfc.ret()
# sbi = Issue()
# sbi.issue()
# axis = AddBook()
# axis.add()
# cnbc = Remove()
# cnbc.remove()
# idbi = Update()
# idbi.update()

