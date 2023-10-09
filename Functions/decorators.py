# def decor(fun):
#     #print(fun)
#     def inner(name):
#         if name=='sunny':
#             print("Sunny bad morning")
#         else:
#             fun(name)
#     return inner
#
#
# @decor
# def wish(name):
#     print("Hello "+name+" good morning")
#
# wish("hari")
# wish("sunny")

# def decor(fun):
#     #print(fun)
#     def inner(name):
#         if name=='sunny':
#             print("Sunny bad morning")
#         else:
#             fun(name)
#     return inner
#
# def wish(name):
#     print("Hello "+name+" good morning")
#
# decorfunc = decor(wish)

def task(func):
    def inner(a,b):
        if b==0:
            print("oops we can't divide by zero")
            return
        else:
            return func(a,b)
    return inner

@task
def div(a,b):
    print(a/b)

#div(4,0)

task1 = task(div)

task1(10,5)
task1(10,0)