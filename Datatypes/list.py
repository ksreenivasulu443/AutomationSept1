ls1= [1,2,3,'test']

print(type(ls1[3]))

print(ls1*3)

ls2= [1,2,3]

ls5 =list(1,2,3)

print(ls1+ls2)

print([i+2 for i in ls2])

print("append",ls2.append(5))

print(ls2.index(3))

print("insert",ls1.insert(1,5))
print("after inser",ls1)

print("count",ls1.count(1))
print("before remove",ls1)
print(ls1.remove(1))
print("after remove,",ls1)

print("reverse",ls1.reverse())

print(ls1)

print("pop",ls1.pop())
print(ls1)
ls1.clear()
print("afterclear",ls1)

ls2=[1,2,3]

ls3= ls2.copy()

print(ls2)
print(ls3)

ls2.append(5)

print(ls2)
print(ls3)

ls4=ls3

print(ls2)
print(ls3)
ls3.append(10)
print(ls2)
print(ls3)




print
