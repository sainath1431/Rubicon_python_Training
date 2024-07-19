# print in python languague by using print() method.
# To run python in terminal in python by following syntax : python file_name.py
# python is compiled and interpreted language.

print("Hello World");

# comment in python

# this single line comment

"""
Multi 
line 
comment
"""

print("\" hello world\""); #format specifier.
# \t --> for tab space
# \n -->  new line

# varibale : container which stores value.
# Rules to write a variable name.
# 1.it can be alphabet , number.
# 2.first character should not be number.
# 3.white spaces are not allowed.
# 4. short and descibed name.
# 5.no keyword is used. (for , if etc.)

#Data type in python : int(9) , float(9.0) , string ("sainath"), boolean(true, false) , complex (2+5j) , binary (bytes, memoryview, bytearray).
#python is not static typed lang. so we not declare type of data at time of declaration of variable (e.g. int a = 10  wrong).

a = 78;
print(a);
print(id(a)); #address of a  variable.

b=2+5j;
print(b); 
print(type(b)); # type() is used to check type of value.

# binary data type.

# c = bytes('hello' );
# print(c);

# (+) it only use when string to string addition not for string to integers.

a = 10;
b = "hello";
print("The value of a is : " + b);
print("The value of a {a} and value of b is {b}".format(a=20,b="hello"));

# Operators 
#Arithmetic Operator.
a=50;
b=20;
print(a+b); #addition
print(a-b); #substration
print(a*b); #mutiplication
print(a/b); #division
print(a%b); #modulo

#Relational Opeator.
a=4;
b=7;
print(a>b); #greater than operator 
print(a<b);#less than operator
print(a>=b);#greater than or equal to 
print(a<=b);#less than or equal to
print(a==b);#equal to equal to

#logical Operator.
a=4;
b=8;
print((a>b) or (a<b)); #logical OR operator
print((a>b ) and (a<b)); #logical AND operator
print(not(a>b)); #logical Not operator.

#BitWise Operator - >>(right shift operator) <<(left shift operator)

# 1)  4>>2 4---> 100  
#           ---> 001 (1 in decimal)

#     4<<2 4---> 000100
#           ---> 010000 (16 in decimal);

a=4;
b=2;
print(a>>b);
print(a<<b);

#identity Operator - is (if both object are same) , is not (if both object are not same.) 

x = ["apple", "banana"]
y = ["apple", "banana"]
z = x

print(x is z)

# returns True because z is the same object as x

print(x is y)

# returns False because x is not the same object as y, even if they have the same content

print(x == y)

# to demonstrate the difference betweeen "is" and "==": this comparison returns True because x is equal to y

a = 7;
b = 7;
print( a is b);

print("apple" in x); #true "apple" is present in x.
print("Tea" in x); #false "apple" is not present in x.

#command line arguments:

# to fetch cmd arguments

# import sys
# print(sys.argv); #when such use cmd arguments run from the terminal only.
# print(sys.argv[0]); # first value after python  (file name e.g. hello.py)
# print(sys.argv[1]); # second value after python
# print(sys.argv[2]); # third value after python
# print(sys.argv[3]); # fourth value after python

#take input from user.

a = int(input("Enter a number : ")); # it give integer number
print(a);

#another way

a=input("Enter a number : "); #it give string alphabet form of number.
print(int(a) + 10); #here convert explicitly a into integer and then add with 10

a=input("Enter a number : ");
print(float(a));

# home work

# 1) careate a variable number and assign  4+2j using complex function.print the value of number and its data type.
# 2) check given number is larger than 23. 
# 3) check given number is equal or less than 40.
# 4) check given number is not equal to 10
# 5) take a variable and assign a marks and update the value by adding 30 to  it.
# 6) take your first name and last name from the command line and print them along with the file name.
# 7) take your first name and last name from the keyboard and print them.
# 8) take two integer value from keyboard and print the sum of those integer values.

"""
#conditional statement.

here indentation sperates the block of code in python.


1) if cond:
        True : statement.

2) if cond:
        True : statement.
    else:
        False : statement.

3) if cond:
        statement.
    elif cond:
        statement.
    elif cond:
        statement
    else:
        statement.
    
    elif ladder.
