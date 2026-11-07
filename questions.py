# # Menu Driven Calculator

# while True:
#     print("----Menu Calculator----")
#     print("1.Addition")
#     print("2.Substraction")
#     print("3.Multiplication")
#     print("4.Division")
#     print("5.Exit")

#     choice = int(input("Enter Your Choice :"))

#     if choice == 5:
#         print("Calculator Closed")
#         break
#     if choice >= 1 and choice <=4:
#         num1 = int(input("Enter first number :"))
#         num2 = int(input("Enter second number :"))

#         if choice == 1:
#             print("Addition :" , num1 + num2)
#         elif choice == 2:
#             print("Substraction :", num1 - num2)
#         elif choice == 3:
#             print("Multiploication :", num1 * num2)
#         elif choice == 4:
#             print("Division :", num1 / num2)
#     else:
#         print("Invalid Choice :")        


# Guess The Number Game

# import random

# secret_number = random.randint(1,10)

# attempts = 3

# while True:

#     if attempts == 0:
#         print("You Lost !")
#         break

#     guess = int(input("enter your guess number"))
#     attempts = attempts - 1
#     if guess < secret_number:
#         print("Too Low ! , try a bigger number")
#         print(f"You have left {attempts} attempts")
#     elif guess > secret_number:
#         print("Too High ! , Try Smaller number") 
#         print(f"You have left {attempts} attempts") 
#     else:
#         print("Congratulations 🎉🎉 ! you guessed correctly")  
#         print("secret number",secret_number)
#         print("Total attempts :",attempts)
#         break     



# 1 to 100 , 

for i in range(1,101):
    if i % 7 == 0:
        print(i)