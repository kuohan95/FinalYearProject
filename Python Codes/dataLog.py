import csv

with open('glog.csv') as csvfile:
    readCSV = csv.reader(csvfile, delimiter='\t')

    for row in readCSV:
        print(row)
