
print("Welcome to Ngozi's Tip Calculator: The Python Version")
# Total amount of the bill
total_bill = int(input("What was the total bill?"))
# Percentage to be given as tip
tip_percentage = int(input("What percentage of  tip will you like to give?"))
tip_amount = total_bill + (total_bill * (tip_percentage/100))
spliters = int(input("How many people to slit the bill?"))