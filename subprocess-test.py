import subprocess
import time
import os

path = os.path.join("javaTestingSite")

cmd = ['java ', ' -jar', path]

subprocess.run(cmd)
