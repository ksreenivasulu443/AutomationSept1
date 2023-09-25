def add(a,b):
    print("sum of two number is :", a+b)
    c = a+b
    print("the c value is ", c)
    return c

c= add(4,5)

print(c)

c= add( a= 4, b=5)


# def factorial(num):
#     result=1
#     for i in range(1,num+1):
#         result=result*i
#
#     return result
#
# factorial(5)
#
# for i in range(1,6):
#     print("factorial of {} is {}".format(i,factorial(i)))


# def cal(a,b, str="this is calculation"):
#     return a+b, a-b, a/b, str
#
# ls = cal(10,20) #Positional arguments
# print(ls)
#
# ls2 = cal(a=10,b=30, str="hello") # keyword arguments
# print(ls2)
#
# ls3 = cal( 10, 50)
# print(ls3)

# def sum():
#     print(" no parameters")
#
# def sum(a):
#     print("one argument")
#
# def sum(a,b):
#     print("two arguments")

# def sum(*k):
#     result=0
#     for i in k:
#         result +=i
#     return result
#
# sum1 = sum(10)
# print(sum1)
# sum2= sum(10,20)
# print(sum2)
#
# sum3 = sum(1,2,3,4,5)
# print(sum3
# #
# def sum(ls):
#     for i in ls:
#         print(i)
#
# print(sum([1,2,3]))

# def sum( *n,a):
#     result=0
#     for i in n:
#         result += i
#
#     return a+result
#
# sum1 = sum(10,20,30)
# print(sum1)
#
# sum2 = sum(30,40, a=40)

# def display(**kwargs):
#     print(type(kwargs))
#     for i,j in kwargs.items():
#         print(i,j)
#
# print(display(name='Ha', age=25, marks=45))
#
# print(display(ram='Ha', age=25, marks=45))


# Global variable
#Local variable

# a=10
# def add():
#     global a,b
#     a,b=10,40
#     print(a)
#
# sum= add()
# print(sum)
# print(a)
#
# def printc():
#     c=40
#     print("princ fun" , a)
#     print(globals())
#
# print(printc())


# def fact(n):
#     result=1
#     for i in range(1,n+1):
#         result *= i
#     return result
#
# fact_v= fact(4)
#
# print(fact_v)

# def fact(n):
#     if n == 0:
#         result=1#result=1
#     else:
#         result= n*fact(n-1)
#         print(result,n)
#     return result
#
# a= fact(3)
# print(a)

import datetime
def mygen():
    return datetime.datetime.utcnow().strftime("%Y%m%d%-H%-M%S")

g = mygen()

print(mygen())



