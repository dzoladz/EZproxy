# Simple script to process user.txt file for EZproxy
# Allow user:pass and pass:user combinations

# import os
# working_dir = os.getcwd()
# print(working_dir)
working_dir = '/Users/Derek/Desktop'

# Set Script Variables
file_name='staff.txt'
out_filename=file_name+'.out'

# Create Working Directories for script
source = working_dir+'/'+file_name
destination = working_dir+'/'+out_filename

# File to open and read
user_file = open(source,'r')

with open(destination, "w") as out_file:
    for user in user_file:
        if user.startswith('#'): # print comments 'as is'
            out_file.write(user)
        elif user.startswith('\n'): # retain spacing from original file
            out_file.write(user)
        elif ':' in user: # given file may use . as delimiter
            a , b = user.strip().replace(" ", "").split(":") # if . change split()
            # toggle with comment, or flip inline
            out_file.write(a + ':' + b + "\n")
            out_file.write(b + ':' + a + "\n")