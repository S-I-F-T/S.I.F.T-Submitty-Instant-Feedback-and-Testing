# S.I.F.T-Submitty-Instant-Feedback-and-Testing
S.I.F.T, stading for Submitty Instant-Feedback and Testing is an application separate from Submitty, that allows students to locally run Submitty autograding tests without the worry about going over the limit. Plus, it will be faster as it is done on the user's local device


Research (01/30/2024)
----------------------
1. Python has a library called subprocess, which could be used to run commands. We could use this to run code that the user uploads. 
2. For instance, if the user uploads a Java file, we could run the command `javac <filename>` to compile the file. Then, we could run the command `java <filename>` to run the file.   


Research (02/06/2024)
----------------------
1. Working with Abedalah Safi, I will recording and researching while he will be coding as well as researching.
2. We had an error with running java code in Windows because of how windows treats / in directories. We fixed this by using os.path.join() to join the directory and file name together. This i believe works for both Windows and Unix systems.
3. We also need to use 'r' to so that python knows that it is a raw string.


Research (02/27/2024)
---------------------
1. Ran CPP with subprocess module. We used custom arguments as well

2. We can get stdout and sterr