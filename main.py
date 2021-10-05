
print("Welcome to Ngozi's Tip Calculator: The Python Version")
# Total amount of the bill
total_bill = float(input("What was the total bill?"))

# Percentage to be given as tip
tip_percentage = float(input("What percentage of total bill will you like to give as tip?"))

# Amount to be paid. Tip + Total bill
tip_amount = total_bill + (total_bill * (tip_percentage/100))

# Number of people to share the bill
spliters = int(input("How many people to split the bill?"))

# Amount to be paid by each person
tip_per_person = float(tip_amount / spliters)

# Round to 2 decimal places
# rounded_tip_per_person = round(tip_per_person, 2)

# Method 2: You can also use string formatting
rounded_tip_per_person = "{:.2f}".format(tip_per_person)

# print result
print(f"Each person should pay: ${rounded_tip_per_person}")