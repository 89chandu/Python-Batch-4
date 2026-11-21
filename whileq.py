# # # # Palindrome

# # # num = 121
# # # original = num

# # # reverse = 0

# # # while num > 0:
# # #     digit = num % 10
# # #     reverse = reverse * 10 + digit
# # #     num = num // 10

# # # if original == reverse:
# # #     print("Palindrome Number")   
# # # else:
# # #     print("Not A Palindrome")     








# # # Check Prime Number 

# # # number = 36

# # # i = 2
# # # is_prime = True

# # # if number <= 1:
# # #     is_prime = False

# # # while i < number:
# # #     if number % i == 0:
# # #         is_prime = False
# # #         break
# # #     i = i + 1

# # # if is_prime:
# # #     print("Prime Number")
# # # else:
# # #     print("Not a prime number ")    




# # # Print all prime numbers from 1 to 100

# # # num = 2

# # # while num <= 100:
# # #     i = 2
# # #     while i < num:
# # #         if num % i == 0:
# # #             break
# # #         i = i + 1

# # #     if i == num:
# # #         print(num,end=" ")
# # #     num = num + 1   



# # # arm strong
# # # aisa number jiske har digit ki power , total digits ke barabar
# # # ho aur unka sum original number ke equal ho 

# # # 153

# # # 1 = 1
# # # 5 = 125
# # # 3 = 27


# # num = 153

# # original = num
# # temp = num

# # total = 0
# # count = 0 
# # # count nikalne ke liye
# # while temp > 0:
# #     count = count + 1
# #     temp = temp // 10
# # temp = num   

# # # total nikalne ke liye
# # while temp > 0:
# #     digit = temp % 10
# #     total = total + digit ** count
# #     temp = temp // 10

# # if 153 == 153:
# #     print("Armstrong Number")    
# # else:
# #     print("Not arm strong number")    



# #  LCM - least common multiple

# # example : 4 and 6

# # multiple 4 : 4 , 8, 12, 16 ,20.....
# # multiple 6: 6 , 12 , 18 , 24.....

# # 12


# # a = 6
# # b = 9

# # i = 1

# # while True:
# #     if (a * i) % b == 0:
# #         lcm = a * i
# #         break
# #     i = i + 1

# # print("LCM",lcm)


# # ex: 12 and 18

# # factors 12 : 1,2,3,4,6,12
# # factorrs 18 : 1,2,3,6,9,18

# # hcf = 6


# a = 12 
# b = 18

# i = 1

# hcf = 1

# while i <= a and i <= b:

#     if a % i == 0 and b % i == 0:
#         hcf = i
#         # print(hcf)

#     i = i + 1   

# print("HCF",hcf)    






a = int(input("Enter your number1 :"))
b = int(input("Enter your number2 : "))

# a = input("Enter your number1 :")
# b = input("Enter your number2 : ")

print(a + b)