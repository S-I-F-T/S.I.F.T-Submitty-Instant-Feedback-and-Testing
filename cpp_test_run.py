'''
Autho: Ayaan Ahmad


'''


import subprocess
import time
import exceptiongroup
import os

path = os.path.join(r"C:\Users\ahmad\Desktop\OneDrive - Rensselaer Polytechnic Institute\RPI(S24)\intro_rcos\S.I.F.T-Submitty-Instant-Feedback-and-Testing\testing_CPP\hw1.cpp")

cmd = ['g++ -g -Wall -Wextra -o hw1.exe ', path]


try:
    subprocess.run(cmd)

except subprocess.CalledProcessError as e:
    print("Error: ", e)
    print("Error code: ", e.returncode)
    print("Error output: ", e.output)
