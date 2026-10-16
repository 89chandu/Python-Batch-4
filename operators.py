

# # problem : add two numbers ?


# # a + b




# # Operators : 

# # ek opeartor ek symbol or keyword hota hai jo operation perform krne 
# # ke liye use hota hai variable ya phir values par

# # operator ek symbol ya keyword hote hai jo 
# # varibales ya phir value par operation perform krneke liye use hote hai

# # print("operation on values :",4+5)

# # a = 4
# # b = 5

# # print("operation variable par : ",(a + b))

# # example:
# # + - * /
# # and or not 



# # Operators ke type  : 

# # 1. Arithmetic Operators : 
# # Mathematical calculations ke liye use hone wale operators :

# #  example : + , - , * , / , // , % , **

# # # +
# # print(5+6)

# # # -
# # print(6-4)

# # # *
# # print(2*3)

# # # /
# # print(5/2)

# # # // : floor devision operator 
# # print(5 // 2)

# # # % (remainder) modulus
# # print(7 % 2)

# # # ** (exponantion)

# # # a = 2
# # # b = 3

# # print(6 ** 2)

# #  %
# # //
# # **


# # 2. Comparision Operators 
# # used to compare values and variables 

# # == : Equal to 
# # != : Not Equal to
# # > :Greater than
# # < : less than
# # >= : greater than or equal to
# # <= : less than or equal to

# # print(4 == 4)
# # print( 4 != 4)


# # print(4 < 6)

# # print(4 > 4)
# # print( 4 >= 4)

# # print(4 <= 4)




# # 3. Assignment
# # Assignment operators varibales ko values assign yaa phir
# #  update krne ke liye use hote hai

# # = 
# a = 4
# b = 5

# # += : assignment with addition

# x = 10

# x += 8
# # x = x + 4
# print(x)

# # -=

# y = 10

# y -= 4
# # y = y - 4

# print(y)


# # *=

# z = 10

# z *= 2
# # z = z * 2

# print(z)


# # /= division with assignment

# c = 10
# c /= 2
# print(c)

# # //= floor division with assignment

# d = 7
# d //= 2
# d = d // 2
# print(d)

# # **= 

# e = 3
# e **= 2
# e = e ** 2
# print(e)

# # %=

# f = 5

# f %= 2

# print(f)

# # logical
# # and , or , not

# # Bitwise

# # Membership : 
# # in , not in

# # Identity
# # is , is not









# # Logical Operators 
# # conditions ko combine aur reverse krne ke liye use hone wale operators

# # 1. and , 2. or , 3. not

# # age = 22
# # has_id = True

# # print(age >= 18 and has_id)


# # age = 18
# # country = "india"

# # if(age >= 18 and country == "india"):
# #     print("u can vote")
# # else:
# #     print("u can not vote")    

# # and : dono conditions true honi chahiye tab mai
# #  true return kruga


# # age = 17
# # country = "india"

# # if(age >= 18 or country == "india"):
# #     print("u can vote")
# # else:
# #     print("u can not vote")   


# # or : multiple comnditions me se ek condition true honi chaiye  


# # age = 18
# # country = "india"

# # if(not(age >= 18 and country == "india")):
# #     print("u can vote")
# # else:
# #     print("u can not vote") 
 

# # a = False
# # print(not(a))

# # not : result ko reverse krta hai
# # true ko false , aur false ko true


# # is_raining = False

# # print(not(is_raining))



# # Bitwise Operators :

# # Binary bits ke upar operators perform krne ke liye
# # use hote hai

# # 5 = 0101
# # 3 = 0011
# # ---------------

# # 0001 : and  decimal me 1

# # 0111 : or dicimal me 7 

# # 0110  : xor decimal me 6 output

# # & - BITWISE AND
# # dono corresponding bits 1 honi chahiye 
# # 1

# # << : left shift











# print("Bitwise Operators :")
# print(5 & 3)

# # OR |
# # kisi bhi corresponding bits me 1 hona chahiye
# # to result 1 hoga
# print(5 | 3)

# # XOR
# # bits different ho to 1 , same ho to 0

# print(5 ^ 3)

# # ^

# # NOT ~ : python integers : 8 bit

# # 5

# # 00000101

# print(~5)

# # 11111010



# # practice 

# # 17 // 5
# # 17 % 5

# # and aur or

# # 5 code example

# # not ke 4 example

# # comprasion operators sare use krne 
# # ek code me


# # assignment operators sare code likhna hai

# # a = 4
# # b = 5

# # if (not(a == b and a > b)):
# #     print("thik hai")
# # else:
# #     print("thik nhi hai ")    


# # Left shift : <<


# # 5 : 0101

# # 1010

# # print(5 << 4)

# # sari bits ko 4 position left shift kro


# # right shift >>

# #  10 : 1 0 1 0

# # print(10 >> 1)

# # # sari bits ko ek position right shift kro

# # # 0 1 0 1





# # decimal : 1

# # binary : 0001

# # print(1 << 1)

# #  0 0 0 1

# # 0 0 1 0













# if(2 > 3):
#     print("sjhbxs")


# print("hello")
# print('hello')



# a = 4
# print(type(a))


a = 'Hello'
b = 'World'
print(a + " " + b)
