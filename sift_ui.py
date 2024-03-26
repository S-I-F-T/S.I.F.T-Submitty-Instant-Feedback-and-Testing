import customtkinter as ctk
from customtkinter import filedialog

def select_user_file(user_files):
        """
        @param user_files: list of user files
        
        This function allows the user to select their file(s) 
        and appends the file path to the user_files list.
        """
        file_types = [("Python Files", "*.py"), 
                  ("Java Files", "*.java"), 
                  ("C++ Files", "*.cpp")]
        filename = filedialog.askopenfilename(filetypes=file_types)
        user_files.append(filename)
        
        # Update user files label
        user_files_text = "\n".join(userfiles) if userfiles else "No files selected"
        your_files.configure(text=user_files_text)


    
def select_expected_file(expected_files):
    """
    @param expected_files: list of expected files
    
    This function allows the user to select the expected output file(s)
    """
    filename = filedialog.askopenfilename()
    expected_files.append(filename)

    # Update expected files label
    expected_files_text = "\n".join(expectedfiles) if expectedfiles else "No files selected"
    expected_files_label.configure(text=expected_files_text)

# Function to switch between frames
def switch_frame(frame_name):
    """
    @param frame_name: name of the frame to switch to
    
    This function switches between frames in the UI.
    """
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

ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('640x480')
root.configure(bg="#343434")

userfiles = []
expectedfiles = []

# Welcome page
current_frame = "welcome_frame"

welcome_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

welcome_title = ctk.CTkLabel(master = welcome_frame, text = 'Welcome to SIFT', 
                     font = ctk.CTkFont(family='Calibri', size = 30, weight = "bold"))
welcome_title.pack(pady = 12, padx = 10)

button_frame_1 = ctk.CTkFrame(master= welcome_frame, fg_color="#343434", bg_color="#343434")
button_frame_1.pack(pady = 12, padx = 10)

autograder_button = ctk.CTkButton(master = button_frame_1, text = "Autograder",
                                  font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                  fg_color = "#575757", width = 255, height = 55, 
                                  command = lambda: switch_frame('file_select_frame'))
autograder_button.pack(side=ctk.LEFT, padx = 15)

how_to_button = ctk.CTkButton(master = button_frame_1, text = "How to Use", 
                              font = ctk.CTkFont(family = 'Calibri', size = 15, weight = "bold"),
                              fg_color="#575757", width = 255, height = 55, command = lambda: switch_frame('how_to_frame'))

how_to_button.pack(side=ctk.RIGHT, padx = 15)

button_frame_2 = ctk.CTkFrame(master= welcome_frame, fg_color="#343434", bg_color="#343434")
button_frame_2.pack(pady = 12, padx = 10)

about_button = ctk.CTkButton(master = button_frame_2, text = "About",
                             font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                             fg_color="#575757", width = 255, height = 55, command = lambda: switch_frame('about_frame'))
about_button.pack(side=ctk.LEFT, padx = 15)

settings_button = ctk.CTkButton(master = button_frame_2, text = "Settings",
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                fg_color="#575757", width = 255, height = 55, command = lambda: switch_frame('settings_frame'))
settings_button.pack(side=ctk.RIGHT, padx = 15)

quit_frame = ctk.CTkFrame(master = welcome_frame, fg_color="#343434", bg_color="#343434")
quit_frame.pack(pady = 12, padx = 10)

quit_button = ctk.CTkButton(master = quit_frame, text = "Quit",
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                fg_color="#575757", width = 255, height = 55, command = root.quit)
quit_button.pack(side=ctk.BOTTOM, pady = 10)

# File select page
file_select_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

file_select_big_title_frame = ctk.CTkFrame(master = file_select_frame, fg_color="#343434", bg_color="#343434")
file_select_big_title_frame.pack(pady = 12, padx = 10)

