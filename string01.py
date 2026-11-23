# If you need multiline string, you can use triple double qoutes or triple single quotes

str1 = '''multiline
string'''

str2 = """another 
multiline 
string"""

print(str1)
print(str2)

# If the string contains ' or " itself then 
# METHOD 1- use opposite qutation wrap the string

msg = "It's a sunny day"
quote = 'She said, "Hello World"'
print(msg)
print(quote)

# METHOD 2- use (\) backshalh before ' or " (which is in the string)

msg2 = 'It\'s a sunny day'
quote2 = "She said, \"Hello World\""
print(msg2)
print(quote2)


# we use \ with characters for different things

# \n - a newline

msg3 = "hello\nworld"
print(msg3)

# \t - a tab

msg4 = 'Name:\tkishan'
print(msg4)


# \\ - for single backslash

msg5 = 'C:\\users\\kishan'
print(msg5)


# If you want to check if the string contain one or more character, for that we use (in)

my_str = 'Hello world'

print('Hello' in my_str) #True
print('hey' in my_str)   #False
print('hi' in my_str)    #False
print('e' in my_str)     #True
print('f' in my_str)     #False



# To find the length of a string we {len() function} 

print(len(my_str)) #11
                   # Space count as well


# Each character in a string has a position called an index (use square bracket[])
# index is zero based which means it starts from zero
# therefore index of first character is 0 and second is 1 ad so on
# it only tells the position of character there its doest not assigne number to the space

print(my_str[0])
print(my_str[6])

# Negative indexing is also alowed
# -1 means last character -2 means second to last and so on


print(my_str[-1])
print(my_str[-2])


# In python, values can be mutable or immutable. A mutable value can be changed after it is created, ehile immutable can't.
# We can point a vairiable at a new value, which is called reassignment, but you can't change an immutable value itself by adding, removing, or replacing any of its elements.
# strings are immutable in python, but you can still reassign a variable to a different string

greeting = 'hi'
greeting = 'hello' # here value of greeting is reassigned to hello 
print(greeting)


greeting_2 = 'hello'
greeting_2 [0] = 'H'

# What are we trying to do?
#- greeting_2[0] refers to the first character of "hi".
#- We are trying to replace h with H.
# But Python gives us an error: TypeError: 'str' object does not support item assignment

