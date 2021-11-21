#The data we need to retrieve.
#1. The total number of votes cast
#2. A complete list of candidates who received votes
#3. The percentage of votes each candidate won
#4. The total number of votes each candidate won
#5. The winner of the election based on popular vote. 

#Add our dependencies.
import csv
import os

#Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources","election_results.csv") 

#Assign a variable to save the file to a path.
file_to_save= os.path.join("Analysis","election_analysis.txt") 
 
#1. Initialize total vote counter
total_votes = 0

#Candidat options and candidate votes
candidate_options= []
#Decalre the empty dictionary
candidate_votes= {}

#Winning Candidate and Winning Count Tracker
winning_candidate= ""
winning_count= 0
winning_percentage= 0

#Open the election results and read the file.
with open(file_to_load) as election_data:
    File_reader=csv.reader(election_data)

    #Read the header row.
    header=next(File_reader)
    print(header)

    #Print each row in the CSV file.
    for row in File_reader:
        #Add to the total vote count
        total_votes +=1

        #Print the candidate name for each row.
        candidate_name=row[2]

        #If the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates.
            candidate_options.append(candidate_name)

            #Begin tracking the candidate's vote count.
            candidate_votes[candidate_name]=0

         #Add vote to Candidates count
        candidate_votes[candidate_name] +=1 
#determine the percentage of votes for each candidate by looping through the counts.
#1.Iterate through the candidate list.
for candidate_name in candidate_votes:
    #2 Retrieve vote count of a candidate.
    votes = candidate_votes[candidate_name]
    #3 Calculate the percentage of votes.
    vote_percentage= float(votes) / float (total_votes) *100
    #To do: print out each dandidates name, vote count, and percentage of 
    #votes to the terminal.
    #4 Print the candidate name and percentage of votes
    print(f"{candidate_name}: received {vote_percentage}% of the votes")

#Determine the winning vote count and candidate
#1 Determine if the votes are greater than the winning count.
if (votes > winning_count) and (vote_percentage > winning_percentage):
    #2 If true then set winning_count = votes and winning_percentage =
    #vote percentage
    winning_counts = votes
    winning_percentage = vote_percentage
    #3 Set the winning_candidate equal to the candidate's name
    winning_candidate= candidate_name
#To do: print out the rinning candidate vote count and percentage to terminal.
print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
winning_candidate_summary= (
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"Winning Percentage: {winning_percentage:.1f}%\n"
    f"-------------------------\n")
print(winning_candidate_summary)



   



     
#Using the open() function with the "w" mode we will write data to the file.
open(file_to_save, "w")

#Creat a filename variable to a direct or Indirect path 
file_to_save= os.path.join("analysis","election_analysis.txt")

#Using the with statement open statement to file as text file.
with open(file_to_save, "w") as txt_file:
    #write three counties to the file.
    txt_file.write("Arapahoe\nDenver\nJefferson")

    
  


































