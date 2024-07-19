"""
# 1) careate a variable number and assign  4+2j using complex function.print the value of number and its data type.

number = 4+2j;
print("Value of Number : " , number);
print("Data Type of Number : ", type(number));

# 2) check given number is larger than 23. 

number = int(input("Enter a Number : "));
print(number)

if(number > 23):
    print(number," is larger than 23.");
else:
    print(number," is not larger than 23.");

# 3) check given number is equal or less than 40.

number = int(input("Enter a Number : "));


if(number <= 40):
    print(number , " is equal or less than 40.");
else:
        print(number , " is not  equal or less than 40.");

# 4) check given number is not equal to 10

number = int(input("Enter a Number : "));

if(number != 10):
    print(number, " is not equal to 10");
else:
    print(number," is equal to 10");


    
# 5) take a variable and assign a marks and update the value by adding 30 to  it.

marks = 78;
marks += 30;
print("Updated Marks : " , marks);


# 6) take your first name and last name from the command line and print them along with the file name.

import sys

print("File Name : ",sys.argv[0]);
print("First Name : ",sys.argv[1]);
print("Last Name : ", sys.argv[2]);

# o/p

# File Name :  Assignment1.py
# First Name :  sainath
# Last Name :  Wankhede

# 7) take your first name and last name from the keyboard and print them.

firstName = input("Enter Your First Name : ");
lastName = input("Enter Your Last Name : ");

print("First Name : ",firstName);
print("Last Name : ",lastName);


"""

# 8) take two integer value from keyboard and print the sum of those integer values.

num1 = int(input("Enter First Number : "));
num2 = int(input("Enter Second Number : "));
sum = num1+num2;

print("Sum of ",num1," and ",num2," is ",sum);
