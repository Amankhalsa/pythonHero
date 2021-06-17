# 17-5-2021
# sample of string formating
# name=input("enter your name:")
name="john"
product="I phone"
price=1000
# first method
#you can use variable place of print
print(" hi \""+name+"\" Thanks for buying this \""+product+"\" for \""+str(price)+"\"")
#2nd method
print("Hi \"{}\" you have purchase this \"{}\" with this amout \"{}\" ".format(name,product,price) )
# 3rd method very easy to format
print(f"Hi \"{name}\" you have purchase this \'{product}\' with this amout \'{price}\' ")
"""
#named indexes:
txt1 = "My name is {fname}, I'm {age}".format(fname = "John", age = 36)
#numbered indexes:
txt2 = "My name is {0}, I'm {1}".format("John",36)
#empty placeholders:
txt3 = "My name is {}, I'm {}".format("John",36)

print(txt1)
print(txt2)
print(txt3)


#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "<" to left-align the value:

txt = "We have {:<8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use ">" to right-align the value:

txt = "We have {:>8} chickens."
print(txt.format(49))

#To demonstrate, we insert the number 8 to set the available space for the value to 8 characters.

#Use "^" to center-align the value:

txt = "We have {:^8} chickens."
print(txt.format(49))

#Use "F" to convert a number into a fixed point number, but display inf and nan as INF and NAN:

x = float('inf')

txt = "The price is {:F} dollars."
print(txt.format(x))

#same example, but with a lower case f:

txt = "The price is {:f} dollars."
print(txt.format(x))


#Use "+" to always indicate if the number is positive or negative:

#Use "%" to convert the number into a percentage format:

txt = "You scored {:%}"
print(txt.format(0.25))


#Use "x" to convert the number into Hex format:

txt = "The Hexadecimal version of {0} is {0:x}"

print(txt.format(255))
#Or, without any decimals:

txt = "You scored {:.0%}"
print(txt.format(0.25))

txt = "The temperature is between {:-} and {:+} degrees celsius."

print(txt.format(-3, 7))

#Use "_" to add a underscore character as a thousand separator:

txt = "The universe is {:_} years old."

print(txt.format(13800000000))

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))


#Use "," to add a comma as a thousand separator:

txt = "The universe is {:,} years old."

print(txt.format(13800000000))

#Use "b" to convert the number into binary format:

txt = "The binary version of {0} is {0:b}"

print(txt.format(5))


#concatinate

txt = "The binary version of {0} + {1} is {0}{1} "

print(txt.format("aman","preet"))
#name to boinary
st = "aman"
x=' '.join(format(ord(x), 'b') for x in st)
print(x)

"""