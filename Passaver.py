# A Password Saver:

import time

print("<-- Passaver -->")
print("By: Art's Interactive Software on GitHub.\n")
print("Type '1' to write a new password.")
print("Type '2' to see saved passwords.")
print("Type '3' to exit the application.\n")

def create_new_password(user_choice):
        content = input("--> Enter a password you want to save: ").strip()

        if not content:
            print("Please, enter a password you want to save!")
            return

        password_usage = input("--> Enter what will the password be used for: ").strip()

        if not password_usage:
            print("Please, enter what will the password be used for, so that you can remember easily why you made the password!")
            return

        with open(f"my_passwords.txt", "a") as password:    
            password.write(f"Password '{content}' is used for {password_usage}.\n")
            print("Password saved successfully!")

def see_the_existing_passwords(user_choice):
    try:

            with open("passaver_vault.txt", "r") as saved_passwords:
                passwords = saved_passwords.readlines()
                for line in passwords:
                    print(line.strip())

    except FileNotFoundError:
        print("No password was found saved. The file containing those passwords may have been deleted or not created yet!\n")

def exit_Passaver(user_choice):
        time.sleep(0.5)
        exit("Exitting Passaver... ")

def main():
    while True:
        user_choice = input("> ")

        if user_choice == "1":
            create_new_password(user_choice)

        if user_choice == "2":
            see_the_existing_passwords(user_choice)

        if user_choice == "3":
            exit_Passaver(user_choice)

if __name__ == '__main__':
    main()