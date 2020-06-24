# Import os module
import os

# Module for reading csv
import csv

# Set path for file
csvpath = os.path.join("Resources", "budget_data.csv")

# Open the CSV
with open(csvpath,newline="", encoding="utf-8") as budget:
    csvreader = csv.reader(budget, delimiter=",")

# First row is header
    header = next(csvreader)

# Lists to store data
    total_months = []
    total_profit = []
    monthly_profit_change = []

# Run the analysis
    for row in csvreader:
        total_months.append(row[0])
        total_profit.append(int(row[1]))
    for i in range(len(total_profit)-1):
        monthly_profit_change.append(total_profit[i+1]-total_profit[i])

# Max and Min of Monthly Profit Change
max_increase_value = max(monthly_profit_change)
max_decrease_value = min(monthly_profit_change)

# Attribute Max and Min to proper Month
max_increase_month = monthly_profit_change.index(max(monthly_profit_change)) +1
max_decrease_month = monthly_profit_change.index(min(monthly_profit_change)) +1

# Print the analysis to the terminal

# Header
print("Financial Analysis")

# Seperator
print("----------------------------")

# Total Months
print(f"Total Months: {len(total_months)}")

# Total
print(f"Total: ${sum(total_profit)}")

# Average  Change
print(f"Average  Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")

# Greatest Increase in Profits
print(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_increase_value))})")

# Greatest Decrease in Profits
print(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")

# Export a text file with the results
output = os.path.join("analysis", "Financial Analysis.txt")

with open(output, "w") as file:

# Header
    file.write("Financial Analysis")
    file.write("\n")
# Seperator    
    file.write("----------------------------")
    file.write("\n")
# Total Months
    file.write(f"Total Months: {len(total_months)}")
    file.write("\n")
# Total
    file.write(f"Totatl: ${sum(total_profit)}")
    file.write("\n")
# Average  Change
    file.write(f"Average  Change: {round(sum(monthly_profit_change)/len(monthly_profit_change),2)}")
    file.write("\n")
# Greatest Increase in Profits
    file.write(f"Greatest Increase in Profits: {total_months[max_increase_month]} (${(str(max_decrease_value))})")
    file.write("\n")
# Greatest Decrease in Profits    
    file.write(f"Greatest Decrease in Profits: {total_months[max_decrease_month]} (${(str(max_decrease_value))})")