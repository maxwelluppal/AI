# Programmer: Maxwell Uppal
# Date: 3.14.24
# Program: PasswordGenerator
# Resource: https://www.youtube.com/watch?v=jRAAaDll34Q

import hashlib


def hash_password(password, salt):
    # Combine password and salt
    salted_password = password + salt
    # Hash the salted password using SHA-256
    hashed_password = hashlib.sha256(salted_password.encode()).hexdigest()
    return hashed_password


def main():
    # Accept password input from the user
    password = input("Enter your password: ")

    # Generate a salt (you might want to use a more secure method for generating salts)
    salt = "s@ltYStr1ng"

    # Hash the password using the provided salt
    hashed_password = hash_password(password, salt)

    # Print the hashed password
    print("Hashed password:", hashed_password)


if __name__ == "__main__":
    main()
