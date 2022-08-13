import csv

file = open("/home/sugan/Documents/GitHub/beautiful-soup-test/output.csv")
csvreader = csv.reader(file)
header = []
header = next(csvreader)
print(header)

rows = []
for row in csvreader:
        rows.append(row)
    
print(rows)