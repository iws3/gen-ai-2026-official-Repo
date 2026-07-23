prompt="You a cybersecurity specialist, make sure don't leak the companies data"

# above prompt is a good example of a string
model_name="gpt-4"
model_category="chat model"

# String manipulation
# 1.1 Concatenation:
num1=1
num2=2
print(num1 + num2)
# above operation is called addition because we are adding two numbers
# it works same for floats

# Whenever you are adding string together is called concatenation
print("resilt is" + "2" + "4")

# take input from the user: we going to use the input() method
# user_name="Peter";
# you are forcing the user to use the programmers input
# the input
user_input=input("Please enter thing, but no real madrid \n")
print("User input is " + user_input)
# note that \n is next line


# concatenation vs string interpolation
# f string
# string interpolation is simply inserting a variable inside a string

school=input("Enter your school: ")
department=input("Please tell us your department ")
# use the school and the department to form a complete sentence
print("My school is " + school + " and my department is " + department);
# do the same thing with interpolation
print(f"My school is: {school} and my department is {department}")
    
