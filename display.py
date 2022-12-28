class Display(self):
    def __init__(self):
        with open('books.txt') as f:
            lines = f.readlines()