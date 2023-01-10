class Main:
    # def __init__(self):
    #     # self.menu()
    @staticmethod
    def menu():
        user_input = input('''
                    Hello. How Would you like to proceed?
                        1. IF YOU ARE A LIBRARIAN ENTER 1
                        2. IF YOU ARE A USER ENTER 2
                        3. Enter 3 to Exit .  
        ''')
        if user_input == "1":
            from Lib import Library
        elif user_input == "2":
            from Users import User

        else:
            print("   fvfvdd  ")


L = Main
L.menu()
