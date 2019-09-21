person1 = {
  "name": "John",
  "age": 36,
  "country": "Norway"
}




# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist)
# thislist[1] = "blackcurrant"
# print(thislist)
# thisset = {"apple", "banana", "cherry"}
# print(thisset)
#
# a = 33
# b = 200
# if b > a:
#   print("b is greater than a")
#
# a = 33
# b = 33
# if b > a:
#   print("b is greater than a")
# elif a == b:
#   print("a and b are equal")
#
# a = 200
# b = 33
# if b > a:
#     print("b is greater than a")
# elif a == b:
#     print("a and b are equal")
# else:
#     print("a is greater than b")
#
#
#
# # a = 2
# # b = 330
# #
# # print("A") if a > b else print("B")
#
#
#
# cars = ["Ford", "Volvo", "BMW"]
#
# print(cars)
#
# x = len(cars)
# print ('ilosc');
# print( x)
class Person:
  name = "John"
  age = 36
  country = "Norway"

print(dir(Person))


x = 'name = "John"\nprint(name)'
exec(x)


import requests

x = requests.head('http://www.onet.pl')
y = requests.head('http://www.labhar.pl')


print(x.headers)
print(y.headers)