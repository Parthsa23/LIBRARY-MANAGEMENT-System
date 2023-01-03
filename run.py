# import db
import mysql.connector
import pymysql

import db


class Library:
    def __init__(self):
        mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Password@123",
            database="LMS")

        print(mydb)

    def Add_Book(self):
        ID = int(input('Enter the number :  '))
        BOOK_NAME= input("Enter the book name:  ")
        AUTHOR_NAME=input("Enter the author name : ")
        QUANTITY=int(input("Enter the quantity/stock of the book : "))

    def display_data(self):
        print(db.Database.display_table())







sbi=Library()
# sbi.insert_data()
sbi.display_data()
