#First import the file
import os

#Import CSV file 
import csv
csvpath = '/Users/xilo/Desktop/Bootcamp/Homework/Python_Challange/python_challange/PyPoll/Resources/election_data.csv'
output_file = '/Users/xilo/Desktop/Bootcamp/Homework/Python_Challange/python_challange/PyPoll/Analysis'

#creating the variables
total_votes = 0
charles_percent =0
charles_count =0
diana_percent =0
diana_count =0
raymon_percent =0
raymon_count = 0
winner = 0


with open(csvpath) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")

    next(csv_reader)

    for row in csv_reader:

        total_votes = total_votes + 1

        if row[2] == "Charles Casper Stockham":
            charles_count +=1
        elif row[2] == "Diana DeGette":
            diana_count +=1
        elif row[2] == "Raymon Anthony Doane":
            raymon_count  +=1

results = {"Charles Casper Stockham": charles_count, "Diana DeGette": diana_count, "Raymon Anthony Doane": raymon_count}

#Calcualte

charles_percent =round((charles_count / total_votes) *100, 3)
diana_percent =round((diana_count / total_votes) *100, 3)
raymon_percent =round((raymon_count / total_votes) *100, 3)

winner = max(results, key=results.get)
output= f""" 

Election R esults
-------------------------
Total Votes: {total_votes}
-------------------------
Charles Casper Stockham: {charles_percent}% ({charles_count})
Diana DeGette: {diana_percent}% ({diana_count})
Raymon Anthony Doane: {raymon_percent}% ({raymon_count})
-------------------------
Winner: {winner}
"""
print(output)

with open(output_file, 'w') as outputfile:
    outputfile.write(output)