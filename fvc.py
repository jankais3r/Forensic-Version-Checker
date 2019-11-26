#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import queue
import base64
import webbrowser
import configparser
from tkinter import *
from threading import Thread
from tkinter import messagebox
try:
	from tabulate import tabulate
except:
	print('Install tabulate with "pip3 install tabulate"')
	quit()
try:
	import grequests
except:
	print('Install qrequests with "pip3 install grequests"')
	quit()
try:
	from bs4 import BeautifulSoup
except:
	print('Install BeautifulSoup with "pip3 install beautifulsoup4"')
	quit()

if os.path.isfile('current_versions.ini') == False:
	default_config = """[CURRENT]
gui = Display all
encase = 
blacklight = 
macquisition = 
axiom = 
ufed4pc = 
physicalanalyzer = 
osf = 
forensicexplorer = 
usbdetective = 
ftk = 
ftkimager = 
xamn = 
xways = 
cyberchef = 
nsrl = 
aim = 
passware = 
hashcat = 
exiftool =
bec = 
caine = 
deft = 
ffn = 
atola = 
fec = 
veracrypt = 
autopsy = 
sleuthkit = 
mountimagepro = 
netanalysis = 
hstex = 
"""

	configfile = open('current_versions.ini', 'w')
	configfile.write(default_config)
	configfile.close()
	first_run = True
else:
	first_run = False

config = configparser.ConfigParser()
config.read('current_versions.ini')

mt_queue = queue.Queue()

def spinning_cursor():
    while True:
        for cursor in '|/–\\':
            yield cursor

def crawl():
	ua_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
	}
	
	urls = ['https://www.guidancesoftware.com/encase-forensic',
			'https://www.blackbagtech.com/downloads/',
			'https://www.magnetforensics.com/downloadaxiom/',
			'https://www.cellebrite.com/en/support/product-releases/',
			'https://www.osforensics.com/whatsnew.html',
			'http://www.forensicexplorer.com/version.php',
			'https://usbdetective.com/release-notes/',
			'https://accessdata.com/product-download',
			'https://www.msab.com/downloads/',
			'https://www.x-ways.net/forensics/index-m.html',
			'https://github.com/gchq/CyberChef/releases/latest',
			'https://s3.amazonaws.com/rds.nsrl.nist.gov/RDS/current/README.txt',
			'https://github.com/jankais3r/Forensic-Version-Checker/releases/latest',
			'https://arsenalrecon.com/downloads/',
			'https://blog.passware.com/category/product-update/',
			'https://hashcat.net/beta/',
			'https://owl.phy.queensu.ca/~phil/exiftool/history.html',
			'https://belkasoft.com/becver.txt',
			'https://distrowatch.com/table.php?distribution=caine',
			'https://distrowatch.com/table.php?distribution=deft',
			'https://www.logicube.com/knowledge/forensic-falcon-neo/',
			'https://atola.com/products/taskforce/download.html',
			'http://www.metaspike.com/fec-change-log/',
			'https://www.veracrypt.fr/en/Downloads.html',
			'https://github.com/sleuthkit/autopsy/releases/latest',
			'https://github.com/sleuthkit/sleuthkit/releases/latest',
			'http://www.forensicexplorer.com/download.php',
			'https://www.digital-detective.net/start/netanalysis-quick-start/',
			'https://www.digital-detective.net/start/hstex-quick-start/'
		]
	mt_queue.put(grequests.map((grequests.get(u, headers=ua_headers) for u in urls), size=5))

