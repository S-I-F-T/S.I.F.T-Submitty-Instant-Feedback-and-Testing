"""
Created on Mon Sep 12 14:13:06 2022

@author: abzak

This program asks the user for a character, a height dimesnion,
and a width dimension. Then using those values, it prints a box
of those dimensions using the given character and prints the
dimensions, centered inside the box
"""
#  Asking user for inputs
frame_character = str(input("Enter frame character ==> ")).strip('\r')
print(frame_character)

box_height = input("Height of box ==> ").strip('\r')
print(box_height)
box_height = int(box_height)

box_width = input("Width of box ==> ").strip('\r')
print(box_width)
box_width = int(box_width)

# Creating variables to be used in calculations
dimensions = str(box_width) + "x" + str(box_height)
inner_width = box_width - 2
inner_height = box_height - 2
num_vblank = inner_height - 1
num_top = num_vblank // 2
num_bot = num_vblank - num_top
dim_width = len(dimensions)
num_hblank = inner_width - dim_width
num_left = num_hblank // 2
num_right = num_hblank - num_left

# Calculations using variables
end_line = "\n" + (frame_character * box_width)
mid_line = "\n" + frame_character + (" " * num_left) + dimensions + (" " * num_right) + frame_character
side_line = "\n" + frame_character + (" " * inner_width) + frame_character

# Printing output
print("\nBox:" + end_line + (side_line * num_top) + mid_line + (side_line * num_bot) + end_line)