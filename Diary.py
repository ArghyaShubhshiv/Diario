#Diary Project
#Created by ZodacReaderY with help from ol_the_troll
import sys

def create_file(n):
    print('create file')
    with open(f"c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/{n}.txt",'a+') as f:
        pass
    return f

def get_text(m): 
    print('get text')
    lines = []
    print("Diary entry:")
    with open(f"c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/{m}.txt", "r+") as f:
        for line in f:
            print(line)
    while True :
        line = input()
        if line != 'quit':
            lines.append(line) 
        else:
            a = ''
            for s in range(len(lines)):
                a += f"{lines[s]}\n"
            with open(f"c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/{m}.txt",'a') as f:
                f.write(a)
                f.write('#####################################################################################')
            sys.exit()
    text = "\n".join(lines)
    print(text)

def register():
    print('register')
    name = input("Write the Username to register: ")
    with open("c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/usernames.txt", "a") as f:
        f.write(f'{name}\n')
    print("Name in file")
    Password = input("Write the Password to register: ")
    with open("c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/passwords.txt", "a") as f:
        f.write(f'{Password}\n')
    print("Pass in file")
    create_file(name)
    login(name,Password)
    
    

def login(m,n):
    print('login')
    with open('c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/usernames.txt') as f:
        if m in f.read():
           pass
        else:
            print('Username not found')
            y_or_n = input('Would you like to login or register, l or r: ')
            if y_or_n.lower() == 'l':
                login_username = input("Enter login u: ")
                login_password = input("Enter login p: ")
                login(login_username,login_password)
            else:
                register()
    with open('c:/Users/admin/Documents/Visual Studio 2019/Arditt/Diary project/passwords.txt') as f:
        if n in f.read():
            get_text(m)
        else:
            print("Incorrect password")
            y_or_n = input('Would you like to login or register, l or r: ')
            if y_or_n.lower() == 'l':
                login_username = input("Enter login u: ")
                login_password = input("Enter login p: ")
                login(login_username,login_password)
            else:
                register()
    

login_username = input("Enter login u to enter: ")
login_password = input("Enter login p to enter: ")
login(login_username,login_password)





