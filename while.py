
# # # # # while loop: 
# # # # # while loop kisi block of code ko bar bar
# # # # # execute krne me use hota hai
# # # # # ye tab tak execute hota hai , jab tak given condition "True" hai

# # # # # syntax 

# # # # # while condition:
# # # # #     # block of code

# # # # # example :

# # # # # print krna hai 1 to 5

# # # # # i = 1 # loop kaha se start hoga 
# # # # # while i <= 5: #condition
# # # # #     print(i)
# # # # #     i = i + 1 #increment / decremenet


# # # # # 5 to 1 print

# # # # # i = 5

# # # # # while i >= 1:
# # # # #     print(i)
# # # # #     i = i - 1


# # # # # i = 1
# # # # # while i <= 10:
# # # # #     if i % 2 != 0:
# # # # #         print(i)
# # # # #     i = i + 1






# # # # # i = 1

# # # # # while i <= 5:
# # # # #     if i == 3:
# # # # #           break
# # # # #     print(i)
# # # # #     i = i + 1

# # # # i = 0
# # # # while i < 5:
    
# # # #     if i == 3:
# # # #         continue
# # # #     print(i)
# # # #     i = i + 1





# # # # Count Digits of a number 


# # # # digit = 1234
# # # # count = 0

# # # # while 0 > 0:
# # # #     digit = digit // 10
# # # #     count = count + 1
# # # # print("Total Digits :",count)    


# # # # Sum Of Digits


# # # a = 1234
# # # print(a % 10)
# # # print(a // 10)


# # # number = 12345


# # num = 123
# # total = 0

# # while num > 0:
# #     digit = num % 10 #last digit extract
# #     total = total  + digit
# #     num = num // 10 #last digit remove krne

# # print("Sum of digits :",total)    




# # number = int(input("Enter your number"))
# # reverse = 0

# # while number > 0:
# #     digit = number % 10
# #     reverse = reverse * 10 + digit
# #     number = number // 10
  

# # print("Reversed Number :",reverse)









# # num = 4
# # fact = 1

# # i = 1
# # if num < 0:
# #     print("Factorial nhi nikal skte ")
# # else:
# #     while i <= num:
# #         fact = fact * i
# #         i = i + 1

# #     print("factorial is :", fact)        


# num = 4
# fact = 24
# i = 5

# while 5 <= 4:
#     fact = 6 * 4
#     i = i + 1
# print("factorial is :", fact) 




#1. count digits
#2. sum of digits
#3. product of digits
#4. Reverse Number
#5. Palindrome
#6. Prime Number
#7. Factorial
#8. Armstrong
#9. Perfect Number









num = 6

if num <=1:
    print("Not a prime number")
else:    
    i = 2
    while i < num:
        if num % i == 0:
            break
        i = i + 1

    if i == num:
        print("Prime Number")
    else:
        print("Not a prime number")    



