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

import requests
r = requests.get('https://api.github.com')
# <Response [200]>
print(r)

if r.status_code == 200:
    print('Success!')
elif r.status_code == 404:
    print('Not Found.')