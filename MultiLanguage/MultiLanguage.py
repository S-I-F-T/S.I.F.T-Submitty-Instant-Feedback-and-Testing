import csv
# import json

print("Hello")

with open('test.csv', 'r') as csv_file:
  settings = csv.reader(csv_file)
  
  for line in settings:
    print(line)