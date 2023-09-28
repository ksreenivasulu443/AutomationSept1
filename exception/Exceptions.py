def math(a,b):
    try:
        div=a/b
        print(div)
        return div
    except :
        print("can't divide by zero")
    finally:
        print("executed finally")


math(4,5)
math(4,2)
