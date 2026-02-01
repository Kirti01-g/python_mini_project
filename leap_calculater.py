# this is a leap calculater for clearifing the basic of the code 
# and master the if-else statement and function

# step1 : get user input and convert it to an integer

year = int(input("enter a year : "))

# step 2: the logic ladder
 
if (year % 4 == 0 and year % 100 != 0)
        or (year % 400 == 0):
    print(f"{year} is a leap year!")
else:
    print(f"{year} is not a leap year!")
        