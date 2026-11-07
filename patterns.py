# # #  1 to 5
# # # range(start, stop , step)

# # # for i in range(1,6):
# # #     print(i)


# # # Nested loop 

# # # 1 1
# # # 1 2
# # # 1 3
# # # 2 1
# # # 2 2
# # # 2 3
# # # 3 1
# # # 3 2
# # # 3 3

# # # for i in range(1 , 4):
# # #     for j in range(1,4):
# # #         print(i , j)

# # # range(start, stop)

# # # i = 2

# # # outer loop
# # # start - 1 
# # # stop - 4

# # # inner 


# # # Ek line 5 stars

# # # 1 - 5

# # # for i in range(1,6):
# # #     print("*",end="")

# # #print function : by default new line me bhejta hai
# # # usi problem ke liye end = "" 



# # # Rectangle pattern

# # # Targeted output

# # # * * * *
# # # * * * *
# # # * * * *

# # # for i in range(3):
# # #     for j in range(4):
# # #         print("*" , end=" ")
# # #     print()  
# # # 

# # # a = 6
# # # b = 6 
# # # name = "rahul"
# # # c = 6.7

# # # # type()

# # # print(type(name))


# # # 2 numbers ko add krna
# # # +

# # # Arithmetic operator :
# # # ,+ ,- ,* ,/ ,** ,// ,%

# # # print(6+6)

# # # print(4 ** 3)

# # # print(4 // 3)

# # # print(7 % 3)







# # # comparision operator
# # #  variables yaa phir value ko compare krne me use hote hai 
# # # output hamesa : True yaa Phir False

# # #  == equals to
# # #  != not equals to
# # #  >
# # #  <
# # #  >=
# # #  <=

# # # Boolean : True / False


# # # print(6 != 6)
# # # print( 6 < 7)

# # # print(6 >= 6)
# # # print(5 <= 8)


# # # Assisgnment operator
# # # =
# # # +=
# # # -=
# # # *=
# # # /=
# # # //=
# # # **=
# # # %=


# # a = 7
# # # assign with add
# # # a += 3
# # a = a + 3

# # b = 8

# # b += 2
# # # b = b + 2

# # c = 5
# # c *= 5

# # print(c)







 






# # Logical Opeartors

# # and or not

# # and 
# # sari conditions true honi chhahiye

# # print(5 == 5 and 6 == 5)

# # or 

# # print(5 == 5 or 6 == 5)
# # multiple conditions mese ek condition true honi chhahiye 


# # not

# # print(not(5 > 6))



# # Triangle Pattern 

# # *
# # **
# # ***
# # ****
# # *****

# # for i in range(1,6):
# #     for j in range(5):
# #         print("*",end="")
# #     print() 

#  #    i = 4

# # outer loop : i wala loop : jab uski value ek increment hoti tab
# # inner loop pura execute ek baar

# # inverted triangle

# # * * * * *
# # * * * *
# # * * *
# # * *
# # *

# # # range(start,stop,inc/dec)

# # for i in range(5, 0 , -1):
# #     for j in range(1):
# #         print("*", end=" ")
# #     print() 

# # # i = 3

      






# # left - aligned increasing numbers
# # 1
# # 1 2
# # 1 2 3
# # 1 2 3 4
# # 1 2 3 4 5

# for i in range(1,6):
#     for j in range(1,5+1):
#         print(j, end=" ")
#     print()  

# # i = 6
# # j = 1 , stop kab = j = 6



# # repeated row numbers

# # 1
# # 2 2
# # 3 3 3
# # 4 4 4 4

# for i in range(1,5):#rows
#     for j in range(i):
#         print(i,end=" ")
#     print()    
    


# Decreasing Number Sequence

# 1 2 3 4 5
# 1 2 3 4
# 1 2 3
# 1 2
# 1

# for i in range(5,0,-1): #row
#     for j in range(1,1+1):
#         print(j, end= " ")
#     print() 


# # i = 0 , i = 0
      

# repeated numbers pattern

# 1
# 22
# 333
# 4444
# 55555
# 666666

# for i in range(1,9):
#     for j in range(i):
#         print(i,end="")
#     print()    

# # i = 1 , 



# Starting Number Change

# 1 2 3 4 5
# 2 3 4 5
# 3 4 5
# 4 5
# 5

# for i in range(1,7):
#     for j in range(i,7):
#         print(j,end=" ")
#     print()    


# i = 2 , i = 7
# 



# Right-aligned triangle

#       *
#     * *
#   * * *
# * * * *

# n = 4
# for i in range(1,n+1): #rows

#     # spaces print krega
#     for j in range(4-4):
#         print("1",end="1")

#     #star print krne wala loop 
#     for k in range(4):
#         print("*",end=" ")   

    # print()  

# i = 3   , n + 1 = 5 ,



# Full Pyramid 


#      *
#    * * *
#  * * * * *
# * * * * * * *

n = 4

# for i in range(1,n+1):#row
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()        



# innverted Pyramid
# *********
# *******
#  *****
#   ***
#    * 

# n = 5
# for i in range(n,0,-1):#row
#     # space print wala loop 
#     for j in range(n-1):
#         print(" ",end="")
#     #star print krne wala loop 
#     for k in range(2*i - 1):
#         print("*",end="")
#     print()  

# step 1 :

# i = 5 ,  -1 
# j = 0 , 0
# k = 0 ,  k = 9

# step 2 :
# i = 4 
# j = 0 ,  j = 1
# k = 0 , 

# step 3

# i = 3

# step 4

# i = 2

# step 5
# i = 1







# Diamond Pattern

n = 4

# # upar half
# for i in range(1,n):#row
#     for j in range(n-i):
#         print(" ",end="")
#     for k in range(2*i-1):
#         print("*",end="")
#     print()  

# # lower half
# for i in range(n,0,-1):#row
#     # space print wala loop 
#     for j in range(n-i):
#         print(" ",end="")
#     #star print krne wala loop 
#     for k in range(2*i - 1):
#         print("*",end="")
#     print()       





# Hollow pattern

# Hollow Square

# i == 0 or i == n - 1 or j == 0 or j == n - 1:
# en charo me se koi ek condtion true hai to "*" print otherwise space print hoga

# n = 5

# for i in range(n):#rows
#     for j in range(n):
#         if i == 0 or i == n - 1 or j == 0 or j == n - 1:
#             print("*" , end=" ")
#         else:
#             print(" ",end=" ")   
#     print()  

# step 1:
#  i = 0 , i  = 5 
# j = 0 , j = 5
# j = 1
# j = 2
# j = 3
# j = 4
# * * * * *   

# step 2 : 
# i = 1 
# j = 0 , j = 5  
# j = 1
# j = 2
# j = 3
# j = 4
# *       *

# step 3:
# i = 2 
# j = 0 , j = 5  
# j = 1
# j = 2
# j = 3
# j = 4
# *       *    
# 
# step 4:
#   

# i = 3 
# j = 0 , j = 5  
# j = 1
# j = 2
# j = 3
# j = 4

# step 5 :
# i = 4
# j = 0
# j = 1
# j = 2
# j = 3
# j = 4

# * * * * *


# Hollow Right Angle

# n = 4

# for i in range(1,n+1):
#     for j in range(1,4+1):
#         if j == 1 or j == i or i == n:
#             print("*", end=" ")
#         else:
#             print(" ",end=" ")  
#     print()  
    

#  i = 1     
#  j = 1  

# i = 2
# j = 1
# j = 2
# j = 3


# i = 3
# j = 1


# i = 4
            