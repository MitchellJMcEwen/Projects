#!/bin/bash
 
# declare variable
CYAN="\033[00;36m"
RESET="\033[0m"
info_path=$domain/info
subdomain_path=$domain/subdomains
screenshot_path=$domain/screenshots


# ASCII art for fun

ascii_art=(
" "
"    _    _      _      ______                     "
"   | |  | |    | |     | ___ \                    "
"   | |  | | ___| |__   | |_/ /___  ___ ___  _ __  "
"   | |/\| |/ _ \ '_ \  |    // _ \/ __/ _ \| '_ \ "
"   \  /\  /  __/ |_) | | |\ \  __/ (_| (_) | | | |"
"    \/  \/ \___|_.__/  \_| \_\___|\___\___/|_| |_|"
"-------------------------------------------------------"
"                                           "
"                                           "	
"                                           "
"⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣀⣀⣀⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀"
"⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠾⠛⢉⣉⣉⣉⡉⠛⠷⣦⣄⠀⠀⠀⠀"
"⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣴⠋⣠⣴⣿⣿⣿⣿⣿⡿⣿⣶⣌⠹⣷⡀⠀⠀"
"⠀⠀⠀⠀ ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⠁⣴⣿⣿⣿⣿⣿⣿⣿⣿⣆⠉⠻⣧⠘⣷⠀⠀"
"⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡇⢰⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠈⠀⢹⡇⠀"
"⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⡇⢸⣿⠛⣿⣿⣿⣿⣿⣿⡿⠃⠀⠀⠀⠀⢸⡇⠀"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⣷⠀⢿⡆⠈⠛⠻⠟⠛⠉⠀⠀⠀⠀⠀⠀⣾⠃⠀"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠸⣧⡀⠻⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⠃⠀⠀"
"⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⢼⠿⣦⣄⠀⠀⠀⠀⠀⠀⠀⣀⣴⠟⠁⠀⠀⠀"
"⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣦⠀⠀⠈⠉⠛⠓⠲⠶⠖⠚⠋⠉⠀⠀⠀⠀⠀⠀"
"⠀   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
"⠀⠀  ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
" ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣾⣿⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
"   ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣄⠈⠛⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
"⠀⠀⠀    ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀"
)

# Display ASCII art with a sleep timer
display_ascii_art() {
  for line in "${ascii_art[@]}"; do
    echo "$line"
    sleep 0.1  # Sleep duration 
  done
}

# Call the function to display ASCII art
display_ascii_art

# Requirements

echo """
-------------------------------------------------------
This script requires the following be installed:
-------------------------------------------------------
1. Golang (https://go.dev/doc/install)
2. Subfinder (https://github.com/projectdiscovery/subfinder)
3. Assetfinder (https://github.com/tomnomnom/assetfinder)
4. Amass (https://github.com/owasp-amass/amass)
5. Httprobe (https://github.com/tomnomnom/httprobe)
6. Gowtiness (https://github.com/sensepost/gowitness)
--------------------------------------------------------
"""


# Prompt the user if they want to install the program.
while true; do
    read -p "Do you wish to continue? [Yes] [No]:  " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Please answer yes or no.";;
    esac
done


# Prompt the user for the targeted domain

while true; do
    read -p "Enter a target domain name:  " domain
    if [ -n "$domain" ]; then
    	break
    else
    	echo "Domain cannot be empty. Please enter a valid domain name."
    fi
done


# make a directory for the variable/domain name if it doesnt exist

if [ ! -d "$domain" ];then
	mkdir $domain
fi	

if [ ! -d "$info_path" ];then
	mkdir $info_path
fi	

if [ ! -d "$subdomain_path" ];then
	mkdir $subdomain_path
fi	

if [ ! -d "$screenshot_path" ];then
	mkdir $screenshot_path
fi	

echo "Starting recon against target domain: $domain"


# Starting recon against the specified domain

# 1.Whois

echo -e "${CYAN} [+] Checking who is... ${RESET}"
whois $domain > $info_path/whois.txt

# 2.Subfinder

echo -e "${CYAN} [+] Launching subfinder...${RESET}"
subfinder -d $domain > $subdomain_path/found.txt

# 3.Assetfinder

echo -e "${CYAN} [+] Running assetfinder...${RESET}"
assetfinder $domain | grep $domain >> $subdomain_path/found.txt

# 4.Amass
# Amass usually takes some time to run

echo -e "${CYAN} [+] Running Amass. This could take a while...${RESET}"
amass enum -d $domain >> $subdomain_path/found.txt

# 5.Httprobe
# We are looking for results only using https and striping the "://" from each result

echo -e "${CYAN} [+] Checking what's alive...${RESET}"
cat $subdomain_path/found.txt | grep $domain | sort -u | httprobe -prefer-https | grep https | sed 's/https\?:\/\///' | tee -a $subdomain_path/alive.txt

# 6.Gowitness

echo -e "${CYAN} [+] Taking dem screenshotz...${RESET}"
gowitness file -f $subdomain_path/alive.txt -P $screenshot_path/ --no-http







