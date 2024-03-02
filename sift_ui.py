import customtkinter as ctk

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('640x480')
root.configure(bg="#343434")

# Function to switch between frames
def switch_frame(frame_name):
    global current_frame
    if current_frame != frame_name:
        # Get the frame objects using their names
        current_frame_obj = globals()[current_frame]  # Access the frame as a global variable
        new_frame_obj = globals()[frame_name]       # Access the frame as a global variable

        # Hide the current frame
        current_frame_obj.pack_forget()

        # Show the new frame
        new_frame_obj.pack(fill='both', expand=True)

        current_frame = frame_name

# Welcome page
current_frame = "welcome_frame"

welcome_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

welcome_title = ctk.CTkLabel(master = welcome_frame, text = 'Welcome to SIFT', 
                     font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
welcome_title.pack(pady = 12, padx = 10)

button_frame_1 = ctk.CTkFrame(master= welcome_frame, fg_color="#343434", bg_color="#343434")
button_frame_1.pack(pady=12, padx=10)

autograder_button = ctk.CTkButton(master = button_frame_1, text = "Autograder",
                                  font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                  fg_color="#575757", width = 255, height = 55, 
                                  command = lambda: switch_frame('autograder_frame'))
autograder_button.pack(side=ctk.LEFT, padx=15)

how_to_button = ctk.CTkButton(master = button_frame_1, text = "How to Use", 
                              font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                              fg_color="#575757", width = 255, height = 55)
how_to_button.pack(side=ctk.RIGHT, padx=15)

button_frame_2 = ctk.CTkFrame(master= welcome_frame, fg_color="#343434", bg_color="#343434")
button_frame_2.pack(pady=12, padx=10)

about_button = ctk.CTkButton(master = button_frame_2, text = "About",
                             font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                             fg_color="#575757", width = 255, height = 55)
about_button.pack(side=ctk.LEFT, padx=15)

settings_button = ctk.CTkButton(master = button_frame_2, text = "Settings",
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                fg_color="#575757", width = 255, height = 55)
settings_button.pack(side=ctk.RIGHT, padx=15)

# Autograder page
autograder_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

autograder_title_frame = ctk.CTkFrame(master = autograder_frame, fg_color="#343434", bg_color="#343434")
autograder_title_frame.pack(pady=12, padx=10)

your_files_title = ctk.CTkLabel(master = autograder_title_frame, text = 'Your file(s)', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
your_files_title.pack(side=ctk.LEFT, padx=10)

expected_files_title = ctk.CTkLabel(master = autograder_title_frame, text = 'Expected output file(s)', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
expected_files_title.pack(side=ctk.RIGHT, padx=200)

autograder_back_button = ctk.CTkButton(master = autograder_frame, text = "Back", 
                                       font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"), 
                                       fg_color="#575757", width =100, height = 40, 
                                       command = lambda: switch_frame('welcome_frame'))
autograder_back_button.pack(side=ctk.BOTTOM, pady=10)

welcome_frame.pack(fill = 'both', expand = True)

root.mainloop()