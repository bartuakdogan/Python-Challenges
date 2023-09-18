import time 

print("Welcome to our Even or Odd Programme !.....")
time.sleep(0.3)

num = int(input("Enter your Num: "))

if (num % 2 == 0):
    time.sleep(0.3)
    print(f"Your Number is: {num}  and it's Even!")

else:
    time.sleep(0.3)
    print(f"Your Number is: {num} and it's Odd!")

