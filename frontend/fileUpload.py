# import tkinter as tk
from tkinter import *
from tkinter import filedialog

def browseFiles():
    filename = filedialog.askopenfilename(initialdir = "/",
                                          title = "Select a File",
                                          filetypes = (("Text files",
                                                        "*.txt*"),
                                                       ("all files",
                                                        "*.*")))
      
    # Change label contents
    label_file_explorer.configure(text="File Opened: "+filename)

root = Tk()


root.geometry("800x600")
root.title("S.I.F.T")
root.config(bg="#343434")




label = Label(root, text="File Upload", font=('Arial', 18), bg="#343434")
label.pack(padx=10, pady=20)

label_file_explorer = Label(root, 
							text = "File Explorer using Tkinter",
							width = 100, height = 4, 
							fg = "blue")

	
button_explore = Button(root, 
						text = "Browse Files",
						command = browseFiles) 




# contentFrame = tk.Frame(root)
# contentFrame.columnconfigure(0, weight=1)
# contentFrame.columnconfigure(1, weight=1)

# rando = tk.Label(contentFrame, text="Test", font=('Arial', 18), bg="#000")
# rando.grid(row=0,column=0)

# textbox1 = tk.Text(contentFrame, height=3, font=('Arial',16))
# textbox1.grid(row=1,column=0,sticky=tk.W+tk.E)

# textbox2 = tk.Text(contentFrame, height=3, font=('Arial',16))
# textbox2.grid(row=1,column=1,sticky=tk.W+tk.E)



root.mainloop()

