# This task is to create a Python script that analyzes the records to calculate each of the following:
# 1-The total number of months included in the dataset
# 2-The net total amount of "Profit/Losses" over the entire period
# 3-The average of the changes in "Profit/Losses" over the entire period
# 4-The greatest increase in profits (date and amount) over the entire period
# 5-The greatest decrease in losses (date and amount) over the entire period

#First I set my environment, importing the file that contains the information that the code will use.
#Imported the csv, and by preinspecting the file in excel we can identify and set the months and profits as lists.
import csv
import sys
date = []
profloss = []

#set file budget_data.csv to be open/read by rows per column header (months and profit)
with open("budget_data.csv") as csvfile:
   csvreader = csv.reader(csvfile)
   for row in csvreader:
      #set = split(row,',')
      date.append(row[0])
      profloss.append(row[1])

#Since I am going to do to calculations and need to return an index value I will use [].pop then categorize the data and convert the numerical into float (decimal).
date.pop(0)
profloss.pop(0)
for i in range(0,len(profloss)):
  profloss[i] = float(profloss[i])

#Once everything properly identify, I can start the code for some findings, calculations and reports.
#The net total number and sum of "Profit/Losses" over the entire period
total = len(profloss)
total_profloss = sum(profloss)

# The average of the changes in "Profit/Losses" over the entire period
# Reference 1
avg_profloss = total_profloss/(float(total))

#The greatest increase in profits (date and amount) over the entire period.
# Reference 5
increase = max(profloss)
max = [i for i,j in enumerate(profloss) if j == increase]

# The greatest decrease in losses (date and amount) over the entire period
# Reference 5
decrease = min(profloss)
min = [i for i,j in enumerate(profloss) if j == decrease]

#Report output using "pout" for print out for Total Months, Total Profit, Average Change, Greates Increase Profict,
#and Greates Decrease in Profit.
#Reference 2
def pout():
    print("Financial Analysis")
    print("---------------------------------------------")
    print("Total Months: {0}".format(total))
    print("Total Profit: ${0:.0f}".format(total_profloss))
    print("Average Change: ${0:.2f}".format(avg_profloss))
    print("Greatest Increase in Profit: {0} (${1:.0f})".format(date[max[0]],increase))
    print("Greatest Decrease in Profit: {0} (${1:.0f})".format(date[min[0]],decrease))

#Final output prints and exports summary of the analysis to terminal in .txt format
#Reference 4
pout()
with open("Summary_Budget_Data.txt",'w+') as flush:
   sys.stdout = flush
   pout()

# References Sample 
# 1-Gallagher. J, (2020 July 15).Python Average: A Step-by-Step Guide. URL: https://careerkarma.com/blog/python-average/
# 2-Marcyes. J,(2020 May 3). Effective use for "PrintOut"in Python.PYPI.ORG. URL:https://pypi.org/project/pout/#:~:text=A%20collection%20of%20handy%20functions,variables%20and%20debugging%20Python%20code.&text=Pout%20tries%20to%20print%20out,when%20you're%20done%20debugging. 
# 3-Ramalho. L (2005).Fluent Python: Clear, Concise, and Effective Programming. Dictionaries and Sets:Set of Operations. 1st ed. ch3,ch4.O'Reilly Media Inc
# 4-Saha. R, (2020 April 10). File flush() method in Python.GeekforGeeks.org. URL: https://www.geeksforgeeks.org/file-flush-method-in-python/#:~:text=The%20flush()%20method%20in,using%20the%20flush()%20method.&text=This%20method%20does%20not%20require,it%20does%20not%20return%20anything.
# 5-How to find the max and min of a list in Python. (n.d.) Kite. Retrieved September 24, 2020 from: https://www.kite.com/python/answers/how-to-find-the-max-and-min-of-a-list-in-python
