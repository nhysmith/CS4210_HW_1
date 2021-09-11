#-------------------------------------------------------------------------
# AUTHOR: Nishara Hysmith
# FILENAME: decision_tree.py
# SPECIFICATION: description of the program
# FOR: CS 4200- Assignment #1
# TIME SPENT: 30 - 45 mins
#-----------------------------------------------------------*/

#IMPORTANT NOTE: DO NOT USE ANY ADVANCED PYTHON LIBRARY TO COMPLETE THIS CODE SUCH AS numpy OR pandas. You have to work here only with standard vectors and arrays

#importing some Python libraries
from sklearn import tree
import matplotlib.pyplot as plt
import csv
db = []
X = []
Y = []

#reading the data in a csv file
with open('contact_lens.csv', 'r') as csvfile:
#with open('CS_4210_HW_1/contact_lens.csv', 'r') as csvfile:
  reader = csv.reader(csvfile)
  for i, row in enumerate(reader):
      if i > 0: #skipping the header
         db.append (row)
         print(row)

#transform the original training features to numbers and add to the 4D array X. For instance Young = 1, Prepresbyopic = 2, Presbyopic = 3, so X = [[1, 1, 1, 1], [2, 2, 2, 2], ...]]
#--> add your Python code here
# X =
#print(db)
temp = ["0","0","0","0"]
for i in db:
    for j in range(4):
        if i[j] == 'Young' or i[j] == 'Myope' or i[j] == 'Yes' or i[j] == 'Normal':
            #print(i[j])
            temp[j] = '1'
        elif i[j] == 'Prepresbyopic' or i[j] == 'Hypermetrope' or i[j] == 'No' or i[j] == 'Reduced':
            temp[j] = '2'
        elif i[j] == 'Presbyopic' :
            temp[j] = '3'
        else:
            temp[j] = '?'
    #print("printing")
    print(temp)
    X.append(temp[:])
    #temp.clear()
            
print(X)
#transform the original training classes to numbers and add to the vector Y. For instance Yes = 1, No = 2, so Y = [1, 1, 2, 2, ...]
#--> addd your Python code here
# Y =

for i in db:
    if i[4] == 'Yes':
        Y.append('1')
    elif i[4] == 'No':
        Y.append('2')
    else:
        print(i[4])
print(Y)
    

#fitting the decision tree to the data
clf = tree.DecisionTreeClassifier(criterion = 'entropy')
clf = clf.fit(X, Y)

#plotting the decision tree
tree.plot_tree(clf, feature_names=['Age', 'Spectacle', 'Astigmatism', 'Tear'], class_names=['Yes','No'], filled=True, rounded=True)
plt.show()
