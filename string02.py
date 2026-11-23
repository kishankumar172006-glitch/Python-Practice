# string Concatenation and String Interpolation

# Concatenating Strings

  # Combining multiple strings together with the plus (+) operator. This process is called STRING CONCATENATION

str1 = 'Hello'
str2 = "world"

# 1st option
print(str1 + str2) # but we will notice there is no gap here

# 2nd option
str1_plus_str2 = str1 + ' ' + str2 # so ( ' ' ) this acts as single space so this says Hello'single space'world 
print(str1_plus_str2)

# Repeating Strings
 # we can also repeat a string by multiplying it using {*}

sound = 'ha'
repeated_sound = sound * 3
print(repeated_sound) # hahaha

# Concatennation only works with strings. If you try to concentrate a string with a number, you'll get a TypeError: can only concatenate str (not "int") to str

name = 'kishan'
age = 20

# print(name + age)   i have used # to make code work to, check the error just delete # before print 

# This happened because Python does not automatically convert othert data types like integers into string when you concatenate them.

# Python requires all element to be strings before it can con cantenate them. TO fix, we can covert numbers to string using [str()] which returns the string representation of the given value WITHOUT modifying the original value


print(name + str(age))



# We can also use augumented assignment operator for concatenation. This is represented by a plus and equal sign (+=), and perform both concatenation and assignment in one step

name_and_age = name      # Start with the name
name_and_age += str(age) # Append the age as string

# now this variable knows two things 1- starts with name, 2- change number to str then add both string

print(name_and_age) #kishan20

# We can also use *= to repeat a string and assign the result back to the same variable

laugh = 'ha'
laugh *= 3
print(laugh)

# Here ;augh *= 3 is equivalent to laugh = laugh * 3



# Both (+=) nad (*=) create new string and assign it to the variable; they do not modify the original string.



# String Interpolation
# The process of inserting variables and expression into a string is called string interpolation. Python has a category of string called "f-string" (short for formated string literals) which hadels interpolation

# f-string starts with f (F or f) before the quotes, and allow you to embed variables or expressions inside replacement field indicated by curly braces ({}). Here's an example

name = 'kishan'
age = '20'

#1st method
print("My name is " + name + " and I am " + str(age) + " years old")


#2nd method
name_and_age2 = f'My name is {name} and I am {age} years old'
print(name_and_age2)

num1 = 5
num2 = 10
print(f'The sum of {num1} and {num2} is {num1 + num2}')

#Curly brackets tell Python:

#"Don't treat this as ordinary text. Find the value of the variable inside these    brackets and insert it here."