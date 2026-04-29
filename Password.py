
# This script translates unsecured passwords into more secure ones by replacing characters with similar looking characters to 
# satisfy a minimum password strength requirement. For example, 'a' might be replaced with '@', 's' with '$', etc.
# The letter mapping is read from a file passwordReplacement.txt, applies the replacements, and  
# writes the secure passwords to an output file.




import random
from pathlib import Path

# Get the directory where this script is located
script_dir = Path(__file__).parent

input = script_dir / 'input.txt'
output = script_dir / 'output.txt'
replacements_file = script_dir / 'passwordReplacement.txt'

# Puts letters to search for in the "replacements" list
replacements = []
with open(replacements_file, 'r') as f:
    for line in f:
        letters = line[0:1]
        replacements.append(letters)


# Replaces character in the password
def replace_chars(line):
    for old_char, new_char in replacements.items():
        line = line.replace(old_char, new_char)
    return line

with open(input, 'r') as infile:
    for line in infile:
        # print(replacements)
        for char in line:
            if char in replacements:
                print(line)
    # with open(output, 'w') as outfile:
        #  for line in infile:
        #     for char in line:
        #         if char in replacements:
        #             print(char)
                    # line = line.replace(char, replacements[char])
                    # outfile.write(line)
                
