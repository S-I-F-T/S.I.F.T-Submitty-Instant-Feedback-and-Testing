import subprocess
import time
import exceptiongroup
import os

path = os.path.join(r"C:\Users\ahmad\Desktop\OneDrive - Rensselaer Polytechnic Institute\RPI(S24)\psoft\homeworks\hw0\src\test\java\hw0\BallTest.java")

cmd = ['javac', path]

subprocess.run(cmd)
