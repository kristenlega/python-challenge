import os
import csv
 
budgetdata_csv = os.path.join("..","PyBank", "Resources", "budget_data.csv")

# Open the CSV file
with open(budgetdata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # Skip the header row
    next(csvreader, None)

    # Set the initial summing variables to 0
    monthcount = 0
    total = 0
    rowcount = 0
    previousrow = 0
    increase = 0
    decrease = 0
    totalchange = 0
 
    # Iterate through all of the rows
    for row in csvreader:

        # Count the number of rows
        rowcount = rowcount + 1

        # Count the number of months
        monthcount = monthcount + 1

        # Sum the total
        total = total + int(row[1])

        # Calculate the monthly change, exclude the first row of data
        if previousrow == 0:
            monthlychange = 0

        else:
            monthlychange = int(row[1]) - previousrow

        # Add to the total change variable
        totalchange = totalchange + monthlychange

        # If the change is the biggest increase
        if (int(row[1]) - previousrow) > increase:
            # Assign it to the variable
            increase = (int(row[1]) - previousrow)
            # And store the month
            increasemonth = row[0]

        # If the change is the biggest decrease
        if (int(row[1]) - previousrow) < decrease:
            # Assign it to the variable
            decrease = (int(row[1]) - previousrow)
            # And store the month
            decreasemonth = row[0]

        # Reset the previousrow variable
        previousrow = int(row[1])
        

# Calculate the average change
avgchange = totalchange / (rowcount - 1)

# Print the results to the terminal
print("Financial Analysis")
print("--------------------")
print(f'Total Months: {monthcount}')
print(f'Total: {total}')
# Decimal precision format citation: https://stackoverflow.com/questions/455612/limiting-floats-to-two-decimal-points
print(f'Average Change: {avgchange:.2f}')
print(f'Greatest Increase in Profits: {increasemonth} {increase}')
print(f'Greatest Decrease in Profits: {decreasemonth} {decrease}')


# Create a new text file and print the results there
results = open('analysis/PyBank_Results.txt', "w")

# Write the results - new line formatting citation: https://www.kite.com/python/answers/how-to-write-to-a-file-in-python#:~:text=Use%20writelines()%20to%20write,be%20in%20a%20single%20line.
results.write(
    "Financial Analysis" "\n"
    "--------------------" "\n"
    f'Total Months: {monthcount}' "\n"
    f'Total: {total}' "\n"
    f'Average Change: {avgchange:.2f}' "\n"
    f'Greatest Increase in Profits: {increasemonth} {increase}' "\n"
    f'Greatest Decrease in Profits: {decreasemonth} {decrease}')