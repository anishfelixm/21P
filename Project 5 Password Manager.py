from cryptography.fernet import Fernet

def load_key():
    file = open("key.key", "rb")
    key = file.read()
    file.close()
    return key

key = load_key()
fer = Fernet(key)

"""
def write_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
write_key()
"""

def view():
    with open("passwords.txt","r") as file:
        data = file.readlines()
        for line in data:
            line.rstrip()
            usr, pwd = line.split("|")
            print("User: ", usr, "| Password: ", fer.decrypt(pwd.encode()).decode())

def add():
    with open("passwords.txt", "a") as file:
        username = input("Username: ")
        password = input("Password: ")
        file.write(username + "|" + fer.encrypt(password.encode()).decode() + "\n")

def main():
    while True:
        choice = input("Would you like to enter a new password or view existing passwords or quit [add, view, q]? ").strip().lower()
        if choice == "q":
            break
        if choice == "add":
            add()
        elif choice == "view":
            view()
        else:
            pass

if __name__ == "__main__":
    main()