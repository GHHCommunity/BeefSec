green=`tput setaf 2`
RED=`tput setaf 1`
reset=`tput sgr0`
if [ "$(id -u)" != "0" ]; then
   echo "${RED} This script must be run as root" 1>&2
   exit 1
fi
if ! which beef-xss > /dev/null; then
   echo -e "${RED}[!]${reset} Beef not found! Installing it"
   sleep 2
   sudo apt-get install beef-xss
else
   echo -e "${green}[+]${reset} Beef-xss already installed ready to run the script"
   sleep 2
   sudo apt-get install gnome-terminal -y
   unzip ngrok.zip
   rm ngrok.zip
   python3  main.py
   
fi
   
