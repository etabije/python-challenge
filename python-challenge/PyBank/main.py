import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

# Variables
total_months = 0
net_total = 0
changes = []
#None = null value
previous_amount = None 
greatest_increase = {"date": None, "amount": float('-inf')}
greatest_decrease = {"date": None, "amount": float('inf')}

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    # Skip the header row (important!)
    next(csvreader)

    for row in csvreader:
        date = row[0]
        amount = int(row[1])
        total_months += 1  # Increment the total month counter
        net_total += amount  # Calculate net total

        # Calculate the changes in "Profit/Losses" over the entire period
        if previous_amount is not None:
            change = amount - previous_amount
            changes.append(change)  # append is a method used with lists to add an element to the end of the list

            # Check for greatest increase
            if change > greatest_increase["amount"]:
                greatest_increase["amount"] = change
                greatest_increase["date"] = date

            # Check for greatest decrease
            if change < greatest_decrease["amount"]:
                greatest_decrease["amount"] = change
                greatest_decrease["date"] = date

        # Update the previous amount to the current month
        previous_amount = amount

# Calculate the average change
if len(changes) > 0:
    average_change = sum(changes) / len(changes)
else:
    average_change = 0

# "\n" creates a line spacing
# Print financial analysis
print("Financial Analysis\n")
print("--------------------------------\n")
print(f'Total Months: {total_months}')
print(f'Total: ${net_total}')
print(f'Average Change: ${average_change:.2f}')
print(f'Greatest Increase in Profits: {greatest_increase["date"]} (${greatest_increase["amount"]})')
print(f'Greatest Decrease in Profits: {greatest_decrease["date"]} (${greatest_decrease["amount"]})')
