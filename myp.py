import random   # Import random module to generate random strings
import string   # Import string module for strings
import sys      # Import sys for sys.stdout.write()

# Open (create) 3 files and write into them
# https://www.guru99.com/reading-and-writing-files-in-python.html

file_1 = open("file1", "w+")
file_2 = open("file2", "w+")
file_3 = open("file3", "w+")
allFiles = [file_1, file_2, file_3]

# For Loops
# http://www.pythonforbeginners.com/loops/for-while-and-nested-loops-in-python
# for myFile in allFiles:
#     # Generate Random String
#     # https://pythontips.com/2013/07/28/generating-a-random-string/
#     # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
#     randomString = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
#     # Print each random string consecutively
#     print randomString
#     # Concatenate 11th character to random string and save into files
#     # http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
#     randomString = randomString + "\n"
#     myFile.write(randomString)
#     myFile.close()


# Python knows when for loop ends by indentation
for myFile in allFiles:
    # Generate Random String
    # https://pythontips.com/2013/07/28/generating-a-random-string/
    # https://stackoverflow.com/questions/2257441/random-string-generation-with-upper-case-letters-and-digits-in-python?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    randomString = ''.join(random.choice(string.ascii_lowercase) for n in range(10))
    # Concatenate 11th character to random string and save into files
    # http://www.pythonforbeginners.com/concatenation/string-concatenation-and-formatting-in-python
    randomString = randomString + "\n"
    # Print each random string consecutively
    # https://stackoverflow.com/questions/3263672/the-difference-between-sys-stdout-write-and-print?utm_medium=organic&utm_source=google_rich_qa&utm_campaign=google_rich_qa
    sys.stdout.write(randomString)
    # Write string + \n to each file
    myFile.write(randomString)
    myFile.close()


# Generate random integer
# http://www.pythonforbeginners.com/random/how-to-use-the-random-module-in-python
