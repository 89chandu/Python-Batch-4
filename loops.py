



# # loop :
# # agar aapko same block of code bar bar execute krna hain
# # tab loop ka use hota hai

# # for i in range(50):
# #     print("Hello Python")

# # loop : koi bhi work bar bar krne ke liye use hone wale statment loops hai

# # range(start , stop , step) :

# # range : inbuilt function hai 

# # start :loop kaha se start hoga
# # stop : loop kaha par stop hoga
# # step : loop kitne step aage badhega

# #problem : 1 to 10 numbers print krna hai 

# # for i in range(1 , 11 , 1):
# #     print(i)


# # types of loop
# # for loop
# # while loop



# # for i in range(100):
# #     print(i,"Hello,Python")

# # numbers print krna hai 1 - 50
# # numbers printkarna hai 2 - 40 , but even 

# # for i in range(4,43,4):
# #     print(i)
# # output : 1,2,3 4,5


# # for i in range(1,6,1):
# #     print(i)


# # 20 - 2 , 


# # range(start,stop,step)

# # for i in range(1,5,1):
# #     print(i)

# #  1
# #  2
# #  3
# #  4



# # start : loop kaha se start hoga
# # stop : loop kaha par stop hoga ya break hoga
# # step : loop me increament / decrement hoga pata chalta





# # even numbers print karna

# # for i in range(2,11,2):
# #     print(i)

# # # odd number ko print krna  1 -  30

# # for i in range(1,30,2):
# #     print(i)







# # sum of numbers between 1 - 9

# total = 0

# for i in range(1,10):
#     total = total + i
#     # print(total)

# print(total)  

# #abhi i kee value : 10
# # loop kab tak chalega : 10 






# # Even and odd numbers ko print krna hai .
# #  1 - 11

# # for i in range(1,11):

# #     if i % 2 == 0:
# #         print(i," :Even")
# #     else:
# #         print(i , ": Odd")   
# 


# print numbers in reverse 

#  10 - 1

# for i in range(10,0,-1):
#     print(i)

# sum of even numbers 

# total= 0 

# for i in range(2,21,2):
#     total = total + i

# print(total)    


# Multiplication table

# number = int(input("Enter your number :"))

# for i in range(1,11):
#     print(f"{number} * {i} ={number * i}")




# Factorial of a number :

# 5!
# 5 * 4 * 3 * 2 * 1

# number = int(input("Enter you number :"))
# factorial = 1

# for i in range(1, number+1):
#     factorial = factorial * i

# print("Factorial is :",factorial)    


# Caluculate power without **

# base = 2
# exponent = 4
# result = 1

# for i in range(exponent):
#     result = result * base

# print(result)   



 
# range (start,stop,step) :
# start : loop kaha se start hoga , optional , by default zero  0
# stop : required 
# step : optional , by default 1 




# Count digits in number :
# 12345

# number = 12345
# count = 0

# for digit in str(number):
#     count = count + 1

# print("Digits :",count)




# break : loop ko break krne ya terminate ke liye use hota hai 
# break statment 


# problem : 1 - 20

# 11 par rukna

# for i in range(1,21):

#     if i == 14:
#         break
#     print(i) 

#continue  


# for i in range(1,21):
#     if i == 14:
#         continue
#     print(i) 

# break vs continue 

# differene : break pura program terminate kr deta hai
# continue : sirf us pertucular number ko skip krta hai 


# # for loop wth list

# students = ["Rahul","Priya","Aman","Neha"]

# for s in students:
#     print(s)

# numbers = [1,2,3,4,5]

# for number in numbers:
#     print(number)


# marks = [35,80,45,25,90,60]
# passed = 0

# for mark in marks:
#     if mark >= 40:
#         passed = passed + 1
# print("Passed Student :",passed)   



#find the largest number 

# numbers = [12,45,7,89,34]

# largest = numbers[0] = 89

# for number in numbers:
#     if number > largest:
#         largest = number

# print("Largest :",largest)        




# Count passing students and print those numbers

# Calculate avefrage marks 

marks = [80,90,70,85]

# len() - kitne elements present list me
# print("Number of element :",len(marks))
# # total = 325
# total = 0

# for mark in marks:
#     total = total + mark

# average = total / len(marks)

# # average = 325 / 4

# print("Total :",total) 
# print("Average :",average)


 











# sum of numbers from 1 to 10

# total = 0

# for i in range(1,11):
#     total = total + i

# print("Total :",total)  


# sum even numbers 

# 2 - 21

total = 0

for i in range(2,21,2):
    total = total + i

print(total)







