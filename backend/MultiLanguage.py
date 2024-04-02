import json
import os
import subprocess

class MultiLanguage:
  @staticmethod
  def initializeLanguage():
    with open(os.path.abspath("backend/sifttings.json"), 'r') as json_file:
      settings = json.load(json_file)
      return settings['language']
    
  @staticmethod
  def initializeTheme():
    with open(os.path.abspath("backend/sifttings.json"), 'r') as json_file:
      settings = json.load(json_file)
      return settings['theme']
    
  language = initializeLanguage()
  theme = initializeTheme()
  actual_output = None
  expected_output = None

  # @staticmethod 
  # def run_cpp_file(filepath):

subprocess.run(["g++", os.path.abspath("test/helloworld.cpp"), "-o", "helloworld.exe"], check=True)
print(MultiLanguage.language)