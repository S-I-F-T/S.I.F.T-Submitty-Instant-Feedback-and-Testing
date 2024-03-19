import customtkinter as ctk
from customtkinter import filedialog    

# Function to select user file
def select_user_file(user_files):
    filename = filedialog.askopenfilename()
    user_files.append(filename)

# Function to select expected file
def select_expected_file(expected_files):
    filename = filedialog.askopenfilename()
    expected_files.append(filename)

# Function to switch between frames
def switch_frame(frame_name):
    global current_frame
    if current_frame != frame_name:
        current_frame_obj = globals()[current_frame]
        new_frame_obj = globals()[frame_name]

        current_frame_obj.pack_forget()
        new_frame_obj.pack(fill='both', expand=True)

        current_frame = frame_name

# Function to create button with given properties
def create_button(master, text, font, fg_color, width, height, command):
    return ctk.CTkButton(master=master, text=text, font=font, fg_color=fg_color, width=width, height=height, command=command)

# Function to create label with given properties
def create_label(master, text, font):
    return ctk.CTkLabel(master=master, text=text, font=font)

# Function to create frame with given properties
def create_frame(master, fg_color, bg_color):
    return ctk.CTkFrame(master=master, fg_color=fg_color, bg_color=bg_color)

# Function to create option menu with given properties
def create_option_menu(master, values, font):
    return ctk.CTkOptionMenu(master=master, values=values, font=font)

# Initialize appearance mode and color theme
ctk.set_appearance_mode('dark')
ctk.set_default_color_theme('dark-blue')

root = ctk.CTk()
root.geometry('640x480')
root.configure(bg="#343434")

# Define current_frame
current_frame = "welcome_frame"

# Initialize welcome frame
welcome_frame = create_frame(root, "#343434", "#343434")

# Initialize welcome frame components
welcome_title = create_label(welcome_frame, 'Welcome to SIFT', ctk.CTkFont(family='Calibri', size=30, weight="bold"))
button_frame_1 = create_frame(welcome_frame, "#343434", "#343434")
button_frame_2 = create_frame(welcome_frame, "#343434", "#343434")

# Initialize buttons in welcome frame
autograder_button = create_button(button_frame_1, "Autograder", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, lambda: switch_frame('file_select_frame'))
how_to_button = create_button(button_frame_1, "How to Use", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, None)
about_button = create_button(button_frame_2, "About", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, None)
settings_button = create_button(button_frame_2, "Settings", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, lambda: switch_frame('settings_frame'))

# Pack components in welcome frame
welcome_title.pack(pady=12, padx=10)
button_frame_1.pack(pady=12, padx=10)
autograder_button.pack(side=ctk.LEFT, padx=15)
how_to_button.pack(side=ctk.RIGHT, padx=15)
button_frame_2.pack(pady=12, padx=10)
about_button.pack(side=ctk.LEFT, padx=15)
settings_button.pack(side=ctk.RIGHT, padx=15)

# Initialize file select frame
file_select_frame = create_frame(root, "#343434", "#343434")

# Initialize file select frame components
file_select_title_frame = create_frame(file_select_frame, "#343434", "#343434")
file_select_choose_frame = create_frame(file_select_frame, "#343434", "#343434")

# Initialize labels and buttons in file select frame
your_files_title = create_label(file_select_title_frame, 'Your file(s)', ctk.CTkFont(family='Calibri', size=15, weight="bold"))
expected_files_title = create_label(file_select_title_frame, 'Expected output file(s)', ctk.CTkFont(family='Calibri', size=15, weight="bold"))
your_files_button = create_button(file_select_choose_frame, "Select your file(s)", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, lambda: select_user_file(userfiles))
expected_files_button = create_button(file_select_choose_frame, "Select expected output file(s)", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 255, 55, lambda: select_expected_file(expectedfiles))

