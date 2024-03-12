from tkinter import *

root = Tk()


root.geometry("800x600")
root.title("S.I.F.T")
root.config(bg="#343434")


label = Label(root, text="About", font=('Arial', 50), bg="#343434")
label.pack(padx=10, pady=10)


description1 = StringVar()
paragraph1 = Label(root, textvariable=description1, font=('Arial', 20), bg="#343434", justify="left")
description1.set(
"""SIFT (Submitty Instant Feedback and Testing) is a standalone auto-grader 
for coding homework assignments to help students test their code effectively 
without relying on Submitty servers""")
paragraph1.pack(padx=10, pady=5)

description2 = StringVar()
paragraph2 = Label(root, textvariable=description2, font=('Arial', 25),justify="left", bg="#343434")
description2.set(
"""Created by Abedalah Safi, Abrar Zaki, Ayaan Ahmad, and Josh Javillo""")
paragraph2.pack(padx=10, pady=10)

description3 = StringVar()
paragraph3 = Label(root, textvariable=description3, font=('Arial', 25),justify="left", bg="#343434")
description3.set(
"""MIT License
Copyright (c) 2024 S.I.F.T v0.0.1""")
paragraph3.pack(padx=0, pady=10)

#insert back button for to go back to main page

root.mainloop()