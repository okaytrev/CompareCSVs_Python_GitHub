#imports
import csv
import os

#sets  the absolute path to variable
abs_path = os.path.dirname(os.path.abspath(__file__))

#function accepts a CSV and column number as parameters, returns that column as a list
def getcolumn_aslist(csv_path, column_number):
    mylist =[]
    with open (csv_path, "r", encoding='utf-8') as csv_file: #utf-8 to avoid strange symbols, reads the CSV
        reader = csv.reader(csv_file, delimiter=',') 
        for lines in reader:
            mylist.append(lines[column_number])
    return mylist 

#function calls, path and location
hibob = getcolumn_aslist(abs_path + "\\hibob.csv", 4)
google = getcolumn_aslist(abs_path + "\\google.csv", 0)

#open file and store in variable
CSV_Differences = open(abs_path + "\\CSV_Differences.csv", "wt")

#loops through both lists generated from getcolumn_aslist and saves the differences in a text file
for item in hibob:
    if item not in google:
        CSV_Differences.write(item+"\n")

#close file
CSV_Differences.close()






