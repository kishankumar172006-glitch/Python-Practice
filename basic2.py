name = 'kishan'

# To see what data type name is we can use

print(type(name))  # <class 'str'> it means its a string


# to verify that a perticular variable is a specific type before performing operation on it. we use ininstance() function

balance = '50'  # It is a string not integer there we cant devide it

print(isinstance(balance, int)) # this will give false


# You can also check multiple types at once

print(isinstance(balance, (int, str))) # It will check if its an int or str, so the answer will be True