# #Assignment operator
# ls = [1,2,3,4]
# sum=0
# sum2=0
# mul= 1
# sub=0
# div = 1
# for i in ls:
#     sum +=i
#     mul *= i
#     sub -=i # sub = sub-i
#     div /=i # div = div/i
#
# #
# #
# print(sum)
# print(mul)
# print(sub)
# print(div)
# # print(sum2)
# # print(mul)
# # print(div)
#

# Special opeartos
# 1. Identity operators ( is, is not)
# 2. Membership operator ( in , not in )

# a=10
# b=20
# c=10
# print(id(a))
# print(id(b))
# print(id(c))
# print( a is c)
# print( "print for a==b",a == c)
# # # print(a is c)
# # print("is not ", a is not b)
# # print("is not ", a is not c)
#
# ls = [1,2,3]
# ls2 = [1,2,3]
# print(id(ls))
# print(id(ls2))
# print(" ls==ls2",ls==ls2)
# print("ls is ls2",ls is ls2)


#Membership operator

# ls =[1,2,3,4]
# tup = (1,2,3)
#
# print( 6 in tup)
# print(3 in ls)
# print('1' in ls)

# str= 'Hello Sreeni, Good morning '
# #
# print('S' in str)
# print('K' in str)
# print('Bad' in str)
# print('morning' in str)
#
# print("k" not in str)
#
# for i in ls:
#     print(i)

#Operator precedence

#PEMDAS- BODMAS rule

# print((8+2)*3/2)  #(10)*3/2--> 30/2 -->15
# print((8+2)/(2*3)) # 10/(2*3) --> 10/(6)
#
#print((8+2)/2*3) # (10)/2*3 --> 5*3-->15
#
print(round((8+2)/3*2+3*2)) # (10)/3*2+3*2 --> 3.3*2+3*2-->6.6+3*2-->6.6+6--.12.6


#
# a = 20
# b = 10
# c = 15
# d = 5
# e = 0
#
# e = (a + b) * c / d       #( 30 * 15 ) / 5
# print("Value of (a + b) * c / d is ",  e)
#
# e = ((a + b) * c) / d     # (30 * 15 ) / 5
# print("Value of ((a + b) * c) / d is ",  e)
#
# e = (a + b) * (c / d);    # (30) * (15/5)
# print("Value of (a + b) * (c / d) is ",  e)
#
# e = a + (b * c) / d;      #  20 + (150/5)
# print("Value of a + (b * c) / d is ",  e)
