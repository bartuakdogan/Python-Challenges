import time

print("Welcome to Greetings Generator !")

name = input("Please enter your full name: ")

def greetings():
    time.sleep(0.2)
    return f"Hello, Dear {name}! Welcome to our Generator...."

print(greetings())