def latest_update():
	thread = Thread(target=crawl)
	thread.start()
	while(thread.is_alive()):
		current_save.configure(text='Checking for updates·..')
		window.update()
		time.sleep(0.15)
		current_save.configure(text='Checking for updates.·.')
		window.update()
		time.sleep(0.15)
		current_save.configure(text='Checking for updates..·')
		window.update()
		time.sleep(0.15)
		current_save.configure(text='Checking for updates...')
		for _ in range(10):
			window.update()
			time.sleep(0.15)
		
	response = mt_queue.get()
	
	### EnCase
	try:
		current = encase_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[0].text, 'html.parser')
			version = soup.select_one('h3').text.strip()
			version = version.replace('EnCase Forensic ','')
			version = version.split(':')[0]
		except:
			version = 'Error'
			encase_latest.configure(readonlybackground='red')
		
		encase_latest.configure(state='normal')
		encase_latest.delete(0, END)
		encase_latest.insert(0,version)
		encase_latest.configure(state='readonly')
		if encase_current.get() == encase_latest.get():
			encase_latest.configure(readonlybackground='limegreen')
			encase_update.configure(text='', cursor='')
		elif ((encase_current.get() != '') and (encase_latest.get() != 'Error')):
			encase_latest.configure(readonlybackground='orange')
			encase_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### BlackLight
	try:
		current = blacklight_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[1].text, 'html.parser')
			version = soup.find('dl', {'id': 'blacklightrevision'}).select_one('span').text.strip()
			version = version.replace('BlackLight ','')
		except:
			version = 'Error'
			blacklight_latest.configure(readonlybackground='red')
		blacklight_latest.configure(state='normal')
		blacklight_latest.delete(0, END)
		blacklight_latest.insert(0,version)
		blacklight_latest.configure(state='readonly')
		if blacklight_current.get() == blacklight_latest.get():
			blacklight_latest.configure(readonlybackground='limegreen')
			blacklight_update.configure(text='', cursor='')
		elif ((blacklight_current.get() != '') and (blacklight_latest.get() != 'Error')):
			blacklight_latest.configure(readonlybackground='orange')
			blacklight_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### MacQuisition
	try:
		current = macquisition_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[1].text, 'html.parser')
			version = soup.find('dl', {'id': 'macquisitionrevision'}).select_one('span').text.strip()
			version = version.replace('MacQuisition ','')
		except:
			version = 'Error'
			macquisition_latest.configure(readonlybackground='red')
		macquisition_latest.configure(state='normal')
		macquisition_latest.delete(0, END)
		macquisition_latest.insert(0,version)
		macquisition_latest.configure(state='readonly')
		if macquisition_current.get() == macquisition_latest.get():
			macquisition_latest.configure(readonlybackground='limegreen')
			macquisition_update.configure(text='', cursor='')
		elif ((macquisition_current.get() != '') and (macquisition_latest.get() != 'Error')):
			macquisition_latest.configure(readonlybackground='orange')
			macquisition_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### AXIOM
	try:
		current = axiom_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[2].text, 'html.parser')
			version = soup.select_one('h2').text.strip()
			version = version.replace('MAGNET AXIOM ','')
		except:
			version = 'Error'
			axiom_latest.configure(readonlybackground='red')
		axiom_latest.configure(state='normal')
		axiom_latest.delete(0, END)
		axiom_latest.insert(0,version)
		axiom_latest.configure(state='readonly')
		if axiom_current.get() == axiom_latest.get():
			axiom_latest.configure(readonlybackground='limegreen')
			axiom_update.configure(text='', cursor='')
		elif ((axiom_current.get() != '') and (axiom_latest.get() != 'Error')):
			axiom_latest.configure(readonlybackground='orange')
			axiom_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### UFED 4PC
	try:
		current = ufed4pc_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[3].text, 'html.parser')
			version = soup.find(text=re.compile('UFED.(4PC|Ultimate).')).parent.select_one('b').text.strip()
			version = version.replace('Version ','')
		except:
			version = 'Error'
			ufed4pc_latest.configure(readonlybackground='red')
		ufed4pc_latest.configure(state='normal')
		ufed4pc_latest.delete(0, END)
		ufed4pc_latest.insert(0,version)
		ufed4pc_latest.configure(state='readonly')
		if ufed4pc_current.get() == ufed4pc_latest.get():
			ufed4pc_latest.configure(readonlybackground='limegreen')
			ufed4pc_update.configure(text='', cursor='')
		elif ((ufed4pc_current.get() != '') and (ufed4pc_latest.get() != 'Error')):
			ufed4pc_latest.configure(readonlybackground='orange')
			ufed4pc_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Physical Analyzer
	try:
		current = physicalanalyzer_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[3].text, 'html.parser')
			version = soup.find(text=re.compile('(Physical|Logical).Analyzer.')).parent.select_one('b').text.strip()
			version = version.replace('Version ','')
		except:
			version = 'Error'
			physicalanalyzer_latest.configure(readonlybackground='red')
		physicalanalyzer_latest.configure(state='normal')
		physicalanalyzer_latest.delete(0, END)
		physicalanalyzer_latest.insert(0,version)
		physicalanalyzer_latest.configure(state='readonly')
		if physicalanalyzer_current.get() == physicalanalyzer_latest.get():
			physicalanalyzer_latest.configure(readonlybackground='limegreen')
			physicalanalyzer_update.configure(text='', cursor='')
		elif ((physicalanalyzer_current.get() != '') and (physicalanalyzer_latest.get() != 'Error')):
			physicalanalyzer_latest.configure(readonlybackground='orange')
			physicalanalyzer_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### OSForensics
	try:
		current = osf_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[4].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.replace(' build ','.')
			version = version.split(' ')[0]
			version = version[1:]
		except:
			version = 'Error'
			osf_latest.configure(readonlybackground='red')
		osf_latest.configure(state='normal')
		osf_latest.delete(0, END)
		osf_latest.insert(0,version)
		osf_latest.configure(state='readonly')
		if osf_current.get() == osf_latest.get():
			osf_latest.configure(readonlybackground='limegreen')
			osf_update.configure(text='', cursor='')
		elif ((osf_current.get() != '') and (osf_latest.get() != 'Error')):
			osf_latest.configure(readonlybackground='orange')
			osf_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### ForensicExplorer
	try:
		current = forensicexplorer_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[5].text, 'html.parser')
			version = soup.text.strip()
			version = version.replace('v','')
		except:
			version = 'Error'
			forensicexplorer_latest.configure(readonlybackground='red')
		forensicexplorer_latest.configure(state='normal')
		forensicexplorer_latest.delete(0, END)
		forensicexplorer_latest.insert(0,version)
		forensicexplorer_latest.configure(state='readonly')
		if forensicexplorer_current.get() == forensicexplorer_latest.get():
			forensicexplorer_latest.configure(readonlybackground='limegreen')
			forensicexplorer_update.configure(text='', cursor='')
		elif ((forensicexplorer_current.get() != '') and (forensicexplorer_latest.get() != 'Error')):
			forensicexplorer_latest.configure(readonlybackground='orange')
			forensicexplorer_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### USB Detective
	try:
		current = usbdetective_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[6].text, 'html.parser')
			version = soup.select_one('h2').text.strip()
			version = version.replace('Version ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
			usbdetective_latest.configure(readonlybackground='red')
		usbdetective_latest.configure(state='normal')
		usbdetective_latest.delete(0, END)
		usbdetective_latest.insert(0,version)
		usbdetective_latest.configure(state='readonly')
		if usbdetective_current.get() == usbdetective_latest.get():
			usbdetective_latest.configure(readonlybackground='limegreen')
			usbdetective_update.configure(text='', cursor='')
		elif ((usbdetective_current.get() != '') and (usbdetective_latest.get() != 'Error')):
			usbdetective_latest.configure(readonlybackground='orange')
			usbdetective_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### FTK
	try:
		current = ftk_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[7].text, 'html.parser')
			version = soup.select_one('a[href^="http://accessdata.com/product-download/forensic-toolkit-ftk-version"]').parent.parent.select_one('h5').text.strip()
			version = version.replace('Forensic Toolkit (FTK) version ','')
		except:
			version = 'Error'
			ftk_latest.configure(readonlybackground='red')
		ftk_latest.configure(state='normal')
		ftk_latest.delete(0, END)
		ftk_latest.insert(0,version)
		ftk_latest.configure(state='readonly')
		if ftk_current.get() == ftk_latest.get():
			ftk_latest.configure(readonlybackground='limegreen')
			ftk_update.configure(text='', cursor='')
		elif ((ftk_current.get() != '') and (ftk_latest.get() != 'Error')):
			ftk_latest.configure(readonlybackground='orange')
			ftk_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### FTK Imager
	try:
		current = ftkimager_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[7].text, 'html.parser')
			version = soup.select_one('a[href^="http://accessdata.com/product-download/ftk-imager-version"]').parent.parent.select_one('h5').text.strip()
			version = version.replace('FTK Imager version ','')
		except:
			version = 'Error'
			ftkimager_latest.configure(readonlybackground='red')
		ftkimager_latest.configure(state='normal')
		ftkimager_latest.delete(0, END)
		ftkimager_latest.insert(0,version)
		ftkimager_latest.configure(state='readonly')
		if ftkimager_current.get() == ftkimager_latest.get():
			ftkimager_latest.configure(readonlybackground='limegreen')
			ftkimager_update.configure(text='', cursor='')
		elif ((ftkimager_current.get() != '') and (ftkimager_latest.get() != 'Error')):
			ftkimager_latest.configure(readonlybackground='orange')
			ftkimager_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### XAMN
	try:
		current = xamn_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[8].text, 'html.parser')
			version = soup.find('a', {'class': 'wpfd_downloadlink'})['title']
			version = version.replace('XAMN v','')
		except:
			version = 'Error'
			xamn_latest.configure(readonlybackground='red')
		xamn_latest.configure(state='normal')
		xamn_latest.delete(0, END)
		xamn_latest.insert(0,version)
		xamn_latest.configure(state='readonly')
		if xamn_current.get() == xamn_latest.get():
			xamn_latest.configure(readonlybackground='limegreen')
			xamn_update.configure(text='', cursor='')
		elif ((xamn_current.get() != '') and (xamn_latest.get() != 'Error')):
			xamn_latest.configure(readonlybackground='orange')
			xamn_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### X-Ways
	try:
		current = xways_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[9].text, 'html.parser')
			version = soup.find('div', {'class': 'content'}).select_one('b').text.strip()
			version = version[19:].strip()
		except:
			version = 'Error'
			xways_latest.configure(readonlybackground='red')
		xways_latest.configure(state='normal')
		xways_latest.delete(0, END)
		xways_latest.insert(0,version)
		xways_latest.configure(state='readonly')
		if xways_current.get() == xways_latest.get():
			xways_latest.configure(readonlybackground='limegreen')
			xways_update.configure(text='', cursor='')
		elif ((xways_current.get() != '') and (xways_latest.get() != 'Error')):
			xways_latest.configure(readonlybackground='orange')
			xways_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### CyberChef
	try:
		current = cyberchef_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[10].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('v','')
		except:
			version = 'Error'
			cyberchef_latest.configure(readonlybackground='red')
		cyberchef_latest.configure(state='normal')
		cyberchef_latest.delete(0, END)
		cyberchef_latest.insert(0,version)
		cyberchef_latest.configure(state='readonly')
		if cyberchef_current.get() == cyberchef_latest.get():
			cyberchef_latest.configure(readonlybackground='limegreen')
			cyberchef_update.configure(text='', cursor='')
		elif ((cyberchef_current.get() != '') and (cyberchef_latest.get() != 'Error')):
			cyberchef_latest.configure(readonlybackground='orange')
			cyberchef_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### NSRL
	try:
		current = nsrl_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[11].text, 'html.parser')
			version = soup.text.strip()
			version = version.replace('NSRL RDS Version ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
			nsrl_latest.configure(readonlybackground='red')
		nsrl_latest.configure(state='normal')
		nsrl_latest.delete(0, END)
		nsrl_latest.insert(0,version)
		nsrl_latest.configure(state='readonly')
		if nsrl_current.get() == nsrl_latest.get():
			nsrl_latest.configure(readonlybackground='limegreen')
			nsrl_update.configure(text='', cursor='')
		elif ((nsrl_current.get() != '') and (nsrl_latest.get() != 'Error')):
			nsrl_latest.configure(readonlybackground='orange')
			nsrl_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Arsenal Image Mounter
	try:
		current = aim_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[13].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.replace('Arsenal Image Mounter v','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
			aim_latest.configure(readonlybackground='red')
		aim_latest.configure(state='normal')
		aim_latest.delete(0, END)
		aim_latest.insert(0,version)
		aim_latest.configure(state='readonly')
		if aim_current.get() == aim_latest.get():
			aim_latest.configure(readonlybackground='limegreen')
			aim_update.configure(text='', cursor='')
		elif ((aim_current.get() != '') and (aim_latest.get() != 'Error')):
			aim_latest.configure(readonlybackground='orange')
			aim_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Passware
	try:
		current = passware_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[14].text, 'html.parser')
			version = soup.select_one('a[href^="https://blog.passware.com/passware-kit"]').select_one('h2').text.strip()
			version = version.replace('Passware Kit','')
			version = version.strip()
		except:
			version = 'Error'
			passware_latest.configure(readonlybackground='red')
		passware_latest.configure(state='normal')
		passware_latest.delete(0, END)
		passware_latest.insert(0,version)
		passware_latest.configure(state='readonly')
		if passware_current.get() == passware_latest.get():
			passware_latest.configure(readonlybackground='limegreen')
			passware_update.configure(text='', cursor='')
		elif ((passware_current.get() != '') and (passware_latest.get() != 'Error')):
			passware_latest.configure(readonlybackground='orange')
			passware_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### hashcat
	try:
		current = hashcat_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[15].text, 'html.parser')
			version = soup.select_one('a[href^="hashcat-"]')['href']
			version = version.replace('hashcat-','')
			version = version.replace('%2B','+')
			version = version.replace('.7z','')
		except:
			version = 'Error'
			hashcat_latest.configure(readonlybackground='red')
		hashcat_latest.configure(state='normal')
		hashcat_latest.delete(0, END)
		hashcat_latest.insert(0,version)
		hashcat_latest.configure(state='readonly')
		if hashcat_current.get() == hashcat_latest.get():
			hashcat_latest.configure(readonlybackground='limegreen')
			hashcat_update.configure(text='', cursor='')
		elif ((hashcat_current.get() != '') and (hashcat_latest.get() != 'Error')):
			hashcat_latest.configure(readonlybackground='orange')
			hashcat_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### ExifTool
	try:
		current = exiftool_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[16].text, 'html.parser')
			version = soup.findAll('a')[3]['name']
			version = version.replace('v','')
		except:
			version = 'Error'
			exiftool_latest.configure(readonlybackground='red')
		exiftool_latest.configure(state='normal')
		exiftool_latest.delete(0, END)
		exiftool_latest.insert(0,version)
		exiftool_latest.configure(state='readonly')
		if exiftool_current.get() == exiftool_latest.get():
			exiftool_latest.configure(readonlybackground='limegreen')
			exiftool_update.configure(text='', cursor='')
		elif ((exiftool_current.get() != '') and (exiftool_latest.get() != 'Error')):
			exiftool_latest.configure(readonlybackground='orange')
			exiftool_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Belkasoft Evidence Center
	try:
		current = bec_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[17].text, 'html.parser')
			version = soup.text.strip()
		except:
			version = 'Error'
			bec_latest.configure(readonlybackground='red')
		bec_latest.configure(state='normal')
		bec_latest.delete(0, END)
		bec_latest.insert(0,version)
		bec_latest.configure(state='readonly')
		if bec_current.get() == bec_latest.get():
			bec_latest.configure(readonlybackground='limegreen')
			bec_update.configure(text='', cursor='')
		elif ((bec_current.get() != '') and (bec_latest.get() != 'Error')):
			bec_latest.configure(readonlybackground='orange')
			bec_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### CAINE
	try:
		current = caine_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[18].text, 'html.parser')
			version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
		except:
			version = 'Error'
			caine_latest.configure(readonlybackground='red')
		caine_latest.configure(state='normal')
		caine_latest.delete(0, END)
		caine_latest.insert(0,version)
		caine_latest.configure(state='readonly')
		if caine_current.get() == caine_latest.get():
			caine_latest.configure(readonlybackground='limegreen')
			caine_update.configure(text='', cursor='')
		elif ((caine_current.get() != '') and (caine_latest.get() != 'Error')):
			caine_latest.configure(readonlybackground='orange')
			caine_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### DEFT
	try:
		current = deft_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[19].text, 'html.parser')
			version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
		except:
			version = 'Error'
			deft_latest.configure(readonlybackground='red')
		deft_latest.configure(state='normal')
		deft_latest.delete(0, END)
		deft_latest.insert(0,version)
		deft_latest.configure(state='readonly')
		if deft_current.get() == deft_latest.get():
			deft_latest.configure(readonlybackground='limegreen')
			deft_update.configure(text='', cursor='')
		elif ((deft_current.get() != '') and (deft_latest.get() != 'Error')):
			deft_latest.configure(readonlybackground='orange')
			deft_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Forensic Falcon Neo
	try:
		current = ffn_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[20].text, 'html.parser')
			version = soup.find('table', {'class': 'datatableblue'}).findAll('tr')[2].findAll('td')[1].text.strip()
		except:
			version = 'Error'
			ffn_latest.configure(readonlybackground='red')
		ffn_latest.configure(state='normal')
		ffn_latest.delete(0, END)
		ffn_latest.insert(0,version)
		ffn_latest.configure(state='readonly')
		if ffn_current.get() == ffn_latest.get():
			ffn_latest.configure(readonlybackground='limegreen')
			ffn_update.configure(text='', cursor='')
		elif ((ffn_current.get() != '') and (ffn_latest.get() != 'Error')):
			ffn_latest.configure(readonlybackground='orange')
			ffn_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Atola TaskForce
	try:
		current = atola_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[21].text, 'html.parser')
			version = soup.select_one('a[href^="http://dl.atola.com/taskforce/"]').text.strip()
			version = version.replace('Download ','')
		except:
			version = 'Error'
			atola_latest.configure(readonlybackground='red')
		atola_latest.configure(state='normal')
		atola_latest.delete(0, END)
		atola_latest.insert(0,version)
		atola_latest.configure(state='readonly')
		if atola_current.get() == atola_latest.get():
			atola_latest.configure(readonlybackground='limegreen')
			atola_update.configure(text='', cursor='')
		elif ((atola_current.get() != '') and (atola_latest.get() != 'Error')):
			atola_latest.configure(readonlybackground='orange')
			atola_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Forensic Email Collector
	try:
		current = fec_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[22].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.split(' ')[0]
			version = version.replace('v','')
		except:
			version = 'Error'
			fec_latest.configure(readonlybackground='red')
		fec_latest.configure(state='normal')
		fec_latest.delete(0, END)
		fec_latest.insert(0,version)
		fec_latest.configure(state='readonly')
		if fec_current.get() == fec_latest.get():
			fec_latest.configure(readonlybackground='limegreen')
			fec_update.configure(text='', cursor='')
		elif ((fec_current.get() != '') and (fec_latest.get() != 'Error')):
			fec_latest.configure(readonlybackground='orange')
			fec_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### VeraCrypt
	try:
		current = veracrypt_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[23].text, 'html.parser')
			version = soup.select_one('h3').text.strip()
			version = version.replace('Latest Stable Release - ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
			veracrypt_latest.configure(readonlybackground='red')
		veracrypt_latest.configure(state='normal')
		veracrypt_latest.delete(0, END)
		veracrypt_latest.insert(0,version)
		veracrypt_latest.configure(state='readonly')
		if veracrypt_current.get() == veracrypt_latest.get():
			veracrypt_latest.configure(readonlybackground='limegreen')
			veracrypt_update.configure(text='', cursor='')
		elif ((veracrypt_current.get() != '') and (veracrypt_latest.get() != 'Error')):
			veracrypt_latest.configure(readonlybackground='orange')
			veracrypt_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Autopsy
	try:
		current = autopsy_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[24].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('Autopsy ','')
		except:
			version = 'Error'
			autopsy_latest.configure(readonlybackground='red')
		autopsy_latest.configure(state='normal')
		autopsy_latest.delete(0, END)
		autopsy_latest.insert(0,version)
		autopsy_latest.configure(state='readonly')
		if autopsy_current.get() == autopsy_latest.get():
			autopsy_latest.configure(readonlybackground='limegreen')
			autopsy_update.configure(text='', cursor='')
		elif ((autopsy_current.get() != '') and (autopsy_latest.get() != 'Error')):
			autopsy_latest.configure(readonlybackground='orange')
			autopsy_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### The Sleuth Kit
	try:
		current = sleuthkit_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[25].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('The Sleuth Kit ','')
		except:
			version = 'Error'
			sleuthkit_latest.configure(readonlybackground='red')
		sleuthkit_latest.configure(state='normal')
		sleuthkit_latest.delete(0, END)
		sleuthkit_latest.insert(0,version)
		sleuthkit_latest.configure(state='readonly')
		if sleuthkit_current.get() == sleuthkit_latest.get():
			sleuthkit_latest.configure(readonlybackground='limegreen')
			sleuthkit_update.configure(text='', cursor='')
		elif ((sleuthkit_current.get() != '') and (sleuthkit_latest.get() != 'Error')):
			sleuthkit_latest.configure(readonlybackground='orange')
			sleuthkit_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Mount Image Pro
	try:
		current = mountimagepro_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[26].text, 'html.parser')
			version = soup.select_one('a[href^="http://download.getdata.com/support/mip/MountImagePro"]')['href']
			version = version[version.index('(v'):]
			version = version[2:-5]
		except:
			version = 'Error'
			mountimagepro_latest.configure(readonlybackground='red')
		mountimagepro_latest.configure(state='normal')
		mountimagepro_latest.delete(0, END)
		mountimagepro_latest.insert(0,version)
		mountimagepro_latest.configure(state='readonly')
		if mountimagepro_current.get() == mountimagepro_latest.get():
			mountimagepro_latest.configure(readonlybackground='limegreen')
			mountimagepro_update.configure(text='', cursor='')
		elif ((mountimagepro_current.get() != '') and (mountimagepro_latest.get() != 'Error')):
			mountimagepro_latest.configure(readonlybackground='orange')
			mountimagepro_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### NetAnalysis
	try:
		current = netanalysis_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[27].text, 'html.parser')
			version = soup.find('span', {'class': 'avia_iconbox_title'}).text.strip()
			version = version.replace('Download NetAnalysis v','')
		except:
			version = 'Error'
			netanalysis_latest.configure(readonlybackground='red')
		netanalysis_latest.configure(state='normal')
		netanalysis_latest.delete(0, END)
		netanalysis_latest.insert(0,version)
		netanalysis_latest.configure(state='readonly')
		if netanalysis_current.get() == netanalysis_latest.get():
			netanalysis_latest.configure(readonlybackground='limegreen')
			netanalysis_update.configure(text='', cursor='')
		elif ((netanalysis_current.get() != '') and (netanalysis_latest.get() != 'Error')):
			netanalysis_latest.configure(readonlybackground='orange')
			netanalysis_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### HstEx
	try:
		current = hstex_current.get()
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		try:
			soup = BeautifulSoup(response[28].text, 'html.parser')
			version = soup.find('span', {'class': 'avia_iconbox_title'}).text.strip()
			version = version.replace('Download HstEx v','')
		except:
			version = 'Error'
			hstex_latest.configure(readonlybackground='red')
		hstex_latest.configure(state='normal')
		hstex_latest.delete(0, END)
		hstex_latest.insert(0,version)
		hstex_latest.configure(state='readonly')
		if hstex_current.get() == hstex_latest.get():
			hstex_latest.configure(readonlybackground='limegreen')
			hstex_update.configure(text='', cursor='')
		elif ((hstex_current.get() != '') and (hstex_latest.get() != 'Error')):
			hstex_latest.configure(readonlybackground='orange')
			hstex_update.configure(text='Update', fg='blue', cursor='hand2')
	
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[12].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version == '1.7'
	if version != '1.7':
		about.configure(text='Update FVC', fg='blue', cursor='hand2')
		about.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'))
		
