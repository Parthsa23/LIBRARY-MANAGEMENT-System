class Display():
    def __init__(self):
        with open('books.txt') as f:
            lines = f.readlines()
            print(lines)