from tkinter import *

root = Tk()


root.geometry("800x600")
root.title("S.I.F.T")
root.config(bg="#343434")


label = Label(root, text="How to use", font=('Arial', 50), bg="#343434")
label.pack(padx=10, pady=10)


description1 = StringVar()
paragraph1 = Label(root, textvariable=description1, font=('Arial', 30), width=40, bg="#343434", justify="left")
description1.set(
"""SIFT allows users to auto-grade their homework
assignments without fear of wasting submissions
and waiting for Submitty servers to process code""")
paragraph1.pack(padx=10, pady=5)

description2 = StringVar()
paragraph2 = Label(root, textvariable=description2, font=('Arial', 25),justify="left", bg="#343434")
description2.set(
"""To use SIFT, navigate to the Autograder page and
input your own code, as well as the expected output
files for the assignment
    Once you press the “Compare Output” button,
SIFT will run your code and compare it against the
expected output files provided
The comparison will highlight discrepancies between
the output of the provided code and the expected 
output for easy bug finding and fixing""")
paragraph2.pack(padx=10, pady=10)

#insert back button for to go back to main page

root.mainloop()