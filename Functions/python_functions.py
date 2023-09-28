


# def function_name(arg1, arg2,....): # args optional
#     #line1
#     #line2
#    return val1, val2 # optional
#

#Hello + name + good morning

# def hello_name(name):
#     print("hello world")
#
#
# hello_name(name = 'Sreeniiiii')
# print("hello " + 'Sreni' + " good morning")
# print("hello " + 'Sreni2' + " good morning")
# print("hello " + 'Sreni3' + " good morning")
# print("hello " + 'Sreni4' + " good morning")



# def hello_name(name):
#     print("hello " + name + " good morning")
#     if name == 'GHJ':
#         print( "how are you?")
#
# hello_name(name = 'Sreeni')
# hello_name(name = 'Hari')
# hello_name(name = 'Raj')
# hello_name(name = 'Chndan')
# hello_name(name = 'GHJ')

# x="test"
# import pandas as pd
# def math_op(a,b):
#     sub = a-b
#     add = a+b
#     return add, sub, x
#
# l1, l2,y = math_op(10,40) # public variable
# print(l1, l2,y)



#
# def add(a,b,l1):
#     #sum = a+b
#     return a*b,l1,l2
#
# out2= add(10,2,l1)
# print("the out2",out2)
#
#
# def add(a,b):
#     sum = a+b
#     print(sum)
#
#
# l1 = math_op(10,20)
# print("the l1 value is " ,l1)
# print(l2)
# print("sum is ",sum)
# print(mul)
# print(div)
# tup = math_op(8,40)
# print(tup)

# for i in tup:
#     print(i)


# def add(a,b):
#     print("sum of two number is :", a+b)
#     c = a+b
#     print("the c value is ", c)
#     return c
#
# c= add(4,5)
#
# print(c)
#
# c= add( a= 4, b=5)

# class test:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b
#         print("Initilizer")
#
#     def add(self):
#         print(self.a + self.b)
#
#     def sub(self):
#         print(self.a - self.b)
#
#
# obj = test(a=10, b=20)
# print(obj.add())
# print(obj.sub())




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
# def sum(a,b=10):
#     print("two arguments")
#
# sum(20,10)
# sum(10,a=20)

# def sum(*k):
#     result=0
#     for i in k:
#         result +=i
#     return result
#
# sum1 = sum(10)
# print(sum1)
# sum2= sum(1,2,3,4,5,6)
# print(sum2)

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
# Local variable


def add():
    global a,b
    a,b=10,40
    global c
    c=40
    print(a)

sum= add()
print(sum)
print("a value",a)
print("c value is ",c)

# def printc():
#     c=40
#     print("princ fun" , a)
#     print(globals())
#
# print(printc())
print(globals())

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

# import datetime
#
#
# def mygen():
#     return datetime.datetime.utcnow().strftime("%Y%m%d%-H%-M%S")
#
#
# g = mygen()
#
# print(mygen())

# cust2 = cust_info(1,'sreeni',45,doc='1234')
# print(cust2)


def add(a,b):
    return a+b

sum=add(4,5)
print(sum)
def add(a,b,c):
    return a+b+c

sum2 = add(4,5,6)
print(sum2)

def add(*k):
    result=0
    for i in k:
        result +=i
    return result
sum3 = add(3,4,5,6)
print(sum3)


def cust_info(cust_id,name, age):
    dict = {}
    print(cust_id, name,age)
    dict['cust_id'] = cust_id
    dict['name'] = name
    dict['age'] = age
    return dict

cust1 = cust_info(1,'sreeni',45)
print(cust1)

# cust2 = cust_info(1,'sreeni',45,doc='1234')
# print(cust2)

def cust_info2(**kwargs):
    print(kwargs)
    for i,j in kwargs.items():
        pass#print(i,j)

cust2 = cust_info2(id=1,name='sreeni',age=45,dob='1234',email='test')
print(cust2)

s = lambda a,b : a+b
print(s(1,2))



