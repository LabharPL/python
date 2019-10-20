# import fbchat
# from getpass import getpass
# username = str(raw_input("Username: "))
# client = fbchat.Client(username, getpass())
# no_of_friends = int(raw_input("Number of friends: "))
# for i in xrange(no_of_friends):
# 	name = str(raw_input("Name: "))
# 	friends = client.fetchAllUsers() # return a list of names
# #friends = client._getUsers(name) # return a list of names
# 	friend = friends[i]
#         #print friend
# 	msg = str(raw_input("Message: "))
# #	sent = client.send(friend.uid, msg)
# 	sent = client.send(100002309201228, msg)
# 	if sent:
# 		print("Message sent successfully!")
#
# # EMAIL_ADDRESS = 'arkadiusz.harasimiuk'
# # PASSWORD = 'polka12345'
# # FRIEND_NAME = 'arkadiusz.harasimiukofficial'
# #
# # import fbchat
# #
# # client = fbchat.Client(str(EMAIL_ADDRESS),str(PASSWORD))
# # friends = client.searchForUsers(str(FRIEND_NAME))
# # friend = friends[0]
# # print(friend)
# # raw_input("ENTER")
# #
# # #sent = client.send(friend.uid, "Hey")
# # sent = client.send(100002309201228, "Hey")
# # if sent:
# #     print("Message sent successfully!")
# # else:
# #     print("Message not sent")

# -*- coding: UTF-8 -*-

from fbchat import Client
from fbchat.models import *
from datetime import datetime

now = datetime.now()

#FRIEND_NAME = 'Pola Harasimiuk'
FRIEND_NAME = 'arkadiusz.harasimiukofficial'
# #
# # import fbchat
# #
# # client = fbchat.Client(str(EMAIL_ADDRESS),str(PASSWORD))


#client = Client("<email>", "<password>")
client = Client("arkadiusz.harasimiuk", "polka12345")
friends = client.searchForUsers(str(FRIEND_NAME))

friend = friends[0]
print(friend)
#raw_input("ENTER")


print("Own id: {}".format(client.uid))

#client.send(Message(text="Hi me! It is automat working at: "+now.strftime("%m/%d/%Y, %H:%M:%S")), thread_id=100001378845714, thread_type=ThreadType.USER)
client.send(Message(text="Hi me! It is automat working at: "+now.strftime("%m/%d/%Y, %H:%M:%S")), thread_id=friend.uid, thread_type=ThreadType.USER)
#client.send(Message(text="Hi me! It is automat working at: "+now.strftime("%m/%d/%Y, %H:%M:%S")), thread_id=100002309201228, thread_type=ThreadType.USER)
#client.send(Message(text="Hi me!"), thread_id=client.uid, thread_type=ThreadType.USER)

client.logout()