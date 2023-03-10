# -*- coding: utf-8 -*-
"""hw4_carson_jenkins_ex_2.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1iNnVGvpLLIQlhCfX6S2SC59FQzNdPbIh
"""

'''
Homework 4, Exercise 2
Carson Jenkins
03/09/23
This program takes input from the clipbaord using pyperclip, and 
then parses through and finds any phone numbers and emails.
'''

import re
import pyperclip

clipboard = pyperclip.paste()
# searches clipboard for any phone numbers
# [0-9] is for searching for numbers
# {3} and {4} represent the amount of digits for that level
phone = re.findall("([0-9]{3}-[0-9]{3}-[0-9]{4})", clipboard) 
# searches clipboard for any emails
# [A-Za-z0-9] is searching for any letters or numbers
email = re.findall(r"([A-Za-z0-9]+@[A-Za-z0-9]+\.[a-zA-Z]*)", clipboard) 
# uses join method to combine the numbers and emails into one variable
result = "\n".join(n for n in phone) + "\n"+"\n".join(m for m in email)
# copys the results to the clipboard
pyperclip.copy(result)
print(pyperclip.paste())