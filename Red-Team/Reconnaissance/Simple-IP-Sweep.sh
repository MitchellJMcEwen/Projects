#!/bin/bash

# Variables input arg 1 and 2

IP_Address="$1"
File_Name="$2"

# Accept input variable argument 2 or less than 2 = print error

if [ "$#" -lt 2 ]; then
    echo "Usage: ./ip-sweep.sh {IP_ADDRESS} {FILE_NAME}"
    exit 1
fi

# Check if the file exists or create it

if [ ! -e "$File_Name" ]; then
    echo "File does not exist, creating it now..."
    touch "$File_Name"
fi

# Loop to ping IP addresses through /24 subnet only and store results in the file

for ip in `seq 1 254`; do
ping -c 1 $IP_Address.$ip | grep "64 bytes" | cut -d " " -f 4 | tr -d ":" &
done

