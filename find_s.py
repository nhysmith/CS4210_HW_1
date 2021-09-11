#-------------------------------------------------------------------------*/
# AUTHOR: Nishara Hysmith
# FILENAME: title of the source file
# SPECIFICATION: This program reads a csv file and assigns the rows to a list, db. 
# Then that list is iterated through and all the positive instances are placed into a new list, positiveInstances.
# The first element in positiveInstances is used as the initial vector hypothesis. 
# Then the Maximally Specific Hypothesis is found by Find-S algorithm.
# FOR: CS 4200- Assignment #1
# TIME SPENT: 45 min - 1 hr
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
import csv

num_attributes = 4
db = []
print("\n The Given Training Data Set \n")

#reading the data in a csv file
#with open('CS_4210_HW_1/contact_lens.csv', 'r') as csvfile:
with open('contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

print("\n The initial value of hypothesis: ")
hypothesis = ['0'] * num_attributes #representing the most specific possible hypothesis
print(hypothesis)

#find the first positive training data in db and assign it to the vector hypothesis
##--> add your Python code here

#print(db)
#add all positive instances from db to a list
positiveInstances = []
for i in db:
    temp = i[len(i)-1]
#    print(temp)
    if temp == 'Yes':
        positiveInstances.append(i)

#assign the first postive instance to the hypothesis        
hypothesis = positiveInstances[0][0:4]
print("\nHypothesis:\n")
print(hypothesis)



#find the maximally specific hypothesis according to your training data in db and assign it to the vector hypothesis (special characters allowed: "0" and "?")
##--> add your Python code here

for i in positiveInstances:
    for j in range(4):
        if hypothesis[j] == '0':
            hypothesis[j] = i[j]
        elif hypothesis[j] == i[j]:
            continue
        elif hypothesis[j] == '?':
            continue
        else:
            hypothesis[j] = '?'
            
#print(hypothesis)

print("\n The Maximally Specific Hypothesis for the given training examples found by Find-S algorithm:\n")
print(hypothesis)
