"""
distribution.py
Author: Emma Dunbar
Credit: StackOverflow, Python Software Foundation, W3schools, Geoff Dunbar

Assignment:

Write and submit a Python program (distribution.py) that computes and displays 
the distribution of characters in a given sample of text.

Output of your program should look like this:

Please enter a string of text (the bigger the better): The rain in Spain stays mainly in the plain.
The distribution of characters in "The rain in Spain stays mainly in the plain." is:
iiiiii
nnnnnn
aaaaa
sss
ttt
ee
hh
ll
pp
yy
m
r

Notice about this example:

* The text: 'The rain ... plain' is provided by the user as input to your program.
* Uppercase characters are converted to lowercase
* Spaces and punctuation marks are ignored completely.
* Characters that are more common appear first in the list.
* Where the same number of characters occur, the lines are ordered alphabetically. 
  For example, in the printout above, the letters e, h, l, p and y both occur twice 
  in the text and they are listed in the output in alphabetical order.
* Letters that do not occur in the text are not listed in the output at all.
"""
import string

l1=(input("Please enter a string of text (the bigger the better): "))
print("The distribution of characters in " + l1 + " is: ")
l1=([x.lower() for x in l1])
l2=list(string.punctuation)
space=(' ')
l3=[]
for i in l1:
    if (not i in l2) and (not i==space):
        l3=l3+[i]
l3.sort()
l4=sorted(l3, key=l3.count, reverse=True)
b=" "
for a in l4:
    if a==b:
        print(a, end='')
    else:
        if b!=" ":
            print('')
        print(a, end='')
    b=a
print('')



