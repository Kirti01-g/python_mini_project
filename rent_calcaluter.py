# input we need from the user
#total rent 

rent = int(input("enter your hostel/flate rent = "))

# total food order for snaking 
food = int(input("enter the amount of food orders = "))

# total electricity units spend
electricity_spend = (input("enter the total of electricity spend = "))

# charge per unit
charge_per_unit = (input("enter the charge per unit = "))

# prsion living in room/flate 
persons = int(input("enter the no of persion living in room/flat = "))

# it  will make the output more accurate 
bill = electricity_spend * charge_per_unit

# final output 
output = (food + rent + total_bill)// persons

# total amount you have to pay 
print("enter pesion will pay =",output)
