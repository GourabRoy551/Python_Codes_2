"""
Regular Expressions (RegEx) are used to
1. Search for a specific string in a large amount of data
2. Verify that a string has the proper format (Email, Phone #)
3. Find a string and replace it with another string
4. Format data into the proper form for importing for example
"""

# import the Regex module
import re

#--------Was a Match Found-----------

# Search for ape in the string
if re.search("ape", "The ape was at the apex"):
    print("There is an ape")

# -----------Get All Matches---------
# findall() returns a list of Matches
# . is used to match any 1 character or space
allApes = re.findall("ape.", "The ape was at the apex")

for i in allApes:
    print(i)

# finditer returns an iterator of matching an objects
# We can use span to get the location

theStr = "The ape was at the apex"

for i in re.finditer("ape.", theStr):
        # span returns a tuple
        locTuple = i.span()

        print(locTuple)

        # Slice the match out using the tuple values
        print(theStr[locTuple[0]:locTuple[1]])

# ------------Match 1 of Several Letters --------------

# Square brackets will match any one of the characters between
# the brackets not including upper and Lowercase varieties
# unless they are listed

animalStr = "Cat rat mat fat pat"

allAnimals = re.findall("[crmfp]at", animalStr)
for i in allAnimals:
    print(i)

print()

# Use ^ to denote any character but whatever characters are
# between the brackets

someAnimals = re.findall("[^Cr]at", animalStr)
for i in someAnimals:
    print(i)

print()

# -------Replace All Matches ------

# Replace matching items in a string

owlFood = "rat cat mat pat"

# You can compile a regex into pattern objects which
# provide additional string passed to sub
regex = re.compile("[cr]at")

# sub() replaces items that match the regex in the string
# with the 1st attribute string passed to sub
owlFood = regex.sub("owl", owlFood)

print(owlFood)



# -------- Solving Backlash Problems -----------

# Regex use the backlash to designate spacial characters
# and Python does the same inside string which causes
# issues

# Let's try to get "\\stuff" out of a string

randStr = "Here is \\stuff"

# This won't find it
print("Find \\stuff : ", re.search("\\stuff", randStr))

# This does, but we have to put in 4 slashes which is messy
print("Find \\stuff : ", re.search("\\\\stuff", randStr))

# We can get around this by using raw strings which
# don't treat backslashes as special
print("Find \\stuff: ", re.search(r"\\stuff", randStr))

'''
Output:
    Find \stuff :  None
    Find \stuff :  <re.Match object; span=(8, 14), match='\\stuff'>
    Find \stuff:  <re.Match object; span=(8, 14), match='\\stuff'>

'''


# ------------Matching Whitespace -----------
# We can match many whitespace characters

randStr = """This is a long
string that goes
on for many lines"""

print(randStr)

# Remove newlines
regex = re.compile("\n")

randStr = regex.sub(" ", randStr)

print(randStr)

# We can also match
# \b : Backspace
# \f : Form Feed
# \r : Carriage Return
# \t : Tab
# \v : Vertical Tab
# To remove \r \n on Windows