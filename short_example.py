# #my_function()
# i = 1
# while i < 6:
#   print(i)
#   i += 1
#
#
# i = 1
# while i < 6333:
#   print(i)
#   if i == 3443:
#     break
#   i += 1
#
# for x in "banana":
#   print(x)
#
# def my_function(fname, name="Harasimiuk"):
#   print(fname + " Refsnes " + name)
#
# my_function("Emil", "Hara")
# my_function("Tobias", "Hara3")
# my_function("Arkadiusz ")
# my_function("Linus", "Hara4")
#
# def my_function(food):
#   for x in food:
#     print(x)
#
# fruits = ["apple", "banana", "cherry"]
#
# my_function(fruits)
#
#
# def my_function(x):
#   return 5 * x
#
# print(my_function(3))
# print(my_function(5))
# print(my_function(9))
#
#
# def my_function(child3, child2, child1):
#   print("The youngest child is " + child3)
#
# my_function(child1 = "Emil", child2 = "Tobias", child3 = "Linusek")
#
#
#
# def tri_recursion(k):
#   if(k>0):
#     result = k+tri_recursion(k-1)
#     print(result)
#   else:
#     result = 0
#   return result
#
# print("\n\nRecursion Example Results")
# tri_recursion(646)
#
#
# x = lambda a, b, c : a * b * c
# print(x(5, 6, 2))
#
#
#
x = 300

def myfunc():
    global x

    x = 200
    print(x)


print(x)
myfunc()



import ah1

a = ah1.person1["age"]
print(a)