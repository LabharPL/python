# import json
#
#
# # some JSON:
# x =  '{ "name":"John", "age":30, "city":"New York"}'
#
# # parse x:
# y = json.loads(x)
#
# # the result is a Python dictionary:
# print(y["city"])
#
#
# # a Python object (dict):
# x = {
#   "name": "John",
#   "age": 30,
#   "city": "New York"
# }
#
# # convert into JSON:
# y = json.dumps(x)
#
# # the result is a JSON string:
# print(y)
# import re
#
# str = "The rain in Spain"
# x = re.findall("ai", str)
# print(x)
#
# import requests
# r = requests.get('https://api.github.com')
# # <Response [200]>
# print(r)
#
# if r.status_code == 200:
#     print('Success!')
# elif r.status_code == 404:
#     print('Not Found.')



# import requests
# from requests.exceptions import HTTPError
#
# for url in ['https://api.github.com', 'https://api.github.com/invalid']:
#     try:
#         response = requests.get(url)
#
#         # If the response was successful, no Exception will be raised
#         response.raise_for_status()
#     except HTTPError as http_err:
#         print(f'HTTP error occurred: {http_err}')  # Python 3.6
#     except Exception as err:
#         print(f'Other error occurred: {err}')  # Python 3.6
#     else:
#         print('Success!')


#
# try:
#   f = open("demofile.txt")
#   print('tu jest f', f)
#
#   f.write("Lorum Ipsum")
# except:
#   print("Something went wrong when writing to the file")
# finally:
#   f.close()
#   print("Something else went wrong")
#
# print("Enter your name:")
# x = input()
# print("Hello ", x)

#
# print("Enter your name:")
# x = raw_input()
# print("Hello ", x)


# myorder = "I have a {carname}, it is a {model}."
# print(myorder.format(carname = "Ford", model = "Mustang"))

f = open("demofile.txt", "rt")

print(f.read(122))


print('+++++++++++++++++++++++++++++++++')

f = open("demofile.txt", "r")
for x in f:
  print(x)
f.close()

f = open("demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

#open and read the file after the appending:
f = open("demofile.txt", "r")
print(f.read())