# Creator: Malunga. 

# With example code, 
# Explain how to produce html output using python?

# Answer:
"""we can use python to produce html output by first import neccesary modules and libraries
in our code, that provide us with required instructions for manipulation of html documents and 
envoke web browser to display our output since html files are viewed by web browser."""


# Example code:

import html
import webbrowser

# defining function to display HTML output
def printweb():

# webbrowser object calling open function wich recieves string actual paramiter or argument 
# as a string mentioning file directory(absolute path) to where HTML file reside.
# for my local PC the file is in /home/thoko/Documents/Malunga_The_Dev/javaScript_trai/....

    webbrowser.open("/home/thoko/Documents/Malunga_The_Dev/javaScript_trai/javaScript.html")
    