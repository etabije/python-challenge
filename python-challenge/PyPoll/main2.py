import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')

# Variables
total_votes = 0
charles_votes = 0
diana_votes = 0
raymon_votes = 0
net_total = 0
example = 0

with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row (important!)
    next(csvreader)

    # The total number of votes cast
    for row in csvreader:
        candidate = row[2]
        total_votes += 1  # Increment the total votes counter

        # Count votes for each candidate
        #Use elif to differ the candidates
        if candidate == "Charles Casper Stockham":
            charles_votes += 1
        elif candidate == "Diana DeGette":
            diana_votes += 1
        elif candidate == "Raymon Anthony Doane":
            raymon_votes += 1

#The percentage of votes each candidate won
# Calculate percentages
charles_percent = (charles_votes / total_votes) * 100
diana_percent = (diana_votes / total_votes) * 100
raymon_percent = (raymon_votes / total_votes) * 100



# Determine the winner based on the highest votes
if charles_votes > diana_votes and charles_votes > raymon_votes:
    winner = "Charles Casper Stockham"
elif diana_votes > charles_votes and diana_votes > raymon_votes:
    winner = "Diana DeGette"
else:
    winner = "Raymon Anthony Doane"



print("Election Results\n")
print("--------------------------------\n")
print(f'Total Votes: {total_votes}\n')
print("--------------------------------\n")
print(f'Charles Casper Stockham: {charles_votes} ({charles_percent:.3f}%)')
print(f'Diana DeGette: {diana_votes} ({diana_percent:.3f}%)')
print(f'Raymon Anthony Doane: {raymon_votes} ({raymon_percent:.3f}%)\n')
print("--------------------------------\n")
print(f'Winner: {winner}\n')
print("--------------------------------\n")
