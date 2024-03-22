import csv
import json

print("Hello")

with open('MultiLanguage/sifttings.json', 'r') as csv_file:
  settings = json.load(csv_file)
  
  print(settings)
