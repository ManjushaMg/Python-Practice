#NUmber Guessing Game
#setting up the game
import random
secret_number=random.randint(1,10)
i=1
while i<=3:
    num=int(input("guess the number(between 1 and 10):"))
    i=i+1
    if num>10:
        print("Your guess is out of range please guess a value between 1 and 10")
        continue
    if num>secret_number:
        print("Oops! u guessed a number higher than the secret number")
    elif num<secret_number:
        print("Sorry, it's just lower than secret number")
    elif num==secret_number:
        print("wow! Congratulations, you guessed it RIGHT!!")
        break
if num!=secret_number:
    print("Sorry,You are out of attempts")
    
#for loop
#multiplication table generator
j=int(input("Multiplication table of:"))
for i in range(1,11):
    print(j,"x",i,"=",j*i)
    
#function
#BMI calculator
def calculate_BMI():
    w=int(input("Enter your weight in kg:"))
    h=float(input("Enter your height in meteres:"))
    bmi=w/(h**2)
    print("Your BMI is:",bmi)
calculate_BMI()    