def cli_update():
	thread = Thread(target=crawl)
	thread.start()
	spinner = spinning_cursor()
	sys.stdout.write('Checking for updates ')
	while(thread.is_alive()):
		sys.stdout.write(next(spinner))
		sys.stdout.flush()
		time.sleep(0.1)
		sys.stdout.write('\b')
	sys.stdout.write('\b' * 21)
	response = mt_queue.get()
	
	table_headers = ['Tool', 'Current Version', 'Latest Version', 'Update?']
	table = []
	
	### EnCase
	try:
		current = config['CURRENT']['encase']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[0].text, 'html.parser')
			version = soup.select_one('h3').text.strip()
			version = version.replace('EnCase Forensic ','')
			version = version.split(':')[0]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Encase', current, version, ''])
		else:
			table.append(['Encase', current, version, 'Update available!'])
	
	
	### BlackLight
	try:
		current = config['CURRENT']['blacklight']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[1].text, 'html.parser')
			version = soup.find('dl', {'id': 'blacklightrevision'}).select_one('span').text.strip()
			version = version.replace('BlackLight ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['BlackLight', current, version, ''])
		else:
			table.append(['BlackLight', current, version, 'Update available!'])
	
	
	### MacQuisition
	try:
		current = config['CURRENT']['macquisition']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[1].text, 'html.parser')
			version = soup.find('dl', {'id': 'macquisitionrevision'}).select_one('span').text.strip()
			version = version.replace('MacQuisition ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['MacQuisition', current, version, ''])
		else:
			table.append(['MacQuisition', current, version, 'Update available!'])
	
	
	### AXIOM
	try:
		current = config['CURRENT']['axiom']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[2].text, 'html.parser')
			version = soup.select_one('h2').text.strip()
			version = version.replace('MAGNET AXIOM ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['AXIOM', current, version, ''])
		else:
			table.append(['AXIOM', current, version, 'Update available!'])
	
	
	### UFED 4PC
	try:
		current = config['CURRENT']['ufed4pc']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[3].text, 'html.parser')
			version = soup.find(text=re.compile('UFED.(4PC|Ultimate).')).parent.select_one('b').text.strip()
			version = version.replace('Version ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['UFED 4PC', current, version, ''])
		else:
			table.append(['UFED 4PC', current, version, 'Update available!'])
	
	
	### Physical Analyzer
	try:
		current = config['CURRENT']['physicalanalyzer']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[3].text, 'html.parser')
			version = soup.find(text=re.compile('(Physical|Logical).Analyzer.')).parent.select_one('b').text.strip()
			version = version.replace('Version ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Physical Analyzer', current, version, ''])
		else:
			table.append(['Physical Analyzer', current, version, 'Update available!'])
	
	
	### OSForensics
	try:
		current = config['CURRENT']['osf']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[4].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.replace(' build ','.')
			version = version.split(' ')[0]
			version = version[1:]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['OSForensics', current, version, ''])
		else:
			table.append(['OSForensics', current, version, 'Update available!'])
	
	
	### ForensicExplorer
	try:
		current = config['CURRENT']['forensicexplorer']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[5].text, 'html.parser')
			version = soup.text.strip()
			version = version.replace('v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['ForensicExplorer', current, version, ''])
		else:
			table.append(['ForensicExplorer', current, version, 'Update available!'])
	
	
	### USB Detective
	try:
		current = config['CURRENT']['usbdetective']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[6].text, 'html.parser')
			version = soup.select_one('h2').text.strip()
			version = version.replace('Version ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['USB Detective', current, version, ''])
		else:
			table.append(['USB Detective', current, version, 'Update available!'])
	
	
	### FTK
	try:
		current = config['CURRENT']['ftk']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[7].text, 'html.parser')
			version = soup.select_one('a[href^="http://accessdata.com/product-download/forensic-toolkit-ftk-version"]').parent.parent.select_one('h5').text.strip()
			version = version.replace('Forensic Toolkit (FTK) version ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['FTK', current, version, ''])
		else:
			table.append(['FTK', current, version, 'Update available!'])
	
	
	### FTK Imager
	try:
		current = config['CURRENT']['ftkimager']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[7].text, 'html.parser')
			version = soup.select_one('a[href^="http://accessdata.com/product-download/ftk-imager-version"]').parent.parent.select_one('h5').text.strip()
			version = version.replace('FTK Imager version ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['FTK Imager', current, version, ''])
		else:
			table.append(['FTK Imager', current, version, 'Update available!'])
	
	
	### XAMN
	try:
		current = config['CURRENT']['xamn']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[8].text, 'html.parser')
			version = soup.find('a', {'class': 'wpfd_downloadlink'})['title']
			version = version.replace('XAMN v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['XAMN', current, version, ''])
		else:
			table.append(['XAMN', current, version, 'Update available!'])
	
	
	### X-Ways
	try:
		current = config['CURRENT']['xways']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[9].text, 'html.parser')
			version = soup.find('div', {'class': 'content'}).select_one('b').text.strip()
			version = version[19:].strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['X-Ways', current, version, ''])
		else:
			table.append(['X-Ways', current, version, 'Update available!'])
	
	
	### CyberChef
	try:
		current = config['CURRENT']['cyberchef']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[10].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['CyberChef', current, version, ''])
		else:
			table.append(['CyberChef', current, version, 'Update available!'])
	
	
	### NSRL
	try:
		current = config['CURRENT']['nsrl']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[11].text, 'html.parser')
			version = soup.text.strip()
			version = version.replace('NSRL RDS Version ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['NSRL hash set', current, version, ''])
		else:
			table.append(['NSRL hash set', current, version, 'Update available!'])
	
	
	### Arsenal Image Mounter
	try:
		current = config['CURRENT']['aim']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[13].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.replace('Arsenal Image Mounter v','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['AIM', current, version, ''])
		else:
			table.append(['AIM', current, version, 'Update available!'])
	
	
	### Passware
	try:
		current = config['CURRENT']['passware']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[14].text, 'html.parser')
			version = soup.select_one('a[href^="https://blog.passware.com/passware-kit"]').select_one('h2').text.strip()
			version = version.replace('Passware Kit','')
			version = version.strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Passware', current, version, ''])
		else:
			table.append(['Passware', current, version, 'Update available!'])
	
	
	### hashcat
	try:
		current = config['CURRENT']['hashcat']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[15].text, 'html.parser')
			version = soup.select_one('a[href^="hashcat-"]')['href']
			version = version.replace('hashcat-','')
			version = version.replace('%2B','+')
			version = version.replace('.7z','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['hashcat', current, version, ''])
		else:
			table.append(['hashcat', current, version, 'Update available!'])
	
	
	### ExifTool
	try:
		current = config['CURRENT']['exiftool']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[16].text, 'html.parser')
			version = soup.findAll('a')[3]['name']
			version = version.replace('v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['ExifTool', current, version, ''])
		else:
			table.append(['ExifTool', current, version, 'Update available!'])
	
	
	### Belkasoft Evidence Center
	try:
		current = config['CURRENT']['bec']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[17].text, 'html.parser')
			version = soup.text.strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['BEC', current, version, ''])
		else:
			table.append(['BEC', current, version, 'Update available!'])
	
	
	### CAINE
	try:
		current = config['CURRENT']['caine']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[18].text, 'html.parser')
			version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['CAINE', current, version, ''])
		else:
			table.append(['CAINE', current, version, 'Update available!'])
	
	
	### DEFT
	try:
		current = config['CURRENT']['deft']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[19].text, 'html.parser')
			version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['DEFT', current, version, ''])
		else:
			table.append(['DEFT', current, version, 'Update available!'])
	
	
	### Forensic Falcon Neo
	try:
		current = config['CURRENT']['ffn']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[20].text, 'html.parser')
			version = soup.find('table', {'class': 'datatableblue'}).findAll('tr')[2].findAll('td')[1].text.strip()
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Forensic Falcon Neo', current, version, ''])
		else:
			table.append(['Forensic Falcon Neo', current, version, 'Update available!'])
	
	
	### Atola TaskForce
	try:
		current = config['CURRENT']['atola']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[21].text, 'html.parser')
			version = soup.select_one('a[href^="http://dl.atola.com/taskforce/"]').text.strip()
			version = version.replace('Download ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Atola TaskForce', current, version, ''])
		else:
			table.append(['Atola TaskForce', current, version, 'Update available!'])
	
	
	### Forensic Email Collector
	try:
		current = config['CURRENT']['fec']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[22].text, 'html.parser')
			version = soup.select_one('h4').text.strip()
			version = version.split(' ')[0]
			version = version.replace('v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Forensic Email Collector', current, version, ''])
		else:
			table.append(['Forensic Email Collector', current, version, 'Update available!'])
	
	
	### VeraCrypt
	try:
		current = config['CURRENT']['veracrypt']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[23].text, 'html.parser')
			version = soup.select_one('h3').text.strip()
			version = version.replace('Latest Stable Release - ','')
			version = version.split(' ')[0]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['VeraCrypt', current, version, ''])
		else:
			table.append(['VeraCrypt', current, version, 'Update available!'])
	
	
	### Autopsy
	try:
		current = config['CURRENT']['autopsy']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[24].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('Autopsy ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Autopsy', current, version, ''])
		else:
			table.append(['Autopsy', current, version, 'Update available!'])
	
	
	### The Sleuth Kit
	try:
		current = config['CURRENT']['sleuthkit']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[25].text, 'html.parser')
			version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
			version = version.replace('The Sleuth Kit ','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['The Sleuth Kit', current, version, ''])
		else:
			table.append(['The Sleuth Kit', current, version, 'Update available!'])
	
	
	### Mount Image Pro
	try:
		current = config['CURRENT']['mountimagepro']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[26].text, 'html.parser')
			version = soup.select_one('a[href^="http://download.getdata.com/support/mip/MountImagePro"]')['href']
			version = version[version.index('(v'):]
			version = version[2:-5]
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['Mount Image Pro', current, version, ''])
		else:
			table.append(['Mount Image Pro', current, version, 'Update available!'])
	
	
	### NetAnalysis
	try:
		current = config['CURRENT']['netanalysis']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[27].text, 'html.parser')
			version = soup.find('span', {'class': 'avia_iconbox_title'}).text.strip()
			version = version.replace('Download NetAnalysis v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['NetAnalysis', current, version, ''])
		else:
			table.append(['NetAnalysis', current, version, 'Update available!'])
	
	
	### HstEx
	try:
		current = config['CURRENT']['hstex']
	except:
		current = ''
	if (current != ''):
		try:
			soup = BeautifulSoup(response[28].text, 'html.parser')
			version = soup.find('span', {'class': 'avia_iconbox_title'}).text.strip()
			version = version.replace('Download HstEx v','')
		except:
			version = 'Error'
		if ((current == version) or (version == 'Error')):
			table.append(['HstEx', current, version, ''])
		else:
			table.append(['HstEx', current, version, 'Update available!'])

		
	print(tabulate(table, headers=table_headers, disable_numparse=True))
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[12].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version == '1.7'
	if (version == '1.7'):
		pass
	else:
		print('')
		print('FVC update available!')

def current_save():
	config['CURRENT']['gui'] = gui_option.get()
	try:
		config['CURRENT']['encase'] = encase_current.get()
	except:
		pass
	try:
		config['CURRENT']['blacklight'] = blacklight_current.get()
	except:
		pass
	try:
		config['CURRENT']['macquisition'] = macquisition_current.get()
	except:
		pass
	try:
		config['CURRENT']['axiom'] = axiom_current.get()
	except:
		pass
	try:
		config['CURRENT']['ufed4pc'] = ufed4pc_current.get()
	except:
		pass
	try:
		config['CURRENT']['physicalanalyzer'] = physicalanalyzer_current.get()
	except:
		pass
	try:
		config['CURRENT']['osf'] = osf_current.get()
	except:
		pass
	try:
		config['CURRENT']['forensicexplorer'] = forensicexplorer_current.get()
	except:
		pass
	try:
		config['CURRENT']['usbdetective'] = usbdetective_current.get()
	except:
		pass
	try:
		config['CURRENT']['ftk'] = ftk_current.get()
	except:
		pass
	try:
		config['CURRENT']['ftkimager'] = ftkimager_current.get()
	except:
		pass
	try:
		config['CURRENT']['xamn'] = xamn_current.get()
	except:
		pass
	try:
		config['CURRENT']['xways'] = xways_current.get()
	except:
		pass
	try:
		config['CURRENT']['cyberchef'] = cyberchef_current.get()
	except:
		pass
	try:
		config['CURRENT']['nsrl'] = nsrl_current.get()
	except:
		pass
	try:
		config['CURRENT']['aim'] = aim_current.get()
	except:
		pass
	try:
		config['CURRENT']['passware'] = passware_current.get()
	except:
		pass
	try:
		config['CURRENT']['hashcat'] = hashcat_current.get()
	except:
		pass
	try:
		config['CURRENT']['exiftool'] = exiftool_current.get()
	except:
		pass
	try:
		config['CURRENT']['bec'] = bec_current.get()
	except:
		pass
	try:
		config['CURRENT']['caine'] = caine_current.get()
	except:
		pass
	try:
		config['CURRENT']['deft'] = deft_current.get()
	except:
		pass
	try:
		config['CURRENT']['ffn'] = ffn_current.get()
	except:
		pass
	try:
		config['CURRENT']['atola'] = atola_current.get()
	except:
		pass
	try:
		config['CURRENT']['fec'] = fec_current.get()
	except:
		pass
	try:
		config['CURRENT']['veracrypt'] = veracrypt_current.get()
	except:
		pass
	try:
		config['CURRENT']['autopsy'] = autopsy_current.get()
	except:
		pass
	try:
		config['CURRENT']['sleuthkit'] = sleuthkit_current.get()
	except:
		pass
	try:
		config['CURRENT']['mountimagepro'] = mountimagepro_current.get()
	except:
		pass
	try:
		config['CURRENT']['netanalysis'] = netanalysis_current.get()
	except:
		pass
	try:
		config['CURRENT']['hstex'] = hstex_current.get()
	except:
		pass
	with open('current_versions.ini', 'w') as configfile:
		config.write(configfile)
	current_save.configure(text='Checking for updates...', state='disabled')
	gui_toggle.configure(state='disabled')
	latest_update()
	current_save.configure(text='Current versions saved', state='normal')
	gui_toggle.configure(state='normal')

def about_box():
	messagebox.showinfo('About', 'Forensic Version Checker v1.7\n\n\
Tool\'s homepage:\nhttps://github.com/jankais3r/Forensic-Version-Checker\n\n\
Digital Forensics Discord:\nhttps://discord.gg/pNMZunG')

try:
	if (config['CURRENT']['gui'] == '1' or config['CURRENT']['gui'] == 'Display all'):
		gui = 'Display all'
	elif config['CURRENT']['gui'] == 'Display used':
		gui = 'Display used'
	else:
		gui = 'CLI mode'
except:
	gui = 'Display all'

if gui != 'CLI mode':
	window = Tk()
	window.title('Forensic Version Checker')
	
	icon = 'iVBORw0KGgoAAAANSUhEUgAAASwAAAEsCAMAAABOo35HAAACYVBMVEUAAAAA/wCA/4BV/1WA/0Bm/zOA/1Vt/0mA/0Bx/zmA/010/0aA/0B2/zuA/0l3/0SA/0B4/zyA\
/0d5/0OA/0B5/z2A80Z69EOA9EB69T2A9UV79kKA9kB79j5790KA90B89z6A+ER8+EKA+EB8+D55+EN8+EF8+T55+UN9+UF6+UB9+T56+UN9+kF6+kB9+j57+kB9+kN9+kF9+0N7\
+0J9+0F7+0B7+0J9+0F890B+90N890J8+EB8+EJ++EF8+EB8+EF8+EB7+EJ8+EF7+UF7+UJ8+UF7+UF8+UB7+UJ9+UB9+UF7+UB9+UB7+kJ9+kF7+kB9+kB9+kF9+kB9+kF8+kB8\
+kJ9+kF9+EJ7+EF8+EB7+EJ7+UF7+UJ7+UF8+UB8+UF7+UF8+UJ9+UF8+UF9+UB8+UJ9+UF8+UF9+UB8+UJ9+UF8+UF8+kJ9+kF8+kJ9+kF8+kF8+kF7+EF8+EF8+EF8+EF7+EJ8\
+UF8+UF8+UF8+UF8+UJ8+UF8+UF8+UF8+UF9+UF8+UJ9+UF8+UF9+UB8+UJ9+UF8+UF9+UB8+UJ9+UF8+UF7+UB7+UF8+UF7+kB8+kF8+kF8+kF8+EF8+EF8+EB8+EF8+EF8+UF8\
+UB8+UF8+UF8+UB8+UF8+UF8+UJ8+UF8+UJ8+UF8+UJ9+UF9+UF8+UJ7+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+kF8+kF8+EF8+EF8+UF8+UF8+UF8+UF8+UF8+UF8\
+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UF8+UH////fFht9AAAAyXRSTlMAAQIDBAUGBwgJCgsMDQ4PEBESExQVFhcYGRobHB0fICEiIyQlJicpKissLS4v\
MDE0NTc5Ojs8Pj9AQUJERkdISkxNTk9RUlNUVVhaW1xdXl9gYmRmZ2lqbG5vdHZ4ent9foCBgoOEhYaHiImKjI2QkZKUlZaYmpueoKGio6Slpqiqq6ytrq+wsbKztLW2uLm6u72/\
wMHCw8TFxsfIyszNzs/S1NbX2drb3uDh4uPk5ebn6Onq6+zt7u/w8fLz9PX29/j5+vv8/f64aNKjAAAAAWJLR0TK87Q25gAABpZJREFUeNrt3ftbFFUcgPGDiBCYJYoX1LTI1Mgi\
8VqYpamtaBkqFmmlppVZKUqS2R0ttQumdvFuIKUIKpmCmAsLLHz/q37QeQR2Z+bMsFxm531/dZ+zZz8unOXszlmliIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIiIj6p0ETcvIC\
cV9ezoRBPZWate1si/ikljMf5LqXSll7XnxWZWGKux+/VVfFh10pcPHj+PBJ8WnHJzq1eu6m+Lb6PGdWi1vEx4VedGK1JCy+rvV5favs2+Lzbk3VtUqrFN9XkaqJVYyVyMd6VtPD\
UIm0Pa6FdQApEZH9OlaTO4ASEWnP0sB6H6c7bdbAqoLp7h/V9lYTUTIab4u1DCSjgC3WJpCMNthi7QHJqNQW6zuQjPbZYpWDZFRui3UYJKPDYIEFFlhggQUWWGCBBRZYYPVb7XV/\
nq0JgWVfcOcLDyqlVOqiT0NgWT+pPsq4N5Xxxe1gmVf7TNfJzK0Gy6xj6d1nM/wXsKL3eXLkdAaXgBWtjQlRJ1TUDlb3Wl41m9FLTWB1reFZ8ynl/gNW5/561PJj5ufButdvI6wn\
lX4ULKMvk+1mNWQvWJbLYJcSNnaAJdJaoPdR15UtYN3UvvZj1r9+x7o4Tf9ahqwqf2OdGuPkKpkRv/oZa3+as+uvkr/wL5bOMth9UfQpVusqNxfYFrT6Eatxvrsrt/Ma/IdVne32\
OvdpF/2GdXqs+1MBxpzyF9b3aaoHpXzlJ6ztiT07m6NvFsUBgdW2uueHvqxq8wdW44JYHJEzv9EPWJeeiM2BQtnV8Y91JjNWxy9lno53rINDY3dYVdqB+MYqTlQxLHFHHGO1F8X6\
JLSicLxiBRfH/ty4BbfiE+vq071xyt70mnjEOjeud84kHHc2/rB+uL+3TnAceijesHYN7r3zLhN3xhVW7JfBvvhYUv9gNS1VvdySYLxg1c1Qvd6MuvjAqpyk+qBJlfGA9cdIvf28\
BOf/0qWRv3sfq0RvGUwtu890E7lM70i5mH9Wt6+xdJfB0SfFHEtOju6XRbGPsXQ/TpRVJVZYUpWlN05s34HtW6zmhXqPcfZ1scaS67P1RloU8ipWWHOXIT8kdlgSytcba2nYo1hv\
az28Qdvv3NoaS2S73mnaG72J9XeSzoMbYpxBZYcle4ZojXfBk1haH5JJPyK6WHIkXWfENV7ECursyUy59zywx5ILUzSGHNbkQax9Gg9s5jVxgiXXZmoMesCDWBrHfK7p/B68Dpa0\
rbEf9T0PYq3WXQadYOksioUexFppc0dJpeIGS0rtFtkCD2Kts76fUSfEHZacGGU98psexNrhcPtJG8tug2yXB7GqrO5lXr24x5L6eVZjX/AgljxifieBKK+FHGBJk8VJvo958hV8\
senW59Zol8M5wZKOrabbpyWexAqabNkl7Y56c0dYIrtNFsWxzd7cdTgU9X8/47jEAkuOZ0R91v7o1c2/aC+3J1ZIbLCkItp3eq317E5peHnE8HNvSKyw5MbciNuuCHsWS1q6r1oB\
83eOnWNJsPvwyzy8By8iJZ3fxkr70OKqcBdY0rGt85UaaZ94/X3DmjeGGRtNRZetbugGS6T2dWP4B9ZdFq9jiQR/Xh8I5L97yGZTzh2WSPDglvxAYH157D8aMoBPOXKL1XuBBRZY\
YIEFFlhggQUWWGCBBRZYYIEFFlhggQUWWGCBBRZYYIEFFlhggQUWWGCBBRZYYIEFFlhggQUWWGCBBRZYYIEFFlhggRUfWKZf4pcKVkQZpidtgRXRk2YzegqsiJabzehlsCL62mxG\
34IV0X8my2FqEKzICqNP6DUBK7L6qOvh2Eawov7WinJea2KZgBW1zyKOckvYK2CZPbeGd51M+jcClmmXlnc69zBpRY2AZVX1pjlDlFIqec6mS/08lYGPJSKh2nPnakP9Pw9PYA2U\
wAILLLDAAovAAgsssMDyLVY5SEbltlj7QTIqs8XaA5JRqS3WBpCM3rLFWgaSUcAWKxOku3VofC96FUx3qrS34peW/q8spSaFcRIRaXtIA4sXD7ovHJRSakorUiItk7WwYvfdwl7u\
HT0rlVaJVUWqJpbKvu13q1tTlXbzmv1t1TxHOWhRk5+tgguVo2bX+dfqSq5y2Bjf7gL+NFo5LuGVq758Wq1QrkpZe953fzwXpijXzdpyrMEvUA1HN+eqnpaZk+eDcjIVERERERER\
EREREREREREREREREREREREREREREVE/9T95hAEFoC4rDwAAAABJRU5ErkJggg==' # https://thenounproject.com/term/update/2827723/
	icon = base64.b64decode(icon)
	icon = PhotoImage(data=icon)
	window.tk.call('wm', 'iconphoto', window._w, icon)
	
	if os.name == 'nt':
		fontsize = 9
	else:
		fontsize = 10
		
	rowID = 0
	tool = Label(window, text='Tool', font=('TkDefaultFont', fontsize, 'underline'), padx=5, pady=3)
	tool.grid(column=0, row=rowID, sticky=W)
	current = Label(window, text='Current Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
	current.grid(column=1, row=rowID)
	latest = Label(window, text='Latest Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
	latest.grid(column=2, row=rowID)
	latest = Label(window, text='Update', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
	latest.grid(column=3, row=rowID, padx=(0,10))
	rowID += 1
	
	### EnCase
	try:
		current = config['CURRENT']['encase']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		encase = Label(window, text='EnCase', padx=5)
		encase.grid(column=0, row=rowID, sticky=W)
		encase_current = Entry(window, width=8)
		encase_current.grid(column=rowID, row=rowID, sticky=N+S+E+W)
		encase_current.insert(0,current)
		encase_latest = Entry(window, width=8, state='readonly')
		encase_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		encase_update = Label(text='', padx=2)
		encase_update.grid(column=3, row=rowID, padx=(0,10))
		encase_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.guidancesoftware.com/encase-forensic'))
		rowID += 1
	
	### BlackLight
	try:
		current = config['CURRENT']['blacklight']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		blacklight = Label(window, text='BlackLight', padx=5)
		blacklight.grid(column=0, row=rowID, sticky=W)
		blacklight_current = Entry(window, width=8)
		blacklight_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		blacklight_current.insert(0,current)
		blacklight_latest = Entry(window, width=8, state='readonly')
		blacklight_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		blacklight_update = Label(text='')
		blacklight_update.grid(column=3, row=rowID, padx=(0,10))
		blacklight_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.blackbagtech.com/downloads/'))
		rowID += 1
	
	### MacQuisition
	try:
		current = config['CURRENT']['macquisition']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		macquisition = Label(window, text='MacQuisition', padx=5)
		macquisition.grid(column=0, row=rowID, sticky=W)
		macquisition_current = Entry(window, width=8)
		macquisition_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		macquisition_current.insert(0,current)
		macquisition_latest = Entry(window, width=8, state='readonly')
		macquisition_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		macquisition_update = Label(text='')
		macquisition_update.grid(column=3, row=rowID, padx=(0,10))
		macquisition_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.blackbagtech.com/downloads/'))
		rowID += 1
	
	### AXIOM
	try:
		current = config['CURRENT']['axiom']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		axiom = Label(window, text='AXIOM', padx=5)
		axiom.grid(column=0, row=rowID, sticky=W)
		axiom_current = Entry(window, width=8)
		axiom_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		axiom_current.insert(0,current)
		axiom_latest = Entry(window, width=8, state='readonly')
		axiom_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		axiom_update = Label(text='')
		axiom_update.grid(column=3, row=rowID, padx=(0,10))
		axiom_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.magnetforensics.com/downloadaxiom/'))
		rowID += 1
	
	### UFED4PC
	try:
		current = config['CURRENT']['ufed4pc']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		ufed4pc = Label(window, text='UFED 4PC', padx=5)
		ufed4pc.grid(column=0, row=rowID, sticky=W)
		ufed4pc_current = Entry(window, width=8)
		ufed4pc_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		ufed4pc_current.insert(0,current)
		ufed4pc_latest = Entry(window, width=8, state='readonly')
		ufed4pc_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		ufed4pc_update = Label(text='')
		ufed4pc_update.grid(column=3, row=rowID, padx=(0,10))
		ufed4pc_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.cellebrite.com/en/support/product-releases/'))
		rowID += 1
	
	### Physical Analyzer
	try:
		current = config['CURRENT']['physicalanalyzer']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		physicalanalyzer = Label(window, text='Physical Analyzer', padx=5)
		physicalanalyzer.grid(column=0, row=rowID, sticky=W)
		physicalanalyzer_current = Entry(window, width=8)
		physicalanalyzer_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		physicalanalyzer_current.insert(0,current)
		physicalanalyzer_latest = Entry(window, width=8, state='readonly')
		physicalanalyzer_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		physicalanalyzer_update = Label(text='')
		physicalanalyzer_update.grid(column=3, row=rowID, padx=(0,10))
		physicalanalyzer_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.cellebrite.com/en/support/product-releases/'))
		rowID += 1
	
	### OSForensics
	try:
		current = config['CURRENT']['osf']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		osf = Label(window, text='OSForensics', padx=5)
		osf.grid(column=0, row=rowID, sticky=W)
		osf_current = Entry(window, width=8)
		osf_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		osf_current.insert(0,current)
		osf_latest = Entry(window, width=8, state='readonly')
		osf_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		osf_update = Label(text='')
		osf_update.grid(column=3, row=rowID, padx=(0,10))
		osf_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.osforensics.com/download.html'))
		rowID += 1
	
	### ForensicExplorer
	try:
		current = config['CURRENT']['forensicexplorer']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		forensicexplorer = Label(window, text='ForensicExplorer', padx=5)
		forensicexplorer.grid(column=0, row=rowID, sticky=W)
		forensicexplorer_current = Entry(window, width=8)
		forensicexplorer_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		forensicexplorer_current.insert(0,current)
		forensicexplorer_latest = Entry(window, width=8, state='readonly')
		forensicexplorer_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		forensicexplorer_update = Label(text='')
		forensicexplorer_update.grid(column=3, row=rowID, padx=(0,10))
		forensicexplorer_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.forensicexplorer.com/download.php'))
		rowID += 1
	
	### USB Detective
	try:
		current = config['CURRENT']['usbdetective']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		usbdetective = Label(window, text='USB Detective', padx=5)
		usbdetective.grid(column=0, row=rowID, sticky=W)
		usbdetective_current = Entry(window, width=8)
		usbdetective_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		usbdetective_current.insert(0,current)
		usbdetective_latest = Entry(window, width=8, state='readonly')
		usbdetective_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		usbdetective_update = Label(text='')
		usbdetective_update.grid(column=3, row=rowID, padx=(0,10))
		usbdetective_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://usbdetective.com/release-notes/'))
		rowID += 1
	
	### FTK
	try:
		current = config['CURRENT']['ftk']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		ftk = Label(window, text='FTK', padx=5)
		ftk.grid(column=0, row=rowID, sticky=W)
		ftk_current = Entry(window, width=8)
		ftk_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		ftk_current.insert(0,current)
		ftk_latest = Entry(window, width=8, state='readonly')
		ftk_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		ftk_update = Label(text='')
		ftk_update.grid(column=3, row=rowID, padx=(0,10))
		ftk_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://accessdata.com/product-download'))
		rowID += 1
	
	### FTK Imager
	try:
		current = config['CURRENT']['ftkimager']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		ftkimager = Label(window, text='FTK Imager', padx=5)
		ftkimager.grid(column=0, row=rowID, sticky=W)
		ftkimager_current = Entry(window, width=8)
		ftkimager_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		ftkimager_current.insert(0,current)
		ftkimager_latest = Entry(window, width=8, state='readonly')
		ftkimager_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		ftkimager_update = Label(text='')
		ftkimager_update.grid(column=3, row=rowID, padx=(0,10))
		ftkimager_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://accessdata.com/product-download'))
		rowID += 1
	
	### XAMN
	try:
		current = config['CURRENT']['xamn']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		xamn = Label(window, text='XAMN', padx=5)
		xamn.grid(column=0, row=rowID, sticky=W)
		xamn_current = Entry(window, width=8)
		xamn_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		xamn_current.insert(0,current)
		xamn_latest = Entry(window, width=8, state='readonly')
		xamn_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		xamn_update = Label(text='')
		xamn_update.grid(column=3, row=rowID, padx=(0,10))
		xamn_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.msab.com/downloads/'))
		rowID += 1
	
	### X-Ways
	try:
		current = config['CURRENT']['xways']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		xways = Label(window, text='X-Ways', padx=5)
		xways.grid(column=0, row=rowID, sticky=W)
		xways_current = Entry(window, width=8)
		xways_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		xways_current.insert(0,current)
		xways_latest = Entry(window, width=8, state='readonly')
		xways_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		xways_update = Label(text='')
		xways_update.grid(column=3, row=rowID, padx=(0,10))
		xways_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.x-ways.net/winhex/license.html'))
		rowID += 1
	
	### CyberChef
	try:
		current = config['CURRENT']['cyberchef']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		cyberchef = Label(window, text='CyberChef', padx=5)
		cyberchef.grid(column=0, row=rowID, sticky=W)
		cyberchef_current = Entry(window, width=8)
		cyberchef_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		cyberchef_current.insert(0,current)
		cyberchef_latest = Entry(window, width=8, state='readonly')
		cyberchef_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		cyberchef_update = Label(text='')
		cyberchef_update.grid(column=3, row=rowID, padx=(0,10))
		cyberchef_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/gchq/CyberChef/releases/latest'))
		rowID += 1
	
	### NSRL
	try:
		current = config['CURRENT']['nsrl']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		nsrl = Label(window, text='NSRL hash set', padx=5)
		nsrl.grid(column=0, row=rowID, sticky=W)
		nsrl_current = Entry(window, width=8)
		nsrl_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		nsrl_current.insert(0,current)
		nsrl_latest = Entry(window, width=8, state='readonly')
		nsrl_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		nsrl_update = Label(text='')
		nsrl_update.grid(column=3, row=rowID, padx=(0,10))
		nsrl_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds'))
		rowID += 1
	
	### Arsenal Image Mounter
	try:
		current = config['CURRENT']['aim']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		aim = Label(window, text='AIM', padx=5)
		aim.grid(column=0, row=rowID, sticky=W)
		aim_current = Entry(window, width=8)
		aim_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		aim_current.insert(0,current)
		aim_latest = Entry(window, width=8, state='readonly')
		aim_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		aim_update = Label(text='')
		aim_update.grid(column=3, row=rowID, padx=(0,10))
		aim_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://arsenalrecon.com/downloads/'))
		rowID += 1
	
	### Passware
	try:
		current = config['CURRENT']['passware']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		passware = Label(window, text='Passware', padx=5)
		passware.grid(column=0, row=rowID, sticky=W)
		passware_current = Entry(window, width=8)
		passware_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		passware_current.insert(0,current)
		passware_latest = Entry(window, width=8, state='readonly')
		passware_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		passware_update = Label(text='')
		passware_update.grid(column=3, row=rowID, padx=(0,10))
		passware_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.passware.com/kit-forensic/whatsnew/'))
		rowID += 1
	
	### hashcat
	try:
		current = config['CURRENT']['hashcat']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		hashcat = Label(window, text='hashcat', padx=5)
		hashcat.grid(column=0, row=rowID, sticky=W)
		hashcat_current = Entry(window, width=8)
		hashcat_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		hashcat_current.insert(0,current)
		hashcat_latest = Entry(window, width=8, state='readonly')
		hashcat_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		hashcat_update = Label(text='')
		hashcat_update.grid(column=3, row=rowID, padx=(0,10))
		hashcat_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://hashcat.net/beta/'))
		rowID += 1
	
	### ExifTool
	try:
		current = config['CURRENT']['exiftool']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		exiftool = Label(window, text='ExifTool', padx=5)
		exiftool.grid(column=0, row=rowID, sticky=W)
		exiftool_current = Entry(window, width=8)
		exiftool_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		exiftool_current.insert(0,current)
		exiftool_latest = Entry(window, width=8, state='readonly')
		exiftool_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		exiftool_update = Label(text='')
		exiftool_update.grid(column=3, row=rowID, padx=(0,10))
		exiftool_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://owl.phy.queensu.ca/~phil/exiftool/'))
		rowID += 1
	
	### Belkasoft Evidence Center
	try:
		current = config['CURRENT']['bec']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		bec = Label(window, text='BEC', padx=5)
		bec.grid(column=0, row=rowID, sticky=W)
		bec_current = Entry(window, width=8)
		bec_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		bec_current.insert(0,current)
		bec_latest = Entry(window, width=8, state='readonly')
		bec_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		bec_update = Label(text='')
		bec_update.grid(column=3, row=rowID, padx=(0,10))
		bec_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://belkasoft.com/get'))
		rowID += 1
	
	### CAINE
	try:
		current = config['CURRENT']['caine']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		caine = Label(window, text='CAINE', padx=5)
		caine.grid(column=0, row=rowID, sticky=W)
		caine_current = Entry(window, width=8)
		caine_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		caine_current.insert(0,current)
		caine_latest = Entry(window, width=8, state='readonly')
		caine_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		caine_update = Label(text='')
		caine_update.grid(column=3, row=rowID, padx=(0,10))
		caine_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.caine-live.net/'))
		rowID += 1
	
	### DEFT
	try:
		current = config['CURRENT']['deft']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		deft = Label(window, text='DEFT', padx=5)
		deft.grid(column=0, row=rowID, sticky=W)
		deft_current = Entry(window, width=8)
		deft_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		deft_current.insert(0,current)
		deft_latest = Entry(window, width=8, state='readonly')
		deft_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		deft_update = Label(text='')
		deft_update.grid(column=3, row=rowID, padx=(0,10))
		deft_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://na.mirror.garr.it/mirrors/deft/zero/'))
		rowID += 1
	
	### Forensic Falcon Neo
	try:
		current = config['CURRENT']['ffn']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		ffn = Label(window, text='Forensic Falcon Neo', padx=5)
		ffn.grid(column=0, row=rowID, sticky=W)
		ffn_current = Entry(window, width=8)
		ffn_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		ffn_current.insert(0,current)
		ffn_latest = Entry(window, width=8, state='readonly')
		ffn_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		ffn_update = Label(text='')
		ffn_update.grid(column=3, row=rowID, padx=(0,10))
		ffn_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.logicube.com/knowledge/forensic-falcon-neo/'))
		rowID += 1
	
	### Atola TaskForce
	try:
		current = config['CURRENT']['atola']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		atola = Label(window, text='Atola TaskForce', padx=5)
		atola.grid(column=0, row=rowID, sticky=W)
		atola_current = Entry(window, width=8)
		atola_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		atola_current.insert(0,current)
		atola_latest = Entry(window, width=8, state='readonly')
		atola_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		atola_update = Label(text='')
		atola_update.grid(column=3, row=rowID, padx=(0,10))
		atola_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://atola.com/products/taskforce/download.html'))
		rowID += 1
	
	### Forensic Email Collector
	try:
		current = config['CURRENT']['fec']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		fec = Label(window, text='Forensic Email Collector', padx=5)
		fec.grid(column=0, row=rowID, sticky=W)
		fec_current = Entry(window, width=8)
		fec_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		fec_current.insert(0,current)
		fec_latest = Entry(window, width=8, state='readonly')
		fec_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		fec_update = Label(text='')
		fec_update.grid(column=3, row=rowID, padx=(0,10))
		fec_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.metaspike.com/fec-change-log/'))
		rowID += 1
	
	### VeraCrypt
	try:
		current = config['CURRENT']['veracrypt']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		veracrypt = Label(window, text='VeraCrypt', padx=5)
		veracrypt.grid(column=0, row=rowID, sticky=W)
		veracrypt_current = Entry(window, width=8)
		veracrypt_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		veracrypt_current.insert(0,current)
		veracrypt_latest = Entry(window, width=8, state='readonly')
		veracrypt_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		veracrypt_update = Label(text='')
		veracrypt_update.grid(column=3, row=rowID, padx=(0,10))
		veracrypt_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.veracrypt.fr/en/Downloads.html'))
		rowID += 1
	
	### Autopsy
	try:
		current = config['CURRENT']['autopsy']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		autopsy = Label(window, text='Autopsy', padx=5)
		autopsy.grid(column=0, row=rowID, sticky=W)
		autopsy_current = Entry(window, width=8)
		autopsy_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		autopsy_current.insert(0,current)
		autopsy_latest = Entry(window, width=8, state='readonly')
		autopsy_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		autopsy_update = Label(text='')
		autopsy_update.grid(column=3, row=rowID, padx=(0,10))
		autopsy_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/sleuthkit/autopsy/releases/latest'))
		rowID += 1
	
	### The Sleuth Kit
	try:
		current = config['CURRENT']['sleuthkit']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		sleuthkit = Label(window, text='The Sleuth Kit', padx=5)
		sleuthkit.grid(column=0, row=rowID, sticky=W)
		sleuthkit_current = Entry(window, width=8)
		sleuthkit_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		sleuthkit_current.insert(0,current)
		sleuthkit_latest = Entry(window, width=8, state='readonly')
		sleuthkit_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		sleuthkit_update = Label(text='')
		sleuthkit_update.grid(column=3, row=rowID, padx=(0,10))
		sleuthkit_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/sleuthkit/sleuthkit/releases/latest'))
		rowID += 1
	
	### Mount Image Pro
	try:
		current = config['CURRENT']['mountimagepro']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		mountimagepro = Label(window, text='Mount Image Pro', padx=5)
		mountimagepro.grid(column=0, row=rowID, sticky=W)
		mountimagepro_current = Entry(window, width=8)
		mountimagepro_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		mountimagepro_current.insert(0,current)
		mountimagepro_latest = Entry(window, width=8, state='readonly')
		mountimagepro_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		mountimagepro_update = Label(text='')
		mountimagepro_update.grid(column=3, row=rowID, padx=(0,10))
		mountimagepro_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.forensicexplorer.com/download.php'))
		rowID += 1
	
	### NetAnalysis
	try:
		current = config['CURRENT']['netanalysis']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		netanalysis = Label(window, text='NetAnalysis', padx=5)
		netanalysis.grid(column=0, row=rowID, sticky=W)
		netanalysis_current = Entry(window, width=8)
		netanalysis_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		netanalysis_current.insert(0,current)
		netanalysis_latest = Entry(window, width=8, state='readonly')
		netanalysis_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		netanalysis_update = Label(text='')
		netanalysis_update.grid(column=3, row=rowID, padx=(0,10))
		netanalysis_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.digital-detective.net/start/netanalysis-quick-start/'))
		rowID += 1
	
	### HstEx
	try:
		current = config['CURRENT']['hstex']
	except:
		current = ''
	if (gui == 'Display all' or current != ''):
		hstex = Label(window, text='HstEx', padx=5)
		hstex.grid(column=0, row=rowID, sticky=W)
		hstex_current = Entry(window, width=8)
		hstex_current.grid(column=1, row=rowID, sticky=N+S+E+W)
		hstex_current.insert(0,current)
		hstex_latest = Entry(window, width=8, state='readonly')
		hstex_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
		hstex_update = Label(text='')
		hstex_update.grid(column=3, row=rowID, padx=(0,10))
		hstex_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.digital-detective.net/start/hstex-quick-start/'))
		rowID += 1
	
	gui_option = StringVar()
	gui_option.set(gui)
	gui_toggle = OptionMenu(window, gui_option, 'Display all', 'Display used', 'CLI mode')
	gui_toggle.grid(column=0, row=rowID, sticky=N+S+W, padx=(5), pady=(7,7))
	
	current_save = Button(window, text='Save', command=current_save)
	current_save.grid(column=1, row=rowID, columnspan=2, sticky=N+S+E+W, pady=(7,7))
	
	about = Label(window, text='?', padx=5, fg='grey', cursor='hand2')
	about.grid(column=3, row=rowID, pady=(7,7))
	about.bind('<ButtonRelease-1>', lambda e: about_box())
	
	if first_run != True:
		current_save.configure(text='Checking for updates...', state='disabled')
		gui_toggle.configure(state='disabled')
		latest_update()
		current_save.configure(text='Save', state='normal')
		gui_toggle.configure(state='normal')
	else:
		messagebox.showinfo('Welcome', 'New config file has been created.\n\n\
Please populate your current tool versions,\nchoose a display mode and click Save.')
	
	if gui == 'Display all':
		tab_order = (encase_current, blacklight_current, macquisition_current, axiom_current, ufed4pc_current, physicalanalyzer_current, osf_current, forensicexplorer_current,\
		usbdetective_current, ftk_current, ftkimager_current, xamn_current, xways_current, cyberchef_current, nsrl_current, aim_current, passware_current, hashcat_current,\
		exiftool_current, bec_current, caine_current, deft_current, ffn_current, atola_current, fec_current, veracrypt_current, autopsy_current, sleuthkit_current,\
		mountimagepro_current, netanalysis_current, hstex_current)
		for widget in tab_order:
			widget.lift()
	
	window.mainloop()
else:
	cli_update()
	