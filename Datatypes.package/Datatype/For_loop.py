

# for value in collection_value:
#     stmts

# list =[ 1, 2 ,4 , 'sreeni', '3+4j',1,3,43,33,'raghav']
#
# # print( list[0])
# # print( list[1])
# # print( list[2])
# # print( list[3])
# # print( list[4])
#
#
# for i in list:
#     print(i)

# str = 'Sreeni'
#
# for j in str:
#     if j == 'e':
#         print("Hello this letter is e")
#     else:
#         print(j)
#
# dict = {1:'Sreeni', 2:'Raghav', 3:'chiru'}
#
# print(dict)
# k= 'Rahul'
# for i,j in dict.items():
#     #print(i)
#     #print(j)
#     #print(" key is {0} and value is {1}".format(i,j))
#     #print(f" before updating key is {i} and value is {j} and {k}")
#     a = f"{i},{j}, {k}"
#     print(a)
#     #dict[i]=j.upper()

#

# list = [ 't_profile_name','t_profile_email', 't_profile_phone']
# catalog_name = 'test'
# database = 'test_database'
#
# for i in list:
#     count_query = f"select count(*) from {catalog_name}.{database}.{i}"
#     dup_query = f"select key_col_name, count(*) from {catalog_name}.{database}.{i} group by key_col_name"
#     print(count_query)
#     print(dup_query)

# for i in range(1,11):
#     for j in range(1,11):
#         print(f" {i} *  {j} ", i * j)
#
#
#
# #print(dict)

# a=10
# b=20
# c=30
# # print("b value is %d and c value is %d" %(b,c))
#
# a,b = eval(input("enter value")), eval(input("value of second value "))
#
# print(type(a))
# print(type(b))

# x = 1
# while x<10:
#     print(x)
#     x = x+1


for i in range(1,10):
    if i==5:
        break


