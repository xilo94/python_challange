#First I imported the file
from datetime import date
import os

#Import CSV file
import csv
import statistics
csvpath = '/Users/xilo/Desktop/Bootcamp/Homework/Python_Challange/python_challange/PyBank/Resources/budget_data.csv'
output_file = '/Users/xilo/Desktop/Bootcamp/Homework/Python_Challange/python_challange/PyBank/Analysis'
output_files = '/Users/xilo/Desktop/Bootcamp/Homework/Python_Challange/python_challange/PyBank/budget_analysis.txt'

#Creating the variables
total_months = 0
net_total = 0
total_change = 0
previous_budget =0
current_budget=0
change_months = 0
great_increase = 0
great_decrease = 0
increase_date = ""
decrease_date = ""
average = 0



with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile,delimiter=",")  

    next(csv_reader)

    for row in csv_reader:
    
        
        total_months = total_months +1 
        net_total = net_total+ int(row[1])
        current_budget = int(row[1])
        change = 0
    

#Changes
        if previous_budget != 0:
            change = current_budget - previous_budget
            total_change = total_change + change
            change_months = change_months +1    

        previous_budget = current_budget

        if change > great_increase:
            great_increase = change
            increase_date = row[0]
        
        if change < great_decrease:
            great_decrease = change
            decrease_date = row[0]
     

average = (total_change) / (total_months)

output= f"""
Financial Analysis
----------------------------
Total Months: {total_months}
Total: ${net_total}
Average Change: ${average:.2f}
Greatest Increase in Profits {increase_date} (${great_increase})
Greatest Decrease in Profits: {decrease_date} (${great_decrease})
"""
print(output)

with open(output_file, 'w') as outputfile:
    outputfile.write(output)

# print(output)
# with open(output_files, "w") as txt_file:
#     output_files.write(output)
