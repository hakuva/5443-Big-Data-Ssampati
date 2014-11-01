import csv
import json

# Open Input and Output files.
inputfile = open('GpsFilePoints.csv', 'r')
outputfile = open('GpsFilePoints.json', 'w')

# Fields present in the CSV file. 
fields = ("UserID","FieldID","PointID","Lat","Lng","Ele","Time","Course","Hdop"$

# Read all the lines present in CSV file.
lines = csv.reader(inputfile, fields)
# Make the input read as JSON. 
json_out = json.dumps([row for row in lines])

# print to an output file.
outputfile.write(json_out)

