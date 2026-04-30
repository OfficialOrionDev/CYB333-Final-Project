
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

# Puts letters to search for in input.txt into a list
replacements = []
filler = ["/", "!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "_", "+", "=", "{", "}", "[", "]", "|", ":", ";","<", ">","?"] 
with open(replacements_file, 'r') as f:
    for line in f:
        replacements.append(line[0:1]) # Gets the first character of each line in the file and adds it to the list
print(replacements)
print("\n")

def randomize(char):
    with open(replacements_file, 'r') as f:
        list = []
        for line in f:
            for c in line:
                # Line clean up to only give characters to use
                line = line.replace(',', '')
                line = line.replace('\n', '') 

                # If the character to replace exists in the word, replace it with a random character
                if char == c:
                    # temporarily fills "list" with the characters to replace with
                    for i in range(4, len(line)):
                        list.append(line[i]) # Appends first item in list.
                        c = random.choice(list) # Chooses a random character from the list to replace with
                    return c
        # char = random.choice(replacements)
            

with open(input, 'r') as infile:      
    with open(output, 'w') as outfile:
        for line in infile:
            for char in line:
                # Checks each character. If it's in the list of characters to replace, randomize it. Otherwise, write it as is.
                if char in replacements:
                    char = char.replace(char, randomize(char))
                outfile.write(char)
                if len(line) < 16:
                    pass
                    # line = line + outfile.write(random.choice(filler)) # If the password is less than 16 characters, add a random character from the filler list to increase its strength.
