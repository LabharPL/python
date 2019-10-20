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
z = raw_input('podaj z     ')

print(x.headers)
print(y.headers)
print(z, 'To jest z')

import random
import math
print "Welcome to Sam's Math Test"
num1= random.randint(1, 10)
num2= random.randint(1, 10)
num3= random.randint(1, 10)
list=[num1, num2, num3]
maxNum= max(list)
minNum= min(list)
sqrtOne= math.sqrt(num1)

correct= False
while(correct == False):
    guess1= input("Which number is the highest? "+ str(list) + ": ")
    if maxNum == guess1:
        print("Correct!")
        correct = True
    else:
        print("Incorrect, try again")

correct= False
while(correct == False):
  guess2= input("Which number is the lowest? " + str(list) +": ")
  if minNum == guess2:
     print("Correct!")
     correct = True
  else:
    print("Incorrect, try again")

correct= False
print(list)
while(correct == False):
    guess3= raw_input("Is the square root of " + str(num1) + " greater than or equal to 2? (y/n): ")
    if sqrtOne >= 2.0 and str(guess3) == "y":
        print("Correct!")

    if sqrtOne < 2.0 and str(guess3) == "n":
        print("Correct!")
        correct = True
    else:
      print("Incorrect, try again")

print("Thanks for playing!")

