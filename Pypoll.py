# The Data we need to retrieve "election analysis"
import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
print(file_to_load)

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: print file object.
    print(election_data)

# close the file.
election_data.close()

# Create a File name under new folder:
file_to_save = os.path.join("analysis", "election_analysis.txt")
# Initialize total votes
total_votes = 0

# declare a new list
candidate_options = []
# 1.Daclare the empty dictionary.
candidate_votes = {}
# winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Using the Open function with "w" mode which will help write data to election analysis file
#with open(file_to_save, "w") as txt_file:

    # Write data saying Hello world inside election alaysis.txt
   # txt_file.write("Hello World")  Replace with three counties

    # Write three counties in election analysis.txt
   #txt_file.write("Arapahoe, Denver, Jefferson ")

    # Write Header
    #txt_file.write ("Counties in the Election")
    #txt_file.write ("\n----------------------------")
    # Again Write three counties in election analysis.txt using \n
    #txt_file.write ("\nArapahoe\nDenver\nJefferson")

# To Do: read and analyze the data here :# Read the file object with reader function.
with open(file_to_load) as election_data:
	file_reader = csv.reader(election_data)
# Print the header row.
	headers = next(file_reader)
	# print(("# "), headers[0],headers[1], headers[2])
	# total_votes=0
# __________________________________________________
# A complete list of candidtates who received votes
# #Print each row in CSV file.
	#rows = csv.reader(election_data)
	for row in file_reader:
		# The total number of votes cast
		total_votes += 1

		# add the candidate name for each row
		candidate_name = row[2]
		# if the candidate does not mactch any existing existing candidate
		if candidate_name not in candidate_options:

			# add the candidate name to candidate list.
			candidate_options.append(candidate_name)
			# Begin tracking that candidate's vote count.
			candidate_votes[candidate_name] = 0
		# 1. Iterate through the candidate list.
		#for candidate_name in candidate_votes:
			# . Retrieve vote count of a candidate.
			# votes = candidate_votes[candidate_name]
			# add a vote to count
		candidate_votes[candidate_name] += 1
		#print (candidate_votes)
# ________________________________________________________________
# Save the results to our text file.
with open(file_to_save, "w") as txt_file:
	# Print the final vote count to the terminal.
	election_results = (
		f"\nElection Results\n"
		f"..................\n"
		f"Total Votes: {total_votes:,}\n"
		f"...................\n")
	print(election_results, end="")
# write the result in election result.txt
	txt_file.write(election_results)
	#print(candidate_options)
# __________________________________________________________________
	for candidate_name in candidate_votes:
		# . Calculate the percentage of votes.
		votes = candidate_votes[candidate_name]
		vote_percentage = float(votes) / float(total_votes) * 100

#print (vote_percentage)
# print winning candidate,vote count and percentage
#print (f"{candidate_name}: received  {vote_percentage} % of the vote.")
		candidate_results = (
			f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n ")
		print(candidate_results)
		txt_file.write(candidate_results)

# Determine the percentage of votes using loop through
		if votes > winning_count and vote_percentage > winning_percentage:
			winning_count = votes
			winning_percentage = vote_percentage
# Set the winning candidate equal to candidate's name		
			winning_candidate = candidate_name
#__________________________________________________________
# format_vote_percentage="{:.2f}".format(float)
# Print the winning candidate's results to the terminal.
	winning_candidate_summary = (
		f"................\n"
		f"Winner: {winning_candidate}\n"
		f"Winning Vote Count: {winning_count:,}\n"
		f"Winning Percentage: {winning_percentage:.1f}%\n"
		f"...................\n")

# Print winning candidate summary
	print(winning_candidate_summary)
# Save the winning candidate's results to the text file.
	txt_file.write(winning_candidate_summary)

#print ((total_votes),row[0],row[1], row[2])


# 5. The winner of the election based on popular vote:
