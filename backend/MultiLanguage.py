import json
import os
import subprocess

class MultiLanguage:
  def __init__(self):
    language = language

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

  @staticmethod 
  def run_cpp_file(filepath):
    output_file = filepath.replace(".cpp", ".exe")
    arguments = ""

    subprocess.run(["g++", os.path.abspath("test/helloworld.cpp"), "-o", "helloworld.exe"], check=True)
    subprocess.run(["./" + output_file, arguments])

# subprocess.run(["g++", os.path.abspath("test/helloworld.cpp"), "-o", "helloworld.exe"], check=True, shell=True)
# print(MultiLanguage.language)
try:
  MultiLanguage.run_cpp_file("test/helloworld.cpp")
except subprocess.CalledProcessError as e:
  raise RuntimeError("command '{}' return with error (code {}): {}".format(e.cmd, e.returncode, e.output))

# print(os.path.abspath("test/helloworld.cpp"))