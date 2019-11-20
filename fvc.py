#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import queue
import grequests
import webbrowser
import configparser
from tkinter import *
from threading import Thread
from bs4 import BeautifulSoup
from tkinter import messagebox


if os.path.isfile('current_versions.ini') == False:
	default_config = """[CURRENT]
gui = 1
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

def crawl():
	ua_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
	}
	
	urls = ['https://www.guidancesoftware.com/encase-forensic',
			'https://www.blackbagtech.com/downloads/',
			'https://www.magnetforensics.com/downloadaxiom/',
			'https://www.cellebrite.com/en/support/product-releases/',
			'https://www.osforensics.com/whatsnew.html',
			'http://www.forensicexplorer.com/download.php',
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
			'http://www.metaspike.com/fec-change-log/'
		]
	mt_queue.put(grequests.map((grequests.get(u, headers=ua_headers) for u in urls), size=5))

def latest_update():
	thread = Thread(target=crawl)
	thread.start()
	while(thread.is_alive()):
		time.sleep(0.1)
		window.update()
		
	response = mt_queue.get()
	
	### EnCase
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
	
	### OSF
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
		soup = BeautifulSoup(response[5].text, 'html.parser')
		version = soup.select_one('a[href$=".exe"]')['href']
		version = version[version.index('(v'):]
		version = version[2:-5]
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
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[12].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version == '1.5'
	if version != '1.5':
		about.configure(text='Update FVC', fg='blue', cursor='hand2')
		about.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'))
	
	### Arsenal Image Mounter
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
		
def cli_update():
	thread = Thread(target=crawl)
	thread.start()
	response = mt_queue.get()
	
	print('Tool				Current Version		Latest Version		Update?')
	
	### EnCase
	try:
		soup = BeautifulSoup(response[0].text, 'html.parser')
		version = soup.select_one('h3').text.strip()
		version = version.replace('EnCase Forensic ','')
		version = version.split(':')[0]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['encase']
		if (current != ''):
			if (current == version):
				print('Encase				'+current+'			'+version)
			else:
				print('Encase				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### BlackLight
	try:
		soup = BeautifulSoup(response[1].text, 'html.parser')
		version = soup.find('dl', {'id': 'blacklightrevision'}).select_one('span').text.strip()
		version = version.replace('BlackLight ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['blacklight']
		if (current != ''):
			if (current == version):
				print('BlackLight			'+current+'			'+version)
			else:
				print('BlackLight			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### MacQuisition
	try:
		soup = BeautifulSoup(response[1].text, 'html.parser')
		version = soup.find('dl', {'id': 'macquisitionrevision'}).select_one('span').text.strip()
		version = version.replace('MacQuisition ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['macquisition']
		if (current != ''):
			if (current == version):
				print('MacQuisition			'+current+'		'+version)
			else:
				print('MacQuisition			'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### AXIOM
	try:
		soup = BeautifulSoup(response[2].text, 'html.parser')
		version = soup.select_one('h2').text.strip()
		version = version.replace('MAGNET AXIOM ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['axiom']
		if (current != ''):
			if (current == version):
				print('AXIOM				'+current+'		'+version)
			else:
				print('AXIOM				'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### UFED 4PC
	try:
		soup = BeautifulSoup(response[3].text, 'html.parser')
		version = soup.find(text=re.compile('UFED.(4PC|Ultimate).')).parent.select_one('b').text.strip()
		version = version.replace('Version ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['ufed4pc']
		if (current != ''):
			if (current == version):
				print('UFED 4PC			'+current+'			'+version)
			else:
				print('UFED 4PC			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Physical Analyzer
	try:
		soup = BeautifulSoup(response[3].text, 'html.parser')
		version = soup.find(text=re.compile('(Physical|Logical).Analyzer.')).parent.select_one('b').text.strip()
		version = version.replace('Version ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['physicalanalyzer']
		if (current != ''):
			if (current == version):
				print('Physical Analyzer		'+current+'			'+version)
			else:
				print('Physical Analyzer		'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### OSF
	try:
		soup = BeautifulSoup(response[4].text, 'html.parser')
		version = soup.select_one('h4').text.strip()
		version = version.replace(' build ','.')
		version = version.split(' ')[0]
		version = version[1:]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['osf']
		if (current != ''):
			if (current == version):
				print('OSForensics			'+current+'		'+version)
			else:
				print('OSForensics			'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### ForensicExplorer
	try:
		soup = BeautifulSoup(response[5].text, 'html.parser')
		version = soup.select_one('a[href$=".exe"]')['href']
		version = version[version.index('(v'):]
		version = version[2:-5]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['forensicexplorer']
		if (current != ''):
			if (current == version):
				print('ForensicExplorer		'+current+'		'+version)
			else:
				print('ForensicExplorer		'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### USB Detective
	try:
		soup = BeautifulSoup(response[6].text, 'html.parser')
		version = soup.select_one('h2').text.strip()
		version = version.replace('Version ','')
		version = version.split(' ')[0]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['usbdetective']
		if (current != ''):
			if (current == version):
				print('USB Detective			'+current+'			'+version)
			else:
				print('USB Detective			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### FTK
	try:
		soup = BeautifulSoup(response[7].text, 'html.parser')
		version = soup.select_one('a[href^="http://accessdata.com/product-download/forensic-toolkit-ftk-version"]').parent.parent.select_one('h5').text.strip()
		version = version.replace('Forensic Toolkit (FTK) version ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['ftk']
		if (current != ''):
			if (current == version):
				print('FTK				'+current+'			'+version)
			else:
				print('FTK				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### FTK Imager
	try:
		soup = BeautifulSoup(response[7].text, 'html.parser')
		version = soup.select_one('a[href^="http://accessdata.com/product-download/ftk-imager-version"]').parent.parent.select_one('h5').text.strip()
		version = version.replace('FTK Imager version ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['ftkimager']
		if (current != ''):
			if (current == version):
				print('FTK Imager			'+current+'			'+version)
			else:
				print('FTK Imager			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### XAMN
	try:
		soup = BeautifulSoup(response[8].text, 'html.parser')
		version = soup.find('a', {'class': 'wpfd_downloadlink'})['title']
		version = version.replace('XAMN v','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['xamn']
		if (current != ''):
			if (current == version):
				print('XAMN				'+current+'			'+version)
			else:
				print('XAMN				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### X-Ways
	try:
		soup = BeautifulSoup(response[9].text, 'html.parser')
		version = soup.find('div', {'class': 'content'}).select_one('b').text.strip()
		version = version[19:].strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['xways']
		if (current != ''):
			if (current == version):
				print('X-Ways				'+current+'			'+version)
			else:
				print('X-Ways				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### CyberChef
	try:
		soup = BeautifulSoup(response[10].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['cyberchef']
		if (current != ''):
			if (current == version):
				print('CyberChef			'+current+'			'+version)
			else:
				print('CyberChef			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### NSRL
	try:
		soup = BeautifulSoup(response[11].text, 'html.parser')
		version = soup.text.strip()
		version = version.replace('NSRL RDS Version ','')
		version = version.split(' ')[0]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['nsrl']
		if (current != ''):
			if (current == version):
				print('NSRL				'+current+'			'+version)
			else:
				print('NSRL				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Arsenal Image Mounter
	try:
		soup = BeautifulSoup(response[13].text, 'html.parser')
		version = soup.select_one('h4').text.strip()
		version = version.replace('Arsenal Image Mounter v','')
		version = version.split(' ')[0]
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['aim']
		if (current != ''):
			if (current == version):
				print('AIM				'+current+'			'+version)
			else:
				print('AIM				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Passware
	try:
		soup = BeautifulSoup(response[14].text, 'html.parser')
		version = soup.select_one('a[href^="https://blog.passware.com/passware-kit"]').select_one('h2').text.strip()
		version = version.replace('Passware Kit','')
		version = version.strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['passware']
		if (current != ''):
			if (current == version):
				print('Passware			'+current+'			'+version)
			else:
				print('Passware			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### hashcat
	try:
		soup = BeautifulSoup(response[15].text, 'html.parser')
		version = soup.select_one('a[href^="hashcat-"]')['href']
		version = version.replace('hashcat-','')
		version = version.replace('%2B','+')
		version = version.replace('.7z','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['hashcat']
		if (current != ''):
			if (current == version):
				print('hashcat				'+current+'		'+version)
			else:
				print('hashcat				'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### ExifTool
	try:
		soup = BeautifulSoup(response[16].text, 'html.parser')
		version = soup.findAll('a')[3]['name']
		version = version.replace('v','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['exiftool']
		if (current != ''):
			if (current == version):
				print('ExifTool			'+current+'			'+version)
			else:
				print('ExifTool			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Belkasoft Evidence Center
	try:
		soup = BeautifulSoup(response[17].text, 'html.parser')
		version = soup.text.strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['bec']
		if (current != ''):
			if (current == version):
				print('BEC				'+current+'		'+version)
			else:
				print('BEC				'+current+'		'+version+'		Update available!')
	except:
		pass
	
	
	### CAINE
	try:
		soup = BeautifulSoup(response[18].text, 'html.parser')
		version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['caine']
		if (current != ''):
			if (current == version):
				print('CAINE				'+current+'			'+version)
			else:
				print('CAINE				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### DEFT
	try:
		soup = BeautifulSoup(response[19].text, 'html.parser')
		version = soup.find('td', {'class': 'TablesInvert'}).text.strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['deft']
		if (current != ''):
			if (current == version):
				print('DEFT				'+current+'			'+version)
			else:
				print('DEFT				'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Forensic Falcon Neo
	try:
		soup = BeautifulSoup(response[20].text, 'html.parser')
		version = soup.find('table', {'class': 'datatableblue'}).findAll('tr')[2].findAll('td')[1].text.strip()
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['ffn']
		if (current != ''):
			if (current == version):
				print('Forensic Falcon Neo		'+current+'			'+version)
			else:
				print('Forensic Falcon Neo		'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Atola TaskForce
	try:
		soup = BeautifulSoup(response[21].text, 'html.parser')
		version = soup.select_one('a[href^="http://dl.atola.com/taskforce/"]').text.strip()
		version = version.replace('Download ','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['atola']
		if (current != ''):
			if (current == version):
				print('Atola TaskForce			'+current+'			'+version)
			else:
				print('Atola TaskForce			'+current+'			'+version+'			Update available!')
	except:
		pass
	
	
	### Forensic Email Collector
	try:
		soup = BeautifulSoup(response[22].text, 'html.parser')
		version = soup.select_one('h4').text.strip()
		version = version.split(' ')[0]
		version = version.replace('v','')
	except:
		version = 'Error'
	try:
		current = config['CURRENT']['fec']
		if (current != ''):
			if (current == version):
				print('Forensic Email Collector	'+current+'		'+version)
			else:
				print('Forensic Email Collector	'+current+'		'+version+'		Update available!')
	except:
		pass
		
	
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[12].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version == '1.5'
	if (version == '1.5'):
		pass
	else:
		print('')
		print('FVC update available!')

def current_save():
	config['CURRENT']['gui'] = gui_option.get()
	config['CURRENT']['encase'] = encase_current.get()
	config['CURRENT']['blacklight'] = blacklight_current.get()
	config['CURRENT']['macquisition'] = macquisition_current.get()
	config['CURRENT']['axiom'] = axiom_current.get()
	config['CURRENT']['ufed4pc'] = ufed4pc_current.get()
	config['CURRENT']['physicalanalyzer'] = physicalanalyzer_current.get()
	config['CURRENT']['osf'] = osf_current.get()
	config['CURRENT']['forensicexplorer'] = forensicexplorer_current.get()
	config['CURRENT']['usbdetective'] = usbdetective_current.get()
	config['CURRENT']['ftk'] = ftk_current.get()
	config['CURRENT']['ftkimager'] = ftkimager_current.get()
	config['CURRENT']['xamn'] = xamn_current.get()
	config['CURRENT']['xways'] = xways_current.get()
	config['CURRENT']['cyberchef'] = cyberchef_current.get()
	config['CURRENT']['nsrl'] = nsrl_current.get()
	config['CURRENT']['aim'] = aim_current.get()
	config['CURRENT']['passware'] = passware_current.get()
	config['CURRENT']['hashcat'] = hashcat_current.get()
	config['CURRENT']['exiftool'] = exiftool_current.get()
	config['CURRENT']['bec'] = bec_current.get()
	config['CURRENT']['caine'] = caine_current.get()
	config['CURRENT']['deft'] = deft_current.get()
	config['CURRENT']['ffn'] = ffn_current.get()
	config['CURRENT']['atola'] = atola_current.get()
	config['CURRENT']['fec'] = fec_current.get()
	with open('current_versions.ini', 'w') as configfile:
		config.write(configfile)
	current_save.configure(text='Checking for updates...', state='disabled')
	gui_toggle.configure(state='disabled')
	latest_update()
	current_save.configure(text='Current versions saved', state='normal')
	gui_toggle.configure(state='normal')

def about_box():
	messagebox.showinfo('About', 'Forensic Version Checker v1.5\n\n\
Tool\'s homepage:\nhttps://github.com/jankais3r/Forensic-Version-Checker\n\n\
Digital Forensics Discord:\nhttps://discord.gg/pNMZunG')


try:
	if config['CURRENT']['gui'] == '1':
		gui = True
	else:
		gui = False
except:
	gui = True

if gui == True:
	window = Tk()
	window.title('Forensic Version Checker')
	
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
	encase = Label(window, text='EnCase', padx=5)
	encase.grid(column=0, row=rowID, sticky=W)
	encase_current = Entry(window, width=8)
	encase_current.grid(column=rowID, row=rowID, sticky=N+S+E+W)
	try:
		encase_current.insert(0,config['CURRENT']['encase'])
	except:
		encase_current.insert(0,'')
	encase_latest = Entry(window, width=8, state='readonly')
	encase_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	encase_update = Label(text='', padx=2)
	encase_update.grid(column=3, row=rowID, padx=(0,10))
	encase_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.guidancesoftware.com/encase-forensic'))
	rowID += 1
	
	### BlackLight
	blacklight = Label(window, text='BlackLight', padx=5)
	blacklight.grid(column=0, row=rowID, sticky=W)
	blacklight_current = Entry(window, width=8)
	blacklight_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		blacklight_current.insert(0,config['CURRENT']['blacklight'])
	except:
		blacklight_current.insert(0,'')
	blacklight_latest = Entry(window, width=8, state='readonly')
	blacklight_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	blacklight_update = Label(text='')
	blacklight_update.grid(column=3, row=rowID, padx=(0,10))
	blacklight_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.blackbagtech.com/downloads/'))
	rowID += 1
	rowID += 1
	
	### MacQuisition
	macquisition = Label(window, text='MacQuisition', padx=5)
	macquisition.grid(column=0, row=rowID, sticky=W)
	macquisition_current = Entry(window, width=8)
	macquisition_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		macquisition_current.insert(0,config['CURRENT']['macquisition'])
	except:
		macquisition_current.insert(0,'')
	macquisition_latest = Entry(window, width=8, state='readonly')
	macquisition_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	macquisition_update = Label(text='')
	macquisition_update.grid(column=3, row=rowID, padx=(0,10))
	macquisition_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.blackbagtech.com/downloads/'))
	rowID += 1
	
	### AXIOM
	axiom = Label(window, text='AXIOM', padx=5)
	axiom.grid(column=0, row=rowID, sticky=W)
	axiom_current = Entry(window, width=8)
	axiom_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		axiom_current.insert(0,config['CURRENT']['axiom'])
	except:
		axiom_current.insert(0,'')
	axiom_latest = Entry(window, width=8, state='readonly')
	axiom_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	axiom_update = Label(text='')
	axiom_update.grid(column=3, row=rowID, padx=(0,10))
	axiom_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.magnetforensics.com/downloadaxiom/'))
	rowID += 1
	
	### UFED4PC
	ufed4pc = Label(window, text='UFED 4PC', padx=5)
	ufed4pc.grid(column=0, row=rowID, sticky=W)
	ufed4pc_current = Entry(window, width=8)
	ufed4pc_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		ufed4pc_current.insert(0,config['CURRENT']['ufed4pc'])
	except:
		ufed4pc_current.insert(0,'')
	ufed4pc_latest = Entry(window, width=8, state='readonly')
	ufed4pc_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	ufed4pc_update = Label(text='')
	ufed4pc_update.grid(column=3, row=rowID, padx=(0,10))
	ufed4pc_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.cellebrite.com/en/support/product-releases/'))
	rowID += 1
	
	### Physical Analyzer
	physicalanalyzer = Label(window, text='Physical Analyzer', padx=5)
	physicalanalyzer.grid(column=0, row=rowID, sticky=W)
	physicalanalyzer_current = Entry(window, width=8)
	physicalanalyzer_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		physicalanalyzer_current.insert(0,config['CURRENT']['physicalanalyzer'])
	except:
		physicalanalyzer_current.insert(0,'')
	physicalanalyzer_latest = Entry(window, width=8, state='readonly')
	physicalanalyzer_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	physicalanalyzer_update = Label(text='')
	physicalanalyzer_update.grid(column=3, row=rowID, padx=(0,10))
	physicalanalyzer_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.cellebrite.com/en/support/product-releases/'))
	rowID += 1
	
	### OSF
	osf = Label(window, text='OSForensics', padx=5)
	osf.grid(column=0, row=rowID, sticky=W)
	osf_current = Entry(window, width=8)
	osf_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		osf_current.insert(0,config['CURRENT']['osf'])
	except:
		osf_current.insert(0,'')
	osf_latest = Entry(window, width=8, state='readonly')
	osf_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	osf_update = Label(text='')
	osf_update.grid(column=3, row=rowID, padx=(0,10))
	osf_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.osforensics.com/download.html'))
	rowID += 1
	
	### ForensicExplorer
	forensicexplorer = Label(window, text='ForensicExplorer', padx=5)
	forensicexplorer.grid(column=0, row=rowID, sticky=W)
	forensicexplorer_current = Entry(window, width=8)
	forensicexplorer_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		forensicexplorer_current.insert(0,config['CURRENT']['forensicexplorer'])
	except:
		forensicexplorer_current.insert(0,'')
	forensicexplorer_latest = Entry(window, width=8, state='readonly')
	forensicexplorer_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	forensicexplorer_update = Label(text='')
	forensicexplorer_update.grid(column=3, row=rowID, padx=(0,10))
	forensicexplorer_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.forensicexplorer.com/download.php'))
	rowID += 1
	
	### USB Detective
	usbdetective = Label(window, text='USB Detective', padx=5)
	usbdetective.grid(column=0, row=rowID, sticky=W)
	usbdetective_current = Entry(window, width=8)
	usbdetective_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		usbdetective_current.insert(0,config['CURRENT']['usbdetective'])
	except:
		usbdetective_current.insert(0,'')
	usbdetective_latest = Entry(window, width=8, state='readonly')
	usbdetective_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	usbdetective_update = Label(text='')
	usbdetective_update.grid(column=3, row=rowID, padx=(0,10))
	usbdetective_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://usbdetective.com/release-notes/'))
	rowID += 1
	
	### FTK
	ftk = Label(window, text='FTK', padx=5)
	ftk.grid(column=0, row=rowID, sticky=W)
	ftk_current = Entry(window, width=8)
	ftk_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		ftk_current.insert(0,config['CURRENT']['ftk'])
	except:
		ftk_current.insert(0,'')
	ftk_latest = Entry(window, width=8, state='readonly')
	ftk_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	ftk_update = Label(text='')
	ftk_update.grid(column=3, row=rowID, padx=(0,10))
	ftk_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://accessdata.com/product-download'))
	rowID += 1
	
	### FTK Imager
	ftkimager = Label(window, text='FTK Imager', padx=5)
	ftkimager.grid(column=0, row=rowID, sticky=W)
	ftkimager_current = Entry(window, width=8)
	ftkimager_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		ftkimager_current.insert(0,config['CURRENT']['ftkimager'])
	except:
		ftkimager_current.insert(0,'')
	ftkimager_latest = Entry(window, width=8, state='readonly')
	ftkimager_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	ftkimager_update = Label(text='')
	ftkimager_update.grid(column=3, row=rowID, padx=(0,10))
	ftkimager_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://accessdata.com/product-download'))
	rowID += 1
	
	### XAMN
	xamn = Label(window, text='XAMN', padx=5)
	xamn.grid(column=0, row=rowID, sticky=W)
	xamn_current = Entry(window, width=8)
	xamn_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		xamn_current.insert(0,config['CURRENT']['xamn'])
	except:
		xamn_current.insert(0,'')
	xamn_latest = Entry(window, width=8, state='readonly')
	xamn_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	xamn_update = Label(text='')
	xamn_update.grid(column=3, row=rowID, padx=(0,10))
	xamn_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.msab.com/downloads/'))
	rowID += 1
	
	### X-Ways
	xways = Label(window, text='X-Ways', padx=5)
	xways.grid(column=0, row=rowID, sticky=W)
	xways_current = Entry(window, width=8)
	xways_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		xways_current.insert(0,config['CURRENT']['xways'])
	except:
		xways_current.insert(0,'')
	xways_latest = Entry(window, width=8, state='readonly')
	xways_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	xways_update = Label(text='')
	xways_update.grid(column=3, row=rowID, padx=(0,10))
	xways_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.x-ways.net/winhex/license.html'))
	rowID += 1
	
	### CyberChef
	cyberchef = Label(window, text='CyberChef', padx=5)
	cyberchef.grid(column=0, row=rowID, sticky=W)
	cyberchef_current = Entry(window, width=8)
	cyberchef_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		cyberchef_current.insert(0,config['CURRENT']['cyberchef'])
	except:
		cyberchef_current.insert(0,'')
	cyberchef_latest = Entry(window, width=8, state='readonly')
	cyberchef_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	cyberchef_update = Label(text='')
	cyberchef_update.grid(column=3, row=rowID, padx=(0,10))
	cyberchef_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/gchq/CyberChef/releases/latest'))
	rowID += 1
	
	### NSRL
	nsrl = Label(window, text='NSRL hash set', padx=5)
	nsrl.grid(column=0, row=rowID, sticky=W)
	nsrl_current = Entry(window, width=8)
	nsrl_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		nsrl_current.insert(0,config['CURRENT']['nsrl'])
	except:
		nsrl_current.insert(0,'')
	nsrl_latest = Entry(window, width=8, state='readonly')
	nsrl_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	nsrl_update = Label(text='')
	nsrl_update.grid(column=3, row=rowID, padx=(0,10))
	nsrl_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds'))
	rowID += 1
	
	### Arsenal Image Mounter
	aim = Label(window, text='AIM', padx=5)
	aim.grid(column=0, row=rowID, sticky=W)
	aim_current = Entry(window, width=8)
	aim_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		aim_current.insert(0,config['CURRENT']['aim'])
	except:
		aim_current.insert(0,'')
	aim_latest = Entry(window, width=8, state='readonly')
	aim_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	aim_update = Label(text='')
	aim_update.grid(column=3, row=rowID, padx=(0,10))
	aim_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://arsenalrecon.com/downloads/'))
	rowID += 1
	
	### Passware
	passware = Label(window, text='Passware', padx=5)
	passware.grid(column=0, row=rowID, sticky=W)
	passware_current = Entry(window, width=8)
	passware_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		passware_current.insert(0,config['CURRENT']['passware'])
	except:
		passware_current.insert(0,'')
	passware_latest = Entry(window, width=8, state='readonly')
	passware_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	passware_update = Label(text='')
	passware_update.grid(column=3, row=rowID, padx=(0,10))
	passware_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.passware.com/kit-forensic/whatsnew/'))
	rowID += 1
	
	### hashcat
	hashcat = Label(window, text='hashcat', padx=5)
	hashcat.grid(column=0, row=rowID, sticky=W)
	hashcat_current = Entry(window, width=8)
	hashcat_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		hashcat_current.insert(0,config['CURRENT']['hashcat'])
	except:
		hashcat_current.insert(0,'')
	hashcat_latest = Entry(window, width=8, state='readonly')
	hashcat_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	hashcat_update = Label(text='')
	hashcat_update.grid(column=3, row=rowID, padx=(0,10))
	hashcat_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://hashcat.net/hashcat/'))
	rowID += 1
	
	### ExifTool
	exiftool = Label(window, text='ExifTool', padx=5)
	exiftool.grid(column=0, row=rowID, sticky=W)
	exiftool_current = Entry(window, width=8)
	exiftool_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		exiftool_current.insert(0,config['CURRENT']['exiftool'])
	except:
		exiftool_current.insert(0,'')
	exiftool_latest = Entry(window, width=8, state='readonly')
	exiftool_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	exiftool_update = Label(text='')
	exiftool_update.grid(column=3, row=rowID, padx=(0,10))
	exiftool_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://owl.phy.queensu.ca/~phil/exiftool/'))
	rowID += 1
	
	### Belkasoft Evidence Center
	bec = Label(window, text='BEC', padx=5)
	bec.grid(column=0, row=rowID, sticky=W)
	bec_current = Entry(window, width=8)
	bec_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		bec_current.insert(0,config['CURRENT']['bec'])
	except:
		bec_current.insert(0,'')
	bec_latest = Entry(window, width=8, state='readonly')
	bec_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	bec_update = Label(text='')
	bec_update.grid(column=3, row=rowID, padx=(0,10))
	bec_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://belkasoft.com/get'))
	rowID += 1
	
	### CAINE
	caine = Label(window, text='CAINE', padx=5)
	caine.grid(column=0, row=rowID, sticky=W)
	caine_current = Entry(window, width=8)
	caine_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		caine_current.insert(0,config['CURRENT']['caine'])
	except:
		caine_current.insert(0,'')
	caine_latest = Entry(window, width=8, state='readonly')
	caine_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	caine_update = Label(text='')
	caine_update.grid(column=3, row=rowID, padx=(0,10))
	caine_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.caine-live.net/'))
	rowID += 1
	
	### DEFT
	deft = Label(window, text='DEFT', padx=5)
	deft.grid(column=0, row=rowID, sticky=W)
	deft_current = Entry(window, width=8)
	deft_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		deft_current.insert(0,config['CURRENT']['deft'])
	except:
		deft_current.insert(0,'')
	deft_latest = Entry(window, width=8, state='readonly')
	deft_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	deft_update = Label(text='')
	deft_update.grid(column=3, row=rowID, padx=(0,10))
	deft_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://na.mirror.garr.it/mirrors/deft/zero/'))
	rowID += 1
	
	### Forensic Falcon Neo
	ffn = Label(window, text='Forensic Falcon Neo', padx=5)
	ffn.grid(column=0, row=rowID, sticky=W)
	ffn_current = Entry(window, width=8)
	ffn_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		ffn_current.insert(0,config['CURRENT']['ffn'])
	except:
		ffn_current.insert(0,'')
	ffn_latest = Entry(window, width=8, state='readonly')
	ffn_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	ffn_update = Label(text='')
	ffn_update.grid(column=3, row=rowID, padx=(0,10))
	ffn_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://www.logicube.com/knowledge/forensic-falcon-neo/'))
	rowID += 1
	
	### Atola TaskForce
	atola = Label(window, text='Atola TaskForce', padx=5)
	atola.grid(column=0, row=rowID, sticky=W)
	atola_current = Entry(window, width=8)
	atola_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		atola_current.insert(0,config['CURRENT']['atola'])
	except:
		atola_current.insert(0,'')
	atola_latest = Entry(window, width=8, state='readonly')
	atola_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	atola_update = Label(text='')
	atola_update.grid(column=3, row=rowID, padx=(0,10))
	atola_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://atola.com/products/taskforce/download.html'))
	rowID += 1
	
	### Forensic Email Collector
	fec = Label(window, text='Forensic Email Collector', padx=5)
	fec.grid(column=0, row=rowID, sticky=W)
	fec_current = Entry(window, width=8)
	fec_current.grid(column=1, row=rowID, sticky=N+S+E+W)
	try:
		fec_current.insert(0,config['CURRENT']['fec'])
	except:
		fec_current.insert(0,'')
	fec_latest = Entry(window, width=8, state='readonly')
	fec_latest.grid(column=2, row=rowID, sticky=N+S+E+W)
	fec_update = Label(text='')
	fec_update.grid(column=3, row=rowID, padx=(0,10))
	fec_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('http://www.metaspike.com/fec-change-log/'))
	rowID += 1
	
	about = Label(window, text='?', padx=5, fg='grey', cursor='hand2')
	about.grid(column=0, row=rowID, sticky=W, pady=(7,7))
	about.bind('<ButtonRelease-1>', lambda e: about_box())
	
	gui_option = StringVar()
	gui_toggle = Checkbutton(window, text=' GUI?  ', variable=gui_option, onvalue='1', offvalue='0')
	gui_toggle.grid(column=0, row=rowID, sticky=E, pady=(7,7))
	gui_toggle.select()
	
	current_save = Button(window, text='Save', command=current_save)
	current_save.grid(column=1, row=rowID, columnspan=2, sticky=N+S+E+W, pady=(7,7))

	if first_run != True:
		current_save.configure(text='Checking for updates...', state='disabled')
		gui_toggle.configure(state='disabled')
		latest_update()
		current_save.configure(text='Save', state='normal')
		gui_toggle.configure(state='normal')
	else:
		messagebox.showinfo('Welcome', 'New config file has been created.\n\n\
Please populate your current tool versions, and click Save.\n\n\
To use the CLI mode, untick the GUI checkbox and restart the script.')
	
	tab_order = (encase_current, blacklight_current, macquisition_current, axiom_current, ufed4pc_current, physicalanalyzer_current, osf_current, forensicexplorer_current,\
	usbdetective_current, ftk_current, ftkimager_current, xamn_current, xways_current, cyberchef_current, nsrl_current, aim_current, passware_current, hashcat_current,\
	exiftool_current, bec_current, caine_current, deft_current, ffn_current, atola_current, fec_current)
	for widget in tab_order:
		widget.lift()
	
	window.mainloop()
else:
	cli_update()
	