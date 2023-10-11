def task(func):
    print(func)
    def inner(name):
        if name=='Abc':
            print("This is junk name")
        else:
            func(name)
    return inner

@task
def wish(name):
    print("Hello "+ name + " good morning")

wish("Sreeni")
wish("Mahesh")
wish("Abc") # ( Hello Abc this junk name
wish("Test")
wish("abc")