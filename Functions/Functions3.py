# def add(a,b,c,d=10):
#     return a+b+c+d
#
# sum1 = add(5,6,c=7)
#
# print(sum1)
#
# sum2 = add(1,b=2,c=10)
# print(sum2)

# def add(a,b):
#     return a+b
#
# sum1 = add(1,2)
# print(sum1)
#
# def add(a,b,c):
#     return a+b+c
#
# sum2 = add(1,2,3)
#print(sum2)

#sum3 = add(1,2,4,5)
#print(sum3)

# def add(*var_args):
#     mul=1
#     print(var_args[0])
#     return var_args
#
# sum1 = add(1,2,3,4,5,11,20)
# print(sum1)

# def add(**kwargs):
#     sum=0
#     for i, j in kwargs.items():
#         #print(f" Key value is {i} and value is {j}")
#         sum += j
#     return sum
#
# sum2 = add(a=1, b=2, c=3,d=4,e=5,f=10,g=28)
# print(sum2)

# def add(a):
#     sum=0
#     for i in a:
#         #print(i)
#         sum +=i
#     return sum
#
# sum1 = add(a=[1,2,3,4])
# print(sum1)
#
#
# def add(a,b):
#     return a+b

# add1 = lambda column: column.upper()
#
# sum1 = add1('sreeni')
# print(sum1)

#Exception

def div(a,b):
    failed= []
    try:
        div = a/b
        #return a/b
    except:
        print("failed")
        print(" b value shouldn't be zero")
        failed.append(b)
        return 0
    finally:
        print("this is finally block")
    return a/b





# div1 = div(20,10)
# print(div1)

div1 = div(20,20)
print(div1)
