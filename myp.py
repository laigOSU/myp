
# Import random module to generate random strings 
import random
import string

randomString = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
print randomString

# https://pythontips.com/2013/07/28/generating-a-random-string/
# https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa



# Generate random integer
# http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
