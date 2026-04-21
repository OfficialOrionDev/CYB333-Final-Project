"""
This script translates unsecured passwords into more secure ones by replacing characters with similar looking characters to 
satisfy a minimum password strength requirement. For example, 'a' might be replaced with '@', 's' with '$', etc.
The letter mapping is read from a file passwordReplacement.txt, applies the replacements, and  
writes the secure passwords to an output file.

"""

import random

ab = "Z:\\Desktop General\\VS Code"

input = ab + '\\input.txt'
output = ab + '\\output.txt'
replacements_file = ab + '\\passwordReplacement.txt'

# Load replacements from file
replacements = {}
with open(replacements_file, 'r') as f:
    for line in f:
        line = line[4:].strip().replace(',', '')  # Removes commas
        replacements[line] = line
        print(line)

def replace_chars(line):
    pass

# with open(input, 'r') as infile:
#     with open(output, 'w') as outfile:
#         for line in infile:
#             processed_line = replace_chars(line)
#             outfile.write(processed_line)
#             print(processed_line)
