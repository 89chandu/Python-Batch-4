# Conditional Statments 
# coditions ke according work krte hai ?

# if else 

# Control Flow :Control flow decide krta hai kee , 
# konsa code execute hoga , aur konsa code nhi 

# Why conditional statments ??
# konsa code execute krna hai konsa nhi ,ye decide kre ke liye 

# example : 

# 1. : if statment 
# Condition ke "True" hone par execute hota hai 

# syntax

# if (condition):
#     # block of code

# code

# print(5 > 2)

if (5 < 2):
    print("5 is greater")


# if - else statement :
# else ka block of code tab execute hoga jab , 
# uske upar likha hua if ya 
# elif execute na ho


# age = 19

# if (age > 18):
#     print("u can vote")
# else:
#     print("u can not vote ")  

#  if - elif - else

# marks = int(input("Enter you marks :"))

# if marks >= 90:
#     print("Grade A")
# elif marks >= 75:
#     print("Grade B")  
# elif marks >= 60:
#     print("Grade C")
# else:
#     print("Grade D")          





# Login Validation 

# username = input("Enter Username :")
# password = input("Enter Password :")

# if username == "admin" and password == "1234":
#     print("Login Successfull")
# else:
#     print("Invalid Username Or Password")  






# check postive number




# number = int(input("Enter number :"))

# if (number > 0):
#     print("Positive Number")
# elif number == 0:
#     print("Zero")    
# else:
#     print("Negative Number")    



# check whether number is even 

# num = int(input("Enter a number"))

# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Number is Odd")    


# find the greater number 
# between 2 numbers

# a = 99
# b = 8

# if a > b:
#     print("A is greater")
# else:
#     print("B is Greater or Equal")    





# Traffic Signal

# signal = "green"

# if signal == "red":
#     print("Stop")
# elif signal == "Yellow":
#     print("prepare to go")
# elif signal == "green":
#     print("Go when safe")
# else:
#     print("Invalid signal")            



# ATM Withdrawl


# account_balance = 5000

# withdrawl_amount = int(input("Enter your amount :"))

# if withdrawl_amount <= 0:
#     print("Invalid Amount")
# elif withdrawl_amount > account_balance:
#     print("Insufficient Balance")  
# else:
#     balance = account_balance - withdrawl_amount
#     print("Withdrawl succesfull")  
#     print("Remaining Balance :",balance)    




# Nested If statment :

# Jab if ke andar , dossra if statement ho use nested if kahte hai


# if (condition):
#     # block of code

#     if (condition):
#         # block of code
#     else:
#         #bloc of code 

# else:
#     #block of code 


# Scholarship Eligiblity