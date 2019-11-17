#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import grequests
import webbrowser
import configparser
from tkinter import *
from bs4 import BeautifulSoup
from tkinter import messagebox


window = Tk()
window.title('Forensic Version Checker')

if os.name == 'nt':
	window.geometry('345x530')
	fontsize = 9
else:
	window.geometry('315x475')
	fontsize = 10


if os.path.isfile('current_versions.ini') == False:
	default_config = """[CURRENT]
encase = 
blacklight = 
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
"""

	configfile = open('current_versions.ini', 'w')
	configfile.write(default_config)
	configfile.close()
	messagebox.showinfo('Welcome', 'New config file has been created.\n\nPlease populate your current tool versions, and click Save.')
	first_run = True
else:
	first_run = False

config = configparser.ConfigParser()
config.read('current_versions.ini')

def callback(url):
	webbrowser.open_new(url)

def latest_update():
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
            'https://www.nist.gov/itl/ssd/software-quality-group/nsrl-download/current-rds-hash-sets',
            'https://github.com/jankais3r/Forensic-Version-Checker/releases/latest',
			'https://arsenalrecon.com/downloads/',
			'https://blog.passware.com/category/product-update/',
			'https://hashcat.net/beta/',
			'https://owl.phy.queensu.ca/~phil/exiftool/history.html',
			'https://belkasoft.com/becver.txt',
			'https://distrowatch.com/table.php?distribution=caine',
			'https://distrowatch.com/table.php?distribution=deft',
			'https://www.logicube.com/knowledge/forensic-falcon-neo/'
        ]
	response = grequests.map((grequests.get(u, headers=ua_headers) for u in urls), size=3)
	
	### EnCase
	soup = BeautifulSoup(response[0].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[1].text, 'html.parser')
	try:
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
	
	### AXIOM
	soup = BeautifulSoup(response[2].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[3].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[3].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[4].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[5].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[6].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[7].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[7].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[8].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[9].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[10].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[11].text, 'html.parser')
	try:
		version = soup.find('div', {'class': 'tex2jax'}).select_one('h2').text.strip()
		version = version.replace('RDS Version ','')
		version = version.split('-')[0]
		version = version[:-1]
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
	soup = BeautifulSoup(response[12].text, 'html.parser')
	try:
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v','')
	except:
		version == '1.3'
	if version != '1.3':
		about.configure(text='Update FVC', fg='blue', cursor='hand2')
		about.bind('<ButtonRelease-1>', lambda e:callback('https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'))
	
	### Arsenal Image Mounter
	soup = BeautifulSoup(response[13].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[14].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[15].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[16].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[17].text, 'html.parser')
	try:
		version = soup
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
	soup = BeautifulSoup(response[18].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[19].text, 'html.parser')
	try:
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
	soup = BeautifulSoup(response[20].text, 'html.parser')
	try:
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

def current_save():
	current_save.configure(text='Checking for updates...', state='disabled')
	window.update()
	config['CURRENT']['encase'] = encase_current.get()
	config['CURRENT']['blacklight'] = blacklight_current.get()
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
	with open('current_versions.ini', 'w') as configfile:
		config.write(configfile)
	current_save.configure(text='Current versions saved', state='normal')
	latest_update()

def about_box():
	messagebox.showinfo('About', 'Forensic Version Checker v1.3\n\nTool\'s homepage:\nhttps://github.com/jankais3r/Forensic-Version-Checker\n\nDigital Forensics Discord:\nhttps://discord.gg/pNMZunG')

