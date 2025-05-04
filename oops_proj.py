class chatbook:
    def __init__(self):
        self.username = ''
        self.password = ''
        self.Login = False
        self.menu()

    def menu(self):
        user_input = input(""" 
        Welcome to Chatbook! || Hello, What do you want me to do..
              Press 1 to sign up
              Press 2 to log in
              Press 3 to create a post
              Press 4 to write a message
              Press any key to exit
              
              ->""")
        
        if(user_input == "1"):
            self.sign_up()
        elif(user_input == "2"):
            self.log_in()
        elif(user_input == "3"):
            self.create_post()
        elif(user_input == "4"):
            self.write_message()    
        else:
            exit()    
        
    def sign_up(self):
        self.username = input("Enter your username: ")
        self.password = input("Enter your password: ")
        print(f"User {self.username} signed up successfully!")
        print("\n")
        self.menu()

    def log_in(self):
        if(self.username == '' and self.password == ''):
            print("Please sign up first.")
            self.menu()
        else:    
            uname = input("Enter your username: ")
            pswd = input("Enter your password: ")

            if uname == self.username and pswd == self.password:
                print(f"User {self.username} logged in successfully!")
                self.Login = True 
            else:
                print("Invalid username or password.")
               
            self.menu()  

    def create_post(self):
        if self.Login:
            post = input("Enter your post: ")
            print(f"Post created: {post}")
        else:
            print("Please log in to create a post.")
        self.menu()  

    def write_message(self):
        if self.Login:
            message = input("Enter your message: ")
            print(f"Message sent: {message}")
        else:
            print("Please log in to send a message.")
        self.menu()          


obj = chatbook()            
