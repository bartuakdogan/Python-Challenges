import time



print("Enter the operation you want.")
time.sleep(0.4)
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

choose = input("Choose your operation (1/2/3/4): ")


num1 = float(input("Enter Value1: "))
num2 = float(input("Enter Value2: "))

def addition():
    time.sleep(0.4)
    return f"Equals = {num1 + num2}"

def subtraction():
    time.sleep(0.4)
    return f"Equals = {num1 - num2}"

def multip():
    time.sleep(0.4)
    return f"Equals = {num1 * num2}"

def division():
    time.sleep(0.4)
    return f"Equals = {num1 / num2}" 

if (choose == "1"):
    print(addition())

elif (choose == "2"):
    print(subtraction())

elif (choose == "3"):
    print(multip())

elif (choose == "4"):
    if (num2 != 0):
        print(division())
    else:
        print("Error! Dividing by zero is not possible.")

else:
    print("Invalid operation number. Please enter a valid number!")