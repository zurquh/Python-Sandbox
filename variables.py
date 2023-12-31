# A variable is a container for a value, which can be of various types

'''
This is a 
multiline comment
or docstring (used to define a functions purpose)
can be single or double quotes
'''

"""
VARIABLE RULES:
  - Variable names are case sensitive (name and NAME are different variables)
  - Must start with a letter or an underscore
  - Can have numbers but can not start with one
  no semicolon
"""

x = 1 #int 
y = 2.5 #float
name = 'john' #stir
is_cool = True #bool must have captial t or f 

# Multiple assignment 
x,y, name, is_cool = [1, 2.5, 'john', True]

#Basic math
a = x +y

#casting 
x = str(x)
y = int(y)
z = float(y)

print(type(x), z)
