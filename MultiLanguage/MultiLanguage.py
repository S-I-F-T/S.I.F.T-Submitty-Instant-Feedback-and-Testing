import json

class MultiLanguage():
  def __init__(self):
    with open("sifttings", "r") as j:
      data = json.load(j)
      
      print(data)

if __name__ == "__main__":
  multi_language = MultiLanguage()

