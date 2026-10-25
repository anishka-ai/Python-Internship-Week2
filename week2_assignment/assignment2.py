#Assignment 2: Word Counter from Text File
#Aim: To count the number of words, lines, and characters in a text file.

import os

file_path=os.path.join(os.path.dirname(__file__), "sample.txt")

with open(file_path, "r", encoding= "utf-8") as file:
    text = file.read()

words = len(text.split())
lines = len(text.splitlines())
characters = len(text)

print("Text: ", repr(text))
print("Number of words:", words)
print("Number of lines:", lines)
print("Number of characters:", characters)
