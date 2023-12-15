
# SHA256 Password Cracking 

from pwn import *
import sys
import time
import os

# art for fun
ascii_art = [ 
" ",
" ",
"  @@@@@@ @@@  @@@  @@@@@@   @@@@@@  @@@@@@@   @@@@@            ",
" !@@     @@!  @@@ @@!  @@@ @@   @@@ !@@     @@!@               ",
"  !@@!!  @!@!@!@! @!@!@!@!   .!!@!  !!@@!!  @!@!@!@            ",
"     !:! !!:  !!! !!:  !!!  !!:         !:! !!:  !!!           ",
" ::.: :   :   : :  :   : : :.:: ::: :: : :   : : ::            ",
"                                                               ",
"  @@@@@@@ @@@@@@@   @@@@@@   @@@@@@@ @@@  @@@ @@@@@@@@ @@@@@@@ ",
" !@@      @@!  @@@ @@!  @@@ !@@      @@!  !@@ @@!      @@!  @@@",
" !@!      @!@!!@!  @!@!@!@! !@!      @!@@!@!  @!!!:!   @!@!!@! ",
" :!!      !!: :!!  !!:  !!! :!!      !!: :!!  !!:      !!: :!! ",
"  :: :: :  :   : :  :   : :  :: :: :  :   ::: : :: :::  :   : :",
" ",
" ",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣶⣤⣀⣀⣤⣶⣷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣸⣿⣿⣿⣿⣿⣿⣿⣿⣇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀                 ⣾⣷⣶⣶⣶⣦⣤⠀⢤⣤⣈⣉⠙⠛⠛⠋⣉⣁⣤⡤⠀⣤⣴⣶⣶⣶⣾⣷⠀",
"⠀                 ⠈⠻⢿⣿⣿⣿⣿⣶⣤⣄⣉⣉⣉⣛⣛⣉⣉⣉⣠⣤⣶⣿⣿⣿⣿⡿⠟⠁⠀",
"⠀⠀⠀⠀⠀                 ⠉⠙⠛⠛⠿⠿⠿⢿⣿⣿⣿⣿⡿⠿⠿⠿⠛⠛⠋⠉⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀",
"⠀⠀⠀⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀   ⠀⢿⣷⠦⠄⢀⣠⡀⠠⣄⡀⠠⠴⣾⡿⠀⠀⠀⠀⠀⣀⡀⠀ ",
"⠀⠀⠀⠀⠀⠀⠀                ⢤⣤⣴⣾⣿⣿⣷⣤⣙⣿⣷⣦⣤⡤⠀⠴⠶⠟⠛⠉⠀⠀  ",
"⠀⠀⠀⠀⠀⠀⠀                ⠀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠏⠀⠺⣷⣄⠀⠀⠀⠀⠀  ",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               ⢈⣙⣛⣻⣿⣿⣿⡿⠃⠐⠿⠿⣾⣿⣷⡄⠀⠀⠀  ",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀               ⠘⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⠀⠀⠀⠈⠁⠀⠀⠀  ",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠹⣿⣿⣿⣾⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀ ⠀",
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀                ⠙⠛⠛⠋⠀⠀⠀⠀⠀       ⠀ ",
" ", 
" ", ]    

 # Function to print ASCII art with delay
def print_ascii_art(art, delay=.1):
    for line in art:
        print(line)
        time.sleep(delay)

# Call the function with your ASCII art
print_ascii_art(ascii_art)

print("---------------------------------------------------------")
print("Have your Hash value and Password list ready!!")
print("---------------------------------------------------------")                                                              

prompts = ["Enter the Hash Value: ", "Enter the Password List File Name: "]
input_values = []

for prompt in prompts:
    while True:
        user_input = input(prompt).strip()

        if user_input.lower() == "exit":
            print("Exiting...")
            sys.exit(0)

        if prompt.endswith("File Name: ") and not os.path.exists(user_input):
            print("File does not exist. Please enter a valid file name.")
            continue

        input_values.append(user_input)
        break

if len(input_values) != 2:
    print("Not all inputs were entered, exiting...")
    sys.exit(1)

wanted_hash, password_file = input_values

attempts = 0

# Start cracking with statement to show progress
with log.progress("Attempting to crack: {}!\n".format(wanted_hash)) as p:
# input password file variable, read, specify the encoding for some in file
	with open(password_file, "r", encoding='latin-1') as password_list:
        # iterate over each password/line
		for password in password_list:
            # clean up the password
			password = password.strip("\n").encode('latin-1')
            # hash the password with sha256sumhex function in pwn tools for the comparison we are making
			password_hash = sha256sumhex(password)
			# update with status with plain text password and hash
			p.status("[{}] {} == {}".format(attempts, password.decode('latin-1'), password_hash))
			# if it matches
			if password_hash == wanted_hash: 
				p.success("Password hash found after {} attempts! {} hashes to {}!".format(attempts, password.decode('latin-1'), password_hash))
				exit()
			attempts +=1
		p.failure("Password hash not found!")
