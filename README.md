# S.I.F.T-Submitty-Instant-Feedback-and-Testing
S.I.F.T, stading for Submitty Instant-Feedback and Testing is an application separate from Submitty, that allows students to locally run Submitty autograding tests without the worry about going over the limit. Plus, it will be faster as it is done on the user's local device


Research (01/30/2024)
----------------------
1. Python has a library called subprocess, which could be used to run commands. We could use this to run code that the user uploads. 
2. For instance, if the user uploads a Java file, we could run the command `javac <filename>` to compile the file. Then, we could run the command `java <filename>` to run the file.   