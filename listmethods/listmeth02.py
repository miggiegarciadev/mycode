#!/usr/bin/env python3
proto = ["ssh", "http", "https"]
protoa = ["ssh", "http", "https"]
print(proto)
proto.append("dns") # this line will add "dns" to the end of our list
protoa.append("dns") # this line will add "dns" to the end of our list
print(proto)
proto2 = [ 22, 80, 443, 53 ] # a list of common ports
proto.extend(proto2) # pass proto2 as an argument to the extend method
print(proto)
protoa.append(proto2) # pass proto2 as an argument to the append method
print(protoa)

# Program must run in python3
# Use lots of comments to describe what you're doing-- or what you WANT to do, even if you don't know how to do it yet
# Feel free to use more than one method to manipulate your list data
# You can create a new list if you like
# Add some text to the print statements you use to describe your data (you can make up labels however you wish)
# Contact the instructor if you struggle figuring out how to use methods