file_select_big_title = ctk.CTkLabel(master = file_select_big_title_frame, text = 'File select',
                                          font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
file_select_big_title.pack(pady = 0, padx = 10)

file_select_title_frame = ctk.CTkFrame(master = file_select_frame, fg_color="#343434", bg_color="#343434")
file_select_title_frame.pack(pady = 0, padx = 10)

your_files_title = ctk.CTkLabel(master = file_select_title_frame, text = 'Your file(s)', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
your_files_title.pack(side=ctk.LEFT, padx = 50)

expected_files_title = ctk.CTkLabel(master = file_select_title_frame, text = 'Expected output file(s)', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
expected_files_title.pack(side=ctk.RIGHT, padx = 150)

file_select_choose_frame = ctk.CTkFrame(master = file_select_frame, fg_color="#343434", bg_color="#343434")
file_select_choose_frame.pack(pady = 12, padx = 10)

your_files_button = ctk.CTkButton(master = file_select_choose_frame, text = "Select your file(s)", 
                                  font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                  fg_color="#575757", width = 255, height = 55, command = lambda: select_user_file(userfiles))
your_files_button.pack(side=ctk.LEFT, padx = 15)

expected_files_button = ctk.CTkButton(master = file_select_choose_frame, text = "Select expected output file(s)",
                                        font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                        fg_color="#575757", width = 255, height = 55, command = lambda: select_expected_file(expectedfiles))
expected_files_button.pack(side=ctk.RIGHT, padx = 15)

your_files_frame = ctk.CTkFrame(master = file_select_frame, fg_color="#343434", bg_color="#343434")
your_files_frame.pack(pady = 12, padx = 30, side = ctk.LEFT)

your_files = ctk.CTkLabel(master = your_files_frame, text = 'No files selected', font = ctk.CTkFont(family='Calibri', size=12))
your_files.pack(pady = 5)

expected_files_frame = ctk.CTkFrame(master = file_select_frame, fg_color="#343434", bg_color="#343434")
expected_files_frame.pack(pady = 12, padx = 10, side = ctk.RIGHT)

expected_files_label = ctk.CTkLabel(master = expected_files_frame, text = 'No files selected', font = ctk.CTkFont(family='Calibri', size=12))
expected_files_label.pack(pady = 5)

file_select_back_button = ctk.CTkButton(master = file_select_frame, text = "Back", 
                                       font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"), 
                                       fg_color="#575757", width = 100, height = 40, 
                                       command = lambda: switch_frame('welcome_frame'))
file_select_back_button.pack(side=ctk.BOTTOM, pady = 10)

file_select_compare_button = ctk.CTkButton(master = file_select_frame, text = "Compare",
                                            font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                            fg_color="#575757", width = 100, height = 40, command= lambda: switch_frame('comparison_frame'))
file_select_compare_button.pack(side=ctk.BOTTOM, pady = 10)

# Comparison page
comparison_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

comparison_title_frame = ctk.CTkFrame(master = comparison_frame, fg_color="#343434", bg_color="#343434")
comparison_title_frame.pack(pady = 12, padx = 10)

comparison_title = ctk.CTkLabel(master = comparison_title_frame, text = 'Comparison',
                                font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
comparison_title.pack(pady = 12, padx = 10)

comparison_title_frame = ctk.CTkFrame(master = comparison_frame, fg_color="#343434", bg_color="#343434")
comparison_title_frame.pack(pady = 12, padx = 10)

your_output_title = ctk.CTkLabel(master = comparison_title_frame, text = 'Your output', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
your_output_title.pack(side=ctk.LEFT, padx = 50)

expected_output_title = ctk.CTkLabel(master = comparison_title_frame, text = 'Expected output', font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
expected_output_title.pack(side=ctk.RIGHT, padx = 150)

comparison_back_button = ctk.CTkButton(master = comparison_frame, text = "Back", 
                                       font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"), 
                                       fg_color="#575757", width = 100, height = 40, 
                                       command = lambda: switch_frame('file_select_frame'))
comparison_back_button.pack(side=ctk.BOTTOM, pady = 10)

# Settings page
settings_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

settings_title = ctk.CTkLabel(master = settings_frame, text = 'Settings',
                                font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
settings_title.pack(pady = 12, padx = 10)

settings_language_frame = ctk.CTkFrame(master = settings_frame, fg_color="#343434", bg_color="#343434")
settings_language_frame.pack(pady = 12, padx = 10)

settings_language_label = ctk.CTkLabel(master = settings_language_frame, text = 'Language:',
                                        font = ctk.CTkFont(family='Calibri', size=20, weight = "bold"))
settings_language_label.pack(side=ctk.LEFT, padx = 50)

settings_language_dropdown = ctk.CTkOptionMenu(master = settings_language_frame, values = ['Python', 'Java', 'C++'],
                                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
settings_language_dropdown.pack(side=ctk.RIGHT, padx = 150)

settings_theme_frame = ctk.CTkFrame(master = settings_frame, fg_color="#343434", bg_color="#343434")
settings_theme_frame.pack(pady = 12, padx = 10)

settings_theme_label = ctk.CTkLabel(master = settings_theme_frame, text = 'Theme:',
                                    font = ctk.CTkFont(family='Calibri', size=20, weight = "bold"))
settings_theme_label.pack(side=ctk.LEFT, padx = 60)

settings_theme_dropdown = ctk.CTkOptionMenu(master = settings_theme_frame, values = ['Dark', 'Light'],
                                            font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
settings_theme_dropdown.pack(side=ctk.RIGHT, padx = 150)

settings_back_button = ctk.CTkButton(master = settings_frame, text = "Back",
                                          font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                          fg_color="#575757", width = 100, height = 40, 
                                          command = lambda: switch_frame('welcome_frame'))
settings_back_button.pack(side=ctk.BOTTOM, pady = 10)

# About page
about_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

about_title = ctk.CTkLabel(master = about_frame, text = 'About SIFT',
                           font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
about_title.pack(padx=10, pady=10)

description1 = """SIFT (Submitty Instant Feedback and Testing) is a standalone auto-grader
for coding homework assignments to help students test their code
effectively without relying on Submitty servers"""
about_paragraph1 = ctk.CTkLabel(master = about_frame, text = description1,
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
about_paragraph1.pack(padx=10, pady=5)

description2 = "Created by Abedalah Safi, Abrar Zaki, Ayaan Ahmad, and Josh Javillo"
about_paragraph2 = ctk.CTkLabel(master = about_frame, text = description2,
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
about_paragraph2.pack(padx=10, pady=5)

description3 = """MIT License
Copyright (c) 2024 S.I.F.T v0.0.1"""
about_paragraph3 = ctk.CTkLabel(master = about_frame, text = description3,
                                font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"))
about_paragraph3.pack(padx=10, pady=5)

about_back_button = ctk.CTkButton(master = about_frame, text = "Back",
                                        font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                        fg_color="#575757", width = 100, height = 40, 
                                        command = lambda: switch_frame('welcome_frame'))
about_back_button.pack(side=ctk.BOTTOM, pady = 10)

# How to use page
how_to_frame = ctk.CTkFrame(master = root, fg_color="#343434", bg_color="#343434")

how_to_title = ctk.CTkLabel(master = how_to_frame, text = 'How to Use SIFT',
                                font = ctk.CTkFont(family='Calibri', size=30, weight = "bold"))
how_to_title.pack(padx=10, pady=10)

ht_description1 = """SIFT allows users to auto-grade their homework assignments without
fear of wasting submissions and waiting for Submitty servers to process code"""
how_to_paragraph1 = ctk.CTkLabel(master = how_to_frame, text = ht_description1, font = ctk.CTkFont(family='Calibri', size=17, weight = "bold"))

how_to_paragraph1.pack(padx=10, pady=5)

ht_description2 = """To use SIFT, navigate to the Autograder page and input your own code, as well as 
the expected output files for the assignment. Once you press the “Compare Output”
button, SIFT will run your code and compare it against the expected output files 
provided. The comparison will highlight discrepancies between the output of the 
provided code and the expected output for easy bug finding and fixing"""
paragraph2 = ctk.CTkLabel(master = how_to_frame, text=ht_description2, font = ctk.CTkFont(family='Calibri', size=17, weight = "bold"))

paragraph2.pack(padx=10, pady=10)

how_to_back_button = ctk.CTkButton(master = how_to_frame, text = "Back",
                                        font = ctk.CTkFont(family='Calibri', size=15, weight = "bold"),
                                        fg_color="#575757", width = 100, height = 40, 
                                        command = lambda: switch_frame('welcome_frame'))
how_to_back_button.pack(side=ctk.BOTTOM, pady = 10)

# Pack the welcome frame
welcome_frame.pack(fill = 'both', expand = True)

root.mainloop()