# Pack components in file select frame
file_select_title_frame.pack(pady=12, padx=10)
your_files_title.pack(side=ctk.LEFT, padx=50)
expected_files_title.pack(side=ctk.RIGHT, padx=150)
file_select_choose_frame.pack(pady=12, padx=10)
your_files_button.pack(side=ctk.LEFT, padx=15)
expected_files_button.pack(side=ctk.RIGHT, padx=15)

# Initialize comparison frame
comparison_frame = create_frame(root, "#343434", "#343434")

# Initialize comparison frame components
comparison_title_frame = create_frame(comparison_frame, "#343434", "#343434")

# Initialize labels in comparison frame
comparison_title = create_label(comparison_title_frame, 'Comparison', ctk.CTkFont(family='Calibri', size=30, weight="bold"))
your_output_title = create_label(comparison_title_frame, 'Your output', ctk.CTkFont(family='Calibri', size=15, weight="bold"))
expected_output_title = create_label(comparison_title_frame, 'Expected output', ctk.CTkFont(family='Calibri', size=15, weight="bold"))

# Pack components in comparison frame
comparison_title_frame.pack(pady=12, padx=10)
comparison_title.pack(pady=12, padx=10)
your_output_title.pack(side=ctk.LEFT, padx=50)
expected_output_title.pack(side=ctk.RIGHT, padx=150)


# Initialize autograder frame
autograder_frame = create_frame(root, "#343434", "#343434")

# Initialize autograder frame components
autograder_title_frame = create_frame(autograder_frame, "#343434", "#343434")
autograder_title_frame.pack(pady=12, padx=10)
autograder_button_frame = create_frame(autograder_frame, "#343434", "#343434")
autograder_button_frame.pack(pady=12, padx=10)

# Initialize autograder frame labels and buttons
autograder_title = create_label(autograder_title_frame, 'Autograder', ctk.CTkFont(family='Calibri', size=30, weight="bold"))
autograder_back_button = create_button(autograder_button_frame, "Back", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 100, 40, lambda: switch_frame('welcome_frame'))

# Pack components in autograder frame
autograder_title.pack(pady=12, padx=10)
autograder_back_button.pack(side=ctk.BOTTOM, pady=10)



# Initialize settings frame
settings_frame = create_frame(root, "#343434", "#343434")

# Initialize settings frame components
settings_language_frame = create_frame(settings_frame, "#343434", "#343434")
settings_theme_frame = create_frame(settings_frame, "#343434", "#343434")

# Initialize labels, buttons, and option menu in settings frame
settings_title = create_label(settings_frame, 'Settings', ctk.CTkFont(family='Calibri', size=30, weight="bold"))
settings_language_label = create_label(settings_language_frame, 'Language:', ctk.CTkFont(family='Calibri', size=20, weight="bold"))
settings_language_dropdown = create_option_menu(settings_language_frame, ['Python', 'Java', 'C++'], ctk.CTkFont(family='Calibri', size=15, weight="bold"))
settings_theme_label = create_label(settings_theme_frame, 'Theme:', ctk.CTkFont(family='Calibri', size=20, weight="bold"))
settings_theme_dropdown = create_option_menu(settings_theme_frame, ['Dark', 'Light'], ctk.CTkFont(family='Calibri', size=15, weight="bold"))
settings_back_button = create_button(settings_frame, "Back", ctk.CTkFont(family='Calibri', size=15, weight="bold"), "#575757", 100, 40, lambda: switch_frame('welcome_frame'))

# Pack components in settings frame
settings_title.pack(pady=12, padx=10)
settings_language_frame.pack(pady=12, padx=10)
settings_language_label.pack(side=ctk.LEFT, padx=50)
settings_language_dropdown.pack(side=ctk.RIGHT, padx=150)
settings_theme_frame.pack(pady=12, padx=10)
settings_theme_label.pack(side=ctk.LEFT, padx=50)
settings_theme_dropdown.pack(side=ctk.RIGHT, padx=150)
settings_back_button.pack(side=ctk.BOTTOM, pady=10)

# Pack welcome frame and start main loop
welcome_frame.pack(fill='both', expand=True)
root.mainloop()
