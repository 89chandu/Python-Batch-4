# # # Floyd's Triangle Pattern

# # # 1
# # # 2 3
# # # 4 5 6
# # # 7 8 9 10
# # # 11 12 13 14 15

# # num = 2
# # for i in range(1,6): #rows
# #     for j in range(i):
# #         print(num,end=" ")
# #         num = num + 1
# #     print()    

# # #  i   = 1 , num = 1
# # # j = 0 , j = i = 1

# # # 1

# # # i = 2 ,  num = 2

# # # j = 0 , j = i = 2
# # #  2 3


# # # i = 3 , num = 4




# # # Binary Triangle

# # # 1
# # # 0 1
# # # 1 0 1
# # # 0 1 0 1
# # # 1 0 1 0 1 

# # # for i in range(1, 6): #rows
# # #     for j in range(i):
# # #         print((i + j + 1) % 2 , end= " ")
# # #     print()    

# # # start  step 1:
# # # i = 1 , 
# # #  j = 0 , j = i = 1

# # #   (1+0+1)%2 = 0
# # # i = 2
# # # j= 0

# # # (2 + 0 + 1) % 2 = 1


# # # j = 1

# # # (2 + 1 + 1) % 2 = = 0













# # # Hollow Diamond Pattern

# # n = 5

# # # upper half

# # for i in range(1,n+1):#rows
# #     # space
# #     for j in range(n-i):
# #         print(" ",end="")
# #     #star
# #     for j in range(2*i-1):
# #         if j == 0 or j == 2 * i - 2:
# #             print("*" , end="")  
# #         else:
# #             print(" ",end="") 
# #     print()           

# # # lower half

# # for i in range(n-1,0 , -1):#rows
# #     # space
# #     for j in range(n-i):
# #         print(" ",end="")
# #     #star
# #     for j in range(2*i-1):
# #         if j == 0 or j == 2 * i - 2:
# #             print("*" , end="")  
# #         else:
# #             print(" ",end="")  

# #     print()        




# # #  important logic 
# # # if j == 0 or j == 2 * i - 2:
# # #     print("*" , end="")  
# # # else:
# # #     print(" ",end="")  







# # Hour Glass Pattern


# n = 5

# # upper half

# # for i in range(n , 0 , -1):
# #     for j in range(5-1):
# #         print(" ",end="")
# #     for j in range(2*1-1):
# #         print("*",end="")
# #     print()        
# # # lower half
# # for i in range(2,n+1):
# #     for j in range(n-i):
# #         print(" ",end="")
# #     for j in range(2*i-1):
# #         print("*",end="")
# #     print() 



# # ButterFly Pattern

# n = 5

# # Upper Half
# for i in range(1,n+1,1):
#     for j in range(i):
#         print("*" , end="")

#     for j in range(2 * (n - i)):
#         print(" " , end="")

#     for j in range(i):
#         print("*" , end= '') 

#     print()    


# # lower Half
# for i in range(n-1,0, -1):
#     for j in range(i):
#         print("*" , end="")

#     for j in range(2 * (n - i)):
#         print(" " , end="")

#     for j in range(i):
#         print("*" , end= '') 

#     print() 




        
           
    
for i in range(1,10):
    for j in range(1,i+1):
        print(chr(64+j),end=" ")
    print()    

# Note : asscii value 65 = A
#  64 + j = 65 ,  