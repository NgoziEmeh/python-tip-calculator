
print("Welcome to Ngozi's Tip Calculator: The Python Version")
# Total amount of the bill
total_bill = int(input("What was the total bill?"))

# Percentage to be given as tip
tip_percentage = int(input("What percentage of tip will you like to give?"))

# Amount to be paid. Tip + Total bill
tip_amount = total_bill + (total_bill * (tip_percentage/100))

# Number of people to share the bill
spliters = int(input("How many people to slit the bill?"))
tip_per_person = tip_amount / spliters
print(tip_per_person)