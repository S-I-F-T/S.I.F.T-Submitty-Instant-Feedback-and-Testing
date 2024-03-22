import csv
import json

print("Hello")

# with open('sifttings.csv', 'r') as csv_file:
#   settings = csv.reader(csv_file)
  
#   for line in settings:
#     print(line)

with open('sifttings.json', 'r') as j:
  settings = json.load(j)

  print(settings)

# class MultiLanguage():
#   def __init__(self):
#     with open('sifttings.csv', 'r') as csv_file:
#       settings = csv.reader(csv_file)
      
#       for line in settings:
#         print(line)

# if __name__ == "__main__":
#   multi_language = MultiLanguage()

