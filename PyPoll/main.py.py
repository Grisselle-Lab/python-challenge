
# This task is to create a Python script that analyzes the votes and calculates each of the following:

# 1-The total number of votes cast

# 2-A complete list of candidates who received votes

# 3-The percentage of votes each candidate won

# 4-The total number of votes each candidate won

# 5-The winner of the election based on popular vote.

#First I set my environment, importing the file that contains the information that the code will use.
#Imported the csv, and by preinspecting the file in excel we can identify and set the the voteid as voterslist, votelist and country. I change the terms lightly to help me trace the calculations and made a personal signature.

import csv
import sys
votelist = []
voterslist = []
countylist = []

# list of candidates
candidates = []
candidatespercent = float
candidatesvotelist = int

#set file election_data.csv to be open/read by rows per column header (voterslist,votelist and countrylist)
with open("election_data.csv") as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        voterslist.append(row[0])
        countylist.append(row[1])
        votelist.append(row[2])
        # populate candidate list if new candidate
        if row[2] not in candidates:
            candidates.append(row[2])

#Since I am going to do to calculations and need to return an index value I will use [].pop then categorize the data and convert the numerical into float (decimal).
#Reference 2
voterslist.pop(0)
countylist.pop(0)
votelist.pop(0)
candidates.remove("Candidate")

# Once everything properly identify, I can start the code for some findings, calculations and reports.
# The total number of votes cast
count = len(voterslist)
candidatesvotelist = []
for x in candidates:
    candidatesvotelist.append(0)

# The complete list of candidates who received votes 
for x in votelist:
    i = candidates.index(x)
    candidatesvotelist[i] = candidatesvotelist[i] + 1

# The percentage of votes each candidate won
# Reference 3
candidatespercent = []
for i in range(0,len(candidatesvotelist)):
    candidatespercent.append(round(float(candidatesvotelist[i])/float(count)*100))

# The winner of the election based on the popular vote
maxvotelist = max(candidatesvotelist)
windex = [i for i,y in enumerate(candidatesvotelist) if y == maxvotelist]
winner = candidates[windex[0]]

# Report output using "pout" for print out for Election Results.
# Rerefence 2
def pout():
    print("Election Results")
    print("----------------------------------")
    print("Total Votes : {0}".format(count))
    print("------------------------------")
    for i in range(0,len(candidatesvotelist)):
            print("{0}:   {1}%   ({2})".format(candidates[i],candidatespercent[i],candidatesvotelist[i]))
    print("----------------------------")
    print("Winner  :  {0} ".format(winner))
    print("------------------------------")

#Final output prints and exports summary of the analysis to terminal in .txt format
#Reference 2 and 4
pout()
with open("Summary_Election_Data.txt",'w+') as flush:
    sys.stdout = flush
    pout()

# References Sample 
# 1-Gallagher. J, (2020 July 15).Python Average: A Step-by-Step Guide. URL: https://careerkarma.com/blog/python-average/
# 2-Marcyes. J,(2020 May 3). Effective use for "PrintOut"in Python.PYPI.ORG. URL:https://pypi.org/project/pout/#:~:text=A%20collection%20of%20handy%20functions,variables%20and%20debugging%20Python%20code.&text=Pout%20tries%20to%20print%20out,when%20you're%20done%20debugging. 
# 3-Ramalho. L (2005).Fluent Python: Clear, Concise, and Effective Programming. Dictionaries and Sets:Set of Operations. 1st ed. ch3,ch4.O'Reilly Media Inc
# 4-Saha. R, (2020 April 10). File flush() method in Python.GeekforGeeks.org. URL: https://www.geeksforgeeks.org/file-flush-method-in-python/#:~:text=The%20flush()%20method%20in,using%20the%20flush()%20method.&text=This%20method%20does%20not%20require,it%20does%20not%20return%20anything.
# 5-How to find the max and min of a list in Python. (n.d.) Kite. Retrieved September 24, 2020 from: https://www.kite.com/python/answers/how-to-find-the-max-and-min-of-a-list-in-python

