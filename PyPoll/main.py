import os
import csv
import operator


Candidate = {}
Total_votes = 0

# Path to collect data from the Resources folder
election_dataCSV = os.path.join("..","PyPoll","election_data.csv") 
# Read in the CSV file
with open(election_dataCSV, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    for row in csvreader: 
    #The total number of votes cast
    # A complete list of candidates who received votes    
        if  row[2] not in Candidate.keys():
            Candidate[row[2]] = 1
        else:
            Candidate[row[2]] = Candidate[row[2]] + 1
        
    Total_votes = 0
    for votes in Candidate.values():
        Total_votes = Total_votes + votes
    for name, votes, in Candidate.items():
        per_candidate = round((votes/Total_votes)*100,3)
        percentage = "{:3}".format(per_candidate)
        winner = max(Candidate.items(),
        key=operator.itemgetter(1))[0]
        winner = max(Candidate.items(),
        key=operator.itemgetter(1))[0]
    Total_votes = Total_votes + 1

    # Print he analysis in asked format
    print("Election Results  ")
    print("-----------------------------------------------------------------------")
    print(f"Total Votes: {str(Total_votes)}")
    print("-----------------------------------------------------------------------")
    print(str(name) + " " + str(percentage) + "% " + "(" + str(votes) + ")")
    print("-----------------------------------------------------------------------")
    print (f"Winner: {str(winner)}")
    print("-----------------------------------------------------------------------")

    # Print he analysis in asked format
     #Create .txt file and exports the code
export_file = os.path.join("..","PyPoll","Election_Results.txt")
with open (export_file,'w',newline="") as textfile:

    textfile.write ("Election Results  " + os.linesep)
    textfile.write ("-----------------------------------------------------------------------" + os.linesep)
    textfile.write (f"Total Votes: {str(Total_votes)}"+ os.linesep)
    textfile.write ("-----------------------------------------------------------------------" + os.linesep)
    textfile.write (str(name) + " " + str(percentage) + "% " + "(" + str(votes) + ")" + os.linesep)
    textfile.write ("-----------------------------------------------------------------------" + os.linesep)
    textfile.write (f"Winner:  + {str(winner)} " + os.linesep)
    textfile.write ("----------------------------------------------------------------------")