tool = Label(window, text='Tool', font=('TkDefaultFont', fontsize, 'underline'), padx=5, pady=3)
tool.grid(column=0, row=0, sticky=W)
current = Label(window, text='Current Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
current.grid(column=1, row=0)
latest = Label(window, text='Latest Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
latest.grid(column=2, row=0)
latest = Label(window, text='Update', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
latest.grid(column=3, row=0)

### EnCase
encase = Label(window, text='EnCase', padx=5)
encase.grid(column=0, row=1, sticky=W)
encase_current = Entry(window, width=8)
encase_current.grid(column=1, row=1, sticky=N+S+E+W)
try:
	encase_current.insert(0,config['CURRENT']['encase'])
except:
	encase_current.insert(0,'')
encase_latest = Entry(window, width=8, state='readonly')
encase_latest.grid(column=2, row=1, sticky=N+S+E+W)
encase_update = Label(text='', padx=2)
encase_update.grid(column=3, row=1)
encase_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.guidancesoftware.com/encase-forensic'))

### BlackLight
blacklight = Label(window, text='BlackLight', padx=5)
blacklight.grid(column=0, row=2, sticky=W)
blacklight_current = Entry(window, width=8)
blacklight_current.grid(column=1, row=2, sticky=N+S+E+W)
try:
	blacklight_current.insert(0,config['CURRENT']['blacklight'])
except:
	blacklight_current.insert(0,'')
blacklight_latest = Entry(window, width=8, state='readonly')
blacklight_latest.grid(column=2, row=2, sticky=N+S+E+W)
blacklight_update = Label(text='')
blacklight_update.grid(column=3, row=2)
blacklight_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.blackbagtech.com/downloads/'))

### AXIOM
axiom = Label(window, text='AXIOM', padx=5)
axiom.grid(column=0, row=3, sticky=W)
axiom_current = Entry(window, width=8)
axiom_current.grid(column=1, row=3, sticky=N+S+E+W)
try:
	axiom_current.insert(0,config['CURRENT']['axiom'])
except:
	axiom_current.insert(0,'')
axiom_latest = Entry(window, width=8, state='readonly')
axiom_latest.grid(column=2, row=3, sticky=N+S+E+W)
axiom_update = Label(text='')
axiom_update.grid(column=3, row=3)
axiom_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.magnetforensics.com/downloadaxiom/'))

### UFED4PC
ufed4pc = Label(window, text='UFED 4PC', padx=5)
ufed4pc.grid(column=0, row=4, sticky=W)
ufed4pc_current = Entry(window, width=8)
ufed4pc_current.grid(column=1, row=4, sticky=N+S+E+W)
try:
	ufed4pc_current.insert(0,config['CURRENT']['ufed4pc'])
except:
	ufed4pc_current.insert(0,'')
ufed4pc_latest = Entry(window, width=8, state='readonly')
ufed4pc_latest.grid(column=2, row=4, sticky=N+S+E+W)
ufed4pc_update = Label(text='')
ufed4pc_update.grid(column=3, row=4)
ufed4pc_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.cellebrite.com/en/support/product-releases/'))

### Physical Analyzer
physicalanalyzer = Label(window, text='Physical Analyzer', padx=5)
physicalanalyzer.grid(column=0, row=5, sticky=W)
physicalanalyzer_current = Entry(window, width=8)
physicalanalyzer_current.grid(column=1, row=5, sticky=N+S+E+W)
try:
	physicalanalyzer_current.insert(0,config['CURRENT']['physicalanalyzer'])
except:
	physicalanalyzer_current.insert(0,'')
physicalanalyzer_latest = Entry(window, width=8, state='readonly')
physicalanalyzer_latest.grid(column=2, row=5, sticky=N+S+E+W)
physicalanalyzer_update = Label(text='')
physicalanalyzer_update.grid(column=3, row=5)
physicalanalyzer_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.cellebrite.com/en/support/product-releases/'))

### OSF
osf = Label(window, text='OSForensics', padx=5)
osf.grid(column=0, row=6, sticky=W)
osf_current = Entry(window, width=8)
osf_current.grid(column=1, row=6, sticky=N+S+E+W)
try:
	osf_current.insert(0,config['CURRENT']['osf'])
except:
	osf_current.insert(0,'')
osf_latest = Entry(window, width=8, state='readonly')
osf_latest.grid(column=2, row=6, sticky=N+S+E+W)
osf_update = Label(text='')
osf_update.grid(column=3, row=6)
osf_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.osforensics.com/download.html'))

### ForensicExplorer
forensicexplorer = Label(window, text='ForensicExplorer', padx=5)
forensicexplorer.grid(column=0, row=7, sticky=W)
forensicexplorer_current = Entry(window, width=8)
forensicexplorer_current.grid(column=1, row=7, sticky=N+S+E+W)
try:
	forensicexplorer_current.insert(0,config['CURRENT']['forensicexplorer'])
except:
	forensicexplorer_current.insert(0,'')
forensicexplorer_latest = Entry(window, width=8, state='readonly')
forensicexplorer_latest.grid(column=2, row=7, sticky=N+S+E+W)
forensicexplorer_update = Label(text='')
forensicexplorer_update.grid(column=3, row=7)
forensicexplorer_update.bind('<ButtonRelease-1>', lambda e:callback('http://www.forensicexplorer.com/download.php'))

### USB Detective
usbdetective = Label(window, text='USB Detective', padx=5)
usbdetective.grid(column=0, row=8, sticky=W)
usbdetective_current = Entry(window, width=8)
usbdetective_current.grid(column=1, row=8, sticky=N+S+E+W)
try:
	usbdetective_current.insert(0,config['CURRENT']['usbdetective'])
except:
	usbdetective_current.insert(0,'')
usbdetective_latest = Entry(window, width=8, state='readonly')
usbdetective_latest.grid(column=2, row=8, sticky=N+S+E+W)
usbdetective_update = Label(text='')
usbdetective_update.grid(column=3, row=8)
usbdetective_update.bind('<ButtonRelease-1>', lambda e:callback('https://usbdetective.com/release-notes/'))

### FTK
ftk = Label(window, text='FTK', padx=5)
ftk.grid(column=0, row=9, sticky=W)
ftk_current = Entry(window, width=8)
ftk_current.grid(column=1, row=9, sticky=N+S+E+W)
try:
	ftk_current.insert(0,config['CURRENT']['ftk'])
except:
	ftk_current.insert(0,'')
ftk_latest = Entry(window, width=8, state='readonly')
ftk_latest.grid(column=2, row=9, sticky=N+S+E+W)
ftk_update = Label(text='')
ftk_update.grid(column=3, row=9)
ftk_update.bind('<ButtonRelease-1>', lambda e:callback('https://accessdata.com/product-download'))

### FTK Imager
ftkimager = Label(window, text='FTK Imager', padx=5)
ftkimager.grid(column=0, row=10, sticky=W)
ftkimager_current = Entry(window, width=8)
ftkimager_current.grid(column=1, row=10, sticky=N+S+E+W)
try:
	ftkimager_current.insert(0,config['CURRENT']['ftkimager'])
except:
	ftkimager_current.insert(0,'')
ftkimager_latest = Entry(window, width=8, state='readonly')
ftkimager_latest.grid(column=2, row=10, sticky=N+S+E+W)
ftkimager_update = Label(text='')
ftkimager_update.grid(column=3, row=10)
ftkimager_update.bind('<ButtonRelease-1>', lambda e:callback('https://accessdata.com/product-download'))

### XAMN
xamn = Label(window, text='XAMN', padx=5)
xamn.grid(column=0, row=11, sticky=W)
xamn_current = Entry(window, width=8)
xamn_current.grid(column=1, row=11, sticky=N+S+E+W)
try:
	xamn_current.insert(0,config['CURRENT']['xamn'])
except:
	xamn_current.insert(0,'')
xamn_latest = Entry(window, width=8, state='readonly')
xamn_latest.grid(column=2, row=11, sticky=N+S+E+W)
xamn_update = Label(text='')
xamn_update.grid(column=3, row=11)
xamn_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.msab.com/downloads/'))

### X-Ways
xways = Label(window, text='X-Ways', padx=5)
xways.grid(column=0, row=12, sticky=W)
xways_current = Entry(window, width=8)
xways_current.grid(column=1, row=12, sticky=N+S+E+W)
try:
	xways_current.insert(0,config['CURRENT']['xways'])
except:
	xways_current.insert(0,'')
xways_latest = Entry(window, width=8, state='readonly')
xways_latest.grid(column=2, row=12, sticky=N+S+E+W)
xways_update = Label(text='')
xways_update.grid(column=3, row=12)
xways_update.bind('<ButtonRelease-1>', lambda e:callback('http://www.x-ways.net/winhex/license.html'))

### CyberChef
cyberchef = Label(window, text='CyberChef', padx=5)
cyberchef.grid(column=0, row=13, sticky=W)
cyberchef_current = Entry(window, width=8)
cyberchef_current.grid(column=1, row=13, sticky=N+S+E+W)
try:
	cyberchef_current.insert(0,config['CURRENT']['cyberchef'])
except:
	cyberchef_current.insert(0,'')
cyberchef_latest = Entry(window, width=8, state='readonly')
cyberchef_latest.grid(column=2, row=13, sticky=N+S+E+W)
cyberchef_update = Label(text='')
cyberchef_update.grid(column=3, row=13)
cyberchef_update.bind('<ButtonRelease-1>', lambda e:callback('https://github.com/gchq/CyberChef/releases/latest'))

### NSRL
nsrl = Label(window, text='NSRL hash set', padx=5)
nsrl.grid(column=0, row=14, sticky=W)
nsrl_current = Entry(window, width=8)
nsrl_current.grid(column=1, row=14, sticky=N+S+E+W)
try:
	nsrl_current.insert(0,config['CURRENT']['nsrl'])
except:
	nsrl_current.insert(0,'')
nsrl_latest = Entry(window, width=8, state='readonly')
nsrl_latest.grid(column=2, row=14, sticky=N+S+E+W)
nsrl_update = Label(text='')
nsrl_update.grid(column=3, row=14)
nsrl_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.nist.gov/itl/ssd/software-quality-group/nsrl-download/current-rds-hash-sets'))

### Arsenal Image Mounter
aim = Label(window, text='AIM', padx=5)
aim.grid(column=0, row=15, sticky=W)
aim_current = Entry(window, width=8)
aim_current.grid(column=1, row=15, sticky=N+S+E+W)
try:
	aim_current.insert(0,config['CURRENT']['aim'])
except:
	aim_current.insert(0,'')
aim_latest = Entry(window, width=8, state='readonly')
aim_latest.grid(column=2, row=15, sticky=N+S+E+W)
aim_update = Label(text='')
aim_update.grid(column=3, row=15)
aim_update.bind('<ButtonRelease-1>', lambda e:callback('https://arsenalrecon.com/downloads/'))

### Passware
passware = Label(window, text='Passware', padx=5)
passware.grid(column=0, row=16, sticky=W)
passware_current = Entry(window, width=8)
passware_current.grid(column=1, row=16, sticky=N+S+E+W)
try:
	passware_current.insert(0,config['CURRENT']['passware'])
except:
	passware_current.insert(0,'')
passware_latest = Entry(window, width=8, state='readonly')
passware_latest.grid(column=2, row=16, sticky=N+S+E+W)
passware_update = Label(text='')
passware_update.grid(column=3, row=16)
passware_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.passware.com/kit-forensic/whatsnew/'))

### hashcat
hashcat = Label(window, text='hashcat', padx=5)
hashcat.grid(column=0, row=17, sticky=W)
hashcat_current = Entry(window, width=8)
hashcat_current.grid(column=1, row=17, sticky=N+S+E+W)
try:
	hashcat_current.insert(0,config['CURRENT']['hashcat'])
except:
	hashcat_current.insert(0,'')
hashcat_latest = Entry(window, width=8, state='readonly')
hashcat_latest.grid(column=2, row=17, sticky=N+S+E+W)
hashcat_update = Label(text='')
hashcat_update.grid(column=3, row=17)
hashcat_update.bind('<ButtonRelease-1>', lambda e:callback('https://hashcat.net/hashcat/'))

### ExifTool
exiftool = Label(window, text='ExifTool', padx=5)
exiftool.grid(column=0, row=18, sticky=W)
exiftool_current = Entry(window, width=8)
exiftool_current.grid(column=1, row=18, sticky=N+S+E+W)
try:
	exiftool_current.insert(0,config['CURRENT']['exiftool'])
except:
	exiftool_current.insert(0,'')
exiftool_latest = Entry(window, width=8, state='readonly')
exiftool_latest.grid(column=2, row=18, sticky=N+S+E+W)
exiftool_update = Label(text='')
exiftool_update.grid(column=3, row=18)
exiftool_update.bind('<ButtonRelease-1>', lambda e:callback('https://owl.phy.queensu.ca/~phil/exiftool/'))

### Belkasoft Evidence Center
bec = Label(window, text='BEC', padx=5)
bec.grid(column=0, row=19, sticky=W)
bec_current = Entry(window, width=8)
bec_current.grid(column=1, row=19, sticky=N+S+E+W)
try:
	bec_current.insert(0,config['CURRENT']['bec'])
except:
	bec_current.insert(0,'')
bec_latest = Entry(window, width=8, state='readonly')
bec_latest.grid(column=2, row=19, sticky=N+S+E+W)
bec_update = Label(text='')
bec_update.grid(column=3, row=19)
bec_update.bind('<ButtonRelease-1>', lambda e:callback('https://belkasoft.com/get'))

### CAINE
caine = Label(window, text='CAINE', padx=5)
caine.grid(column=0, row=20, sticky=W)
caine_current = Entry(window, width=8)
caine_current.grid(column=1, row=20, sticky=N+S+E+W)
try:
	caine_current.insert(0,config['CURRENT']['caine'])
except:
	caine_current.insert(0,'')
caine_latest = Entry(window, width=8, state='readonly')
caine_latest.grid(column=2, row=20, sticky=N+S+E+W)
caine_update = Label(text='')
caine_update.grid(column=3, row=20)
caine_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.caine-live.net/'))

### DEFT
deft = Label(window, text='DEFT', padx=5)
deft.grid(column=0, row=21, sticky=W)
deft_current = Entry(window, width=8)
deft_current.grid(column=1, row=21, sticky=N+S+E+W)
try:
	deft_current.insert(0,config['CURRENT']['deft'])
except:
	deft_current.insert(0,'')
deft_latest = Entry(window, width=8, state='readonly')
deft_latest.grid(column=2, row=21, sticky=N+S+E+W)
deft_update = Label(text='')
deft_update.grid(column=3, row=21)
deft_update.bind('<ButtonRelease-1>', lambda e:callback('http://na.mirror.garr.it/mirrors/deft/zero/'))

### Forensic Falcon Neo
ffn = Label(window, text='Forensic Falcon N', padx=5)
ffn.grid(column=0, row=22, sticky=W)
ffn_current = Entry(window, width=8)
ffn_current.grid(column=1, row=22, sticky=N+S+E+W)
try:
	ffn_current.insert(0,config['CURRENT']['ffn'])
except:
	ffn_current.insert(0,'')
ffn_latest = Entry(window, width=8, state='readonly')
ffn_latest.grid(column=2, row=22, sticky=N+S+E+W)
ffn_update = Label(text='')
ffn_update.grid(column=3, row=22)
ffn_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.logicube.com/knowledge/forensic-falcon-neo/'))

divider = Label(window, text='', font=('TkDefaultFont', 1, 'underline'))
divider.grid(column=1, row=23)

about = Label(window, text='?', padx=5, fg='grey', cursor='hand2')
about.grid(column=0, row=24, sticky=W)
about.bind('<ButtonRelease-1>', lambda e: about_box())

current_save = Button(window, text='Save', command=current_save)
current_save.grid(column=1, row=24, columnspan=2, sticky=N+S+E+W)

if first_run != True:
	current_save.configure(text='Checking for updates...', state='disabled')
	window.update()
	
	latest_update()
	current_save.configure(text='Save', state='normal')
	
window.mainloop()
