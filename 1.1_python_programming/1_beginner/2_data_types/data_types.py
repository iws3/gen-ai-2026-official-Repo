"""
Module: Built-in data types
Description: Foundational material for Built-in data types.

Tutor guide:
  - Type code examples, explanations, and live demos under each topic section.

Topics:
  1. Built-in data types
"""

# 1. Built-in data types
# Tutor note: write teaching examples and code snippets here.


# Question: what is a data type..
# Everything  in python has  atype


# integer (int) data type
# memory location that stores whole numbers
student=100
age=23
epochs=200

# floats
# stores decimal numbers
# learn float manipulation
# space floats stores in the memory and how they are manipulated
accuracy=90.3;
temperature=0.7
learning_rate=0.001

# float manipulation:
print(0.1+0.2)
# comparing floats why is 0.1+0.2==0.3 (False)
# correct way
import math
# math.isclose(0.1+0.2, 0.3)


# rounding
# x=3.1415926
# print(round(x, 2))
# formatting
# print(f"{x:.2f}")

# Scientifc notation
y=1.5e6
# 1.5*10**6
# eg: 1e-5
#     1e-3
#     2e-7


# boolean
# True and False and what about 0 and 1

is_logged_in=True
is_admin=False

# String : stores text
# put strings inside of '' or ""
name="Gita";
prompt="How many ethnic groups are there in Cameroon"

# strings are immutable
name="John"
name[0]="g"
# gohn ---> give you an error
# because strings cannot be chnaged in place
# instead
# name="gohn" -->Create an entirely new string object

# Useful string methods
text="Generative Ai"
print(text.upper())
print(text.lower())
print(text.title())
print(text.capitalize())
print(text.strip())
print(text.replace("AI", "ML"))
print(text.startswith("Gen"))
print(text.endswith("Ai"))

# string indexing:
text2="MYtEXT HERE"
text2[0]
text2[:3]

# Exercises










