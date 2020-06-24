# Dependencies

import os
import csv
import collections

# Set path for file

csvpath = os.path.join("Resources", "election_data.csv")

# Open the CSV

with open(csvpath,newline="", encoding="utf-8") as election:
    csvreader = csv.reader(election,delimiter=",")

    header = next(csvreader)
    
    candidates = []

    #Define row 3 as candidate

    for row in csvreader:
        candidate = row[2]

        candidates.append(candidate)


from collections import Counter

def winner(candidates):

    #Convert list of candidates in cand_dictionary

    votes = Counter(candidates)

    election_winner = {}

    for value in votes.values():
        election_winner[value] = []

    for (key,value) in votes.items():
        election_winner[value].append(key)
    total_votes = sum(votes.values())
    c = Counter(election_winner).most_common()

    x = len(sorted(election_winner.keys(),reverse=True))

# Specify the file to write to
    output = os.path.join("analysis", "Election Results.txt")

# Open the file using read and write mode.
    with open(output, "w+") as file:
                
        file.write("Election Results")
        file.write("\n")
        file.write("-------------------------")
        file.write("\n")
        file.write(f"Total Votes: {total_votes}")
        file.write("\n")
        file.write("-------------------------")
        file.write("\n")
        for i in range(x):
            voteByCandidate = sorted(election_winner.keys(),reverse=True)[i]
            votePercentage = (voteByCandidate/total_votes)*100  
            print(election_winner[voteByCandidate]) 
            print(votePercentage) 
            print(voteByCandidate)  
            
            file.write(f"{election_winner[voteByCandidate]}: {votePercentage} ({voteByCandidate})")

        Winner = sorted(election_winner.keys(),reverse=True)[0]

        if len(election_winner[Winner])>1:
            print(sorted(election_winner[Winner])[0])
        else:
            print(election_winner[Winner][0])
            file.write(f"Winner: {election_winner[Winner]}")



winner(candidates)

