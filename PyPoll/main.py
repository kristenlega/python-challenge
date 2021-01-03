import os
import csv
 
electiondata_csv = os.path.join("..","PyPoll", "Resources", "election_data.csv")

# Open the CSV file
with open(electiondata_csv,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
 
    # Skip the header row
    next(csvreader, None)

    # Set the initial summing variables to 0 and create empty list
    totalvotes = 0
    election_results = {}

    # Iterate through all of the rows to determine each of the candidates
    for row in csvreader:

        # Count the number of votes
        totalvotes = totalvotes + 1

        # Set the candidate name as a variable
        candidate_name = row[2]

        # If the candidate is not in the dictionary, add it
        if candidate_name not in election_results:
            election_results[candidate_name] = 1

        # Otherwise, add 1 to the total votes for that candidate
        else:
            election_results[candidate_name] += 1

# Create winner votes variable
winner_votes = 0

# Determine the winner
for candidate_name in election_results:
    if winner_votes < election_results[candidate_name]:
        winner_name = candidate_name
        winner_votes = election_results[candidate_name]


# Print the results to the terminal
# Decimal precision citation: https://stackoverflow.com/questions/45310254/fixed-digits-after-decimal-with-f-strings
print("Election Results")
print("--------------------")
print(f'Total Votes: {totalvotes}')
print("--------------------")
for candidate_name in election_results:
    print(f'{candidate_name}: {(election_results[candidate_name] / totalvotes):.3%} ({election_results[candidate_name]})')
print("--------------------")
print(f'Winner: {winner_name}')
print("--------------------")


# Create a new text file and print the results there
results = open('analysis/PyPoll_Results.txt', "w")

# Write the results - new line formatting citation: https://www.kite.com/python/answers/how-to-write-to-a-file-in-python#:~:text=Use%20writelines()%20to%20write,be%20in%20a%20single%20line.
results.write(
"Election Results" "\n"
"--------------------" "\n"
f'Total Votes: {totalvotes}' "\n"
"--------------------" "\n")
for candidate_name in election_results:
    results.write(
        f'{candidate_name}: {(election_results[candidate_name] / totalvotes):.3%} ({election_results[candidate_name]})' "\n")
results.write(
"--------------------" "\n"
f'Winner: {winner_name}' "\n"
"--------------------")