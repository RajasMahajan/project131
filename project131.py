import csv

rows = []
def calgravity(x,y):
    return  6.67*(x/y^2)

with open("main.csv","r")as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        row.append(row)


massdata = rows[3]

Radius = rows[6]

massdatakg = massdata* 1.989e+30
raduismeters = Radius*6.957e+8

for i in massdata[0]:
    calgravity(massdata[i],Radius[i])














