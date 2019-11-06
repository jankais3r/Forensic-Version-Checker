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
	window.geometry('345x360')
	fontsize = 9
else:
	window.geometry('315x325')
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
            'https://github.com/gchq/CyberChef/blob/master/CHANGELOG.md',
            'https://www.nist.gov/itl/ssd/software-quality-group/nsrl-download/current-rds-hash-sets',
            'https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'
        ]
	response = grequests.map((grequests.get(u) for u in urls), size=5)
	
	### EnCase
	soup = BeautifulSoup(response[0].text, 'html.parser')
	version = soup.select_one('h3').text.strip()
	version = version.replace('EnCase Forensic ','')
	version = version.split(':')[0]
	encase_latest.configure(state='normal')
	encase_latest.delete(0, END)
	encase_latest.insert(0,version)
	encase_latest.configure(state='readonly')
	if encase_current.get() == encase_latest.get():
		encase_latest.configure(readonlybackground='limegreen')
		encase_update.configure(text='', cursor='')
	elif encase_current.get() != '':
		encase_latest.configure(readonlybackground='orange')
		encase_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### BlackLight
	soup = BeautifulSoup(response[1].text, 'html.parser')
	version = soup.find('dl', {'id': 'blacklightrevision'}).select_one('span').text.strip()
	version = version.replace('BlackLight ','')
	blacklight_latest.configure(state='normal')
	blacklight_latest.delete(0, END)
	blacklight_latest.insert(0,version)
	blacklight_latest.configure(state='readonly')
	if blacklight_current.get() == blacklight_latest.get():
		blacklight_latest.configure(readonlybackground='limegreen')
		blacklight_update.configure(text='', cursor='')
	elif blacklight_current.get() != '':
		blacklight_latest.configure(readonlybackground='orange')
		blacklight_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### AXIOM
	soup = BeautifulSoup(response[2].text, 'html.parser')
	version = soup.select_one('h2').text.strip()
	version = version.replace('MAGNET AXIOM ','')
	axiom_latest.configure(state='normal')
	axiom_latest.delete(0, END)
	axiom_latest.insert(0,version)
	axiom_latest.configure(state='readonly')
	if axiom_current.get() == axiom_latest.get():
		axiom_latest.configure(readonlybackground='limegreen')
		axiom_update.configure(text='', cursor='')
	elif axiom_current.get() != '':
		axiom_latest.configure(readonlybackground='orange')
		axiom_update.configure(text='Update', fg='blue', cursor='hand2')
	
	## UFED4PC
	soup = BeautifulSoup(response[3].text, 'html.parser')
	version = soup.find(text=re.compile('UFED 4PC')).parent.select_one('b').text.strip()
	version = version.replace('Version ','')
	ufed4pc_latest.configure(state='normal')
	ufed4pc_latest.delete(0, END)
	ufed4pc_latest.insert(0,version)
	ufed4pc_latest.configure(state='readonly')
	if ufed4pc_current.get() == ufed4pc_latest.get():
		ufed4pc_latest.configure(readonlybackground='limegreen')
		ufed4pc_update.configure(text='', cursor='')
	elif ufed4pc_current.get() != '':
		ufed4pc_latest.configure(readonlybackground='orange')
		ufed4pc_update.configure(text='Update', fg='blue', cursor='hand2')
	
	#Physical Analyzer
	soup = BeautifulSoup(response[3].text, 'html.parser')
	version = soup.find(text=re.compile('Physical|Logical Analyzer')).parent.select_one('b').text.strip()
	version = version.replace('Version ','')
	physicalanalyzer_latest.configure(state='normal')
	physicalanalyzer_latest.delete(0, END)
	physicalanalyzer_latest.insert(0,version)
	physicalanalyzer_latest.configure(state='readonly')
	if physicalanalyzer_current.get() == physicalanalyzer_latest.get():
		physicalanalyzer_latest.configure(readonlybackground='limegreen')
		physicalanalyzer_update.configure(text='', cursor='')
	elif physicalanalyzer_current.get() != '':
		physicalanalyzer_latest.configure(readonlybackground='orange')
		physicalanalyzer_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### OSF
	soup = BeautifulSoup(response[4].text, 'html.parser')
	version = soup.select_one('h4').text.strip()
	version = version.replace(' build ','.')
	version = version.split(' ')[0]
	version = version[1:]
	osf_latest.configure(state='normal')
	osf_latest.delete(0, END)
	osf_latest.insert(0,version)
	osf_latest.configure(state='readonly')
	if osf_current.get() == osf_latest.get():
		osf_latest.configure(readonlybackground='limegreen')
		osf_update.configure(text='', cursor='')
	elif osf_current.get() != '':
		osf_latest.configure(readonlybackground='orange')
		osf_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### ForensicExplorer
	soup = BeautifulSoup(response[5].text, 'html.parser')
	version = soup.select_one('a[href$=".exe"]')['href']
	version = version[version.index('(v'):]
	version = version[2:-5]
	forensicexplorer_latest.configure(state='normal')
	forensicexplorer_latest.delete(0, END)
	forensicexplorer_latest.insert(0,version)
	forensicexplorer_latest.configure(state='readonly')
	if forensicexplorer_current.get() == forensicexplorer_latest.get():
		forensicexplorer_latest.configure(readonlybackground='limegreen')
		forensicexplorer_update.configure(text='', cursor='')
	elif forensicexplorer_current.get() != '':
		forensicexplorer_latest.configure(readonlybackground='orange')
		forensicexplorer_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### USB Detective
	soup = BeautifulSoup(response[6].text, 'html.parser')
	version = soup.select_one('h2').text.strip()
	version = version.replace('Version ','')
	version = version.split(' ')[0]
	usbdetective_latest.configure(state='normal')
	usbdetective_latest.delete(0, END)
	usbdetective_latest.insert(0,version)
	usbdetective_latest.configure(state='readonly')
	if usbdetective_current.get() == usbdetective_latest.get():
		usbdetective_latest.configure(readonlybackground='limegreen')
		usbdetective_update.configure(text='', cursor='')
	elif usbdetective_current.get() != '':
		usbdetective_latest.configure(readonlybackground='orange')
		usbdetective_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### FTK
	soup = BeautifulSoup(response[7].text, 'html.parser')
	version = soup.select_one('a[href^="http://accessdata.com/product-download/forensic-toolkit-ftk-version"]').parent.parent.select_one('h5').text.strip()
	version = version.replace('Forensic Toolkit (FTK) version ','')
	ftk_latest.configure(state='normal')
	ftk_latest.delete(0, END)
	ftk_latest.insert(0,version)
	ftk_latest.configure(state='readonly')
	if ftk_current.get() == ftk_latest.get():
		ftk_latest.configure(readonlybackground='limegreen')
		ftk_update.configure(text='', cursor='')
	elif ftk_current.get() != '':
		ftk_latest.configure(readonlybackground='orange')
		ftk_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### FTK Imager
	soup = BeautifulSoup(response[7].text, 'html.parser')
	version = soup.select_one('a[href^="http://accessdata.com/product-download/ftk-imager-version"]').parent.parent.select_one('h5').text.strip()
	version = version.replace('FTK Imager version ','')
	ftkimager_latest.configure(state='normal')
	ftkimager_latest.delete(0, END)
	ftkimager_latest.insert(0,version)
	ftkimager_latest.configure(state='readonly')
	if ftkimager_current.get() == ftkimager_latest.get():
		ftkimager_latest.configure(readonlybackground='limegreen')
		ftkimager_update.configure(text='', cursor='')
	elif ftkimager_current.get() != '':
		ftkimager_latest.configure(readonlybackground='orange')
		ftkimager_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### XAMN
	soup = BeautifulSoup(response[8].text, 'html.parser')
	version = soup.select_one('a[href^="https://www.msab.com/download/msab_software/XAMN"]').text.strip()
	version = version.replace('XAMN Viewer v','')
	xamn_latest.configure(state='normal')
	xamn_latest.delete(0, END)
	xamn_latest.insert(0,version)
	xamn_latest.configure(state='readonly')
	if xamn_current.get() == xamn_latest.get():
		xamn_latest.configure(readonlybackground='limegreen')
		xamn_update.configure(text='', cursor='')
	elif xamn_current.get() != '':
		xamn_latest.configure(readonlybackground='orange')
		xamn_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### X-Ways
	soup = BeautifulSoup(response[9].text, 'html.parser')
	version = soup.find('div', {'class': 'content'}).select_one('b').text.strip()
	version = version[19:].strip()
	xways_latest.configure(state='normal')
	xways_latest.delete(0, END)
	xways_latest.insert(0,version)
	xways_latest.configure(state='readonly')
	if xways_current.get() == xways_latest.get():
		xways_latest.configure(readonlybackground='limegreen')
		xways_update.configure(text='', cursor='')
	elif xways_current.get() != '':
		xways_latest.configure(readonlybackground='orange')
		xways_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### CyberChef
	soup = BeautifulSoup(response[10].text, 'html.parser')
	version = soup.select_one('a[href^="https://github.com/gchq/CyberChef/releases/"]').text.strip()
	cyberchef_latest.configure(state='normal')
	cyberchef_latest.delete(0, END)
	cyberchef_latest.insert(0,version)
	cyberchef_latest.configure(state='readonly')
	if cyberchef_current.get() == cyberchef_latest.get():
		cyberchef_latest.configure(readonlybackground='limegreen')
		cyberchef_update.configure(text='', cursor='')
	elif cyberchef_current.get() != '':
		cyberchef_latest.configure(readonlybackground='orange')
		cyberchef_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### NSRL
	soup = BeautifulSoup(response[11].text, 'html.parser')
	version = soup.find('div', {'class': 'tex2jax'}).select_one('h2').text.strip()
	version = version.replace('RDS Version ','')
	version = version.split('-')[0]
	version = version[:-1]
	nsrl_latest.configure(state='normal')
	nsrl_latest.delete(0, END)
	nsrl_latest.insert(0,version)
	nsrl_latest.configure(state='readonly')
	if nsrl_current.get() == nsrl_latest.get():
		nsrl_latest.configure(readonlybackground='limegreen')
		nsrl_update.configure(text='', cursor='')
	elif nsrl_current.get() != '':
		nsrl_latest.configure(readonlybackground='orange')
		nsrl_update.configure(text='Update', fg='blue', cursor='hand2')
	
	### Forensic Version Checker
	soup = BeautifulSoup(response[12].text, 'html.parser')
	version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
	version = version.replace('v','')
	if version != '1.0':
		about.configure(text='Update FVC', fg='blue', cursor='hand2')
		about.bind('<ButtonRelease-1>', lambda e:callback('https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'))

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
	with open('current_versions.ini', 'w') as configfile:
		config.write(configfile)
	current_save.configure(text='Current versions saved', state='normal')
	latest_update()

def about_box():
	messagebox.showinfo('About', 'Forensic Version Checker v1.0\n\nTool homepage:\nhttps://github.com/jankais3r/Forensic-Version-Checker\n\nDigital Forensics Discord:\nhttps://discord.gg/pNMZunG')

tool = Label(window, text='Tool', font=('TkDefaultFont', fontsize, 'underline'), padx=5, pady=3)
tool.grid(column=0, row=0, sticky=W)
current = Label(window, text='Current Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
current.grid(column=1, row=0)
latest = Label(window, text='Latest Version', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
latest.grid(column=2, row=0)
latest = Label(window, text='Update', font=('TkDefaultFont', fontsize, 'underline'), pady=3)
latest.grid(column=3, row=0)

encase = Label(window, text='EnCase', padx=5)
encase.grid(column=0, row=1, sticky=W)
encase_current = Entry(window, width=8)
encase_current.grid(column=1, row=1, sticky=N+S+E+W)
encase_current.insert(0,config['CURRENT']['encase'])
encase_latest = Entry(window, width=8, state='readonly')
encase_latest.grid(column=2, row=1, sticky=N+S+E+W)
encase_update = Label(text='', padx=2)
encase_update.grid(column=3, row=1)
encase_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.guidancesoftware.com/encase-forensic'))

blacklight = Label(window, text='BlackLight', padx=5)
blacklight.grid(column=0, row=2, sticky=W)
blacklight_current = Entry(window, width=8)
blacklight_current.grid(column=1, row=2, sticky=N+S+E+W)
blacklight_current.insert(0,config['CURRENT']['blacklight'])
blacklight_latest = Entry(window, width=8, state='readonly')
blacklight_latest.grid(column=2, row=2, sticky=N+S+E+W)
blacklight_update = Label(text='')
blacklight_update.grid(column=3, row=2)
blacklight_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.blackbagtech.com/downloads/'))

axiom = Label(window, text='AXIOM', padx=5)
axiom.grid(column=0, row=3, sticky=W)
axiom_current = Entry(window, width=8)
axiom_current.grid(column=1, row=3, sticky=N+S+E+W)
axiom_current.insert(0,config['CURRENT']['axiom'])
axiom_latest = Entry(window, width=8, state='readonly')
axiom_latest.grid(column=2, row=3, sticky=N+S+E+W)
axiom_update = Label(text='')
axiom_update.grid(column=3, row=3)
axiom_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.magnetforensics.com/downloadaxiom/'))

ufed4pc = Label(window, text='UFED4PC', padx=5)
ufed4pc.grid(column=0, row=4, sticky=W)
ufed4pc_current = Entry(window, width=8)
ufed4pc_current.grid(column=1, row=4, sticky=N+S+E+W)
ufed4pc_current.insert(0,config['CURRENT']['ufed4pc'])
ufed4pc_latest = Entry(window, width=8, state='readonly')
ufed4pc_latest.grid(column=2, row=4, sticky=N+S+E+W)
ufed4pc_update = Label(text='')
ufed4pc_update.grid(column=3, row=4)
ufed4pc_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.cellebrite.com/en/support/product-releases/'))

physicalanalyzer = Label(window, text='Physical Analyzer', padx=5)
physicalanalyzer.grid(column=0, row=5, sticky=W)
physicalanalyzer_current = Entry(window, width=8)
physicalanalyzer_current.grid(column=1, row=5, sticky=N+S+E+W)
physicalanalyzer_current.insert(0,config['CURRENT']['physicalanalyzer'])
physicalanalyzer_latest = Entry(window, width=8, state='readonly')
physicalanalyzer_latest.grid(column=2, row=5, sticky=N+S+E+W)
physicalanalyzer_update = Label(text='')
physicalanalyzer_update.grid(column=3, row=5)
physicalanalyzer_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.cellebrite.com/en/support/product-releases/'))

osf = Label(window, text='OSForensics', padx=5)
osf.grid(column=0, row=6, sticky=W)
osf_current = Entry(window, width=8)
osf_current.grid(column=1, row=6, sticky=N+S+E+W)
osf_current.insert(0,config['CURRENT']['osf'])
osf_latest = Entry(window, width=8, state='readonly')
osf_latest.grid(column=2, row=6, sticky=N+S+E+W)
osf_update = Label(text='')
osf_update.grid(column=3, row=6)
osf_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.osforensics.com/download.html'))

forensicexplorer = Label(window, text='ForensicExplorer', padx=5)
forensicexplorer.grid(column=0, row=7, sticky=W)
forensicexplorer_current = Entry(window, width=8)
forensicexplorer_current.grid(column=1, row=7, sticky=N+S+E+W)
forensicexplorer_current.insert(0,config['CURRENT']['forensicexplorer'])
forensicexplorer_latest = Entry(window, width=8, state='readonly')
forensicexplorer_latest.grid(column=2, row=7, sticky=N+S+E+W)
forensicexplorer_update = Label(text='')
forensicexplorer_update.grid(column=3, row=7)
forensicexplorer_update.bind('<ButtonRelease-1>', lambda e:callback('http://www.forensicexplorer.com/download.php'))

usbdetective = Label(window, text='USB Detective', padx=5)
usbdetective.grid(column=0, row=8, sticky=W)
usbdetective_current = Entry(window, width=8)
usbdetective_current.grid(column=1, row=8, sticky=N+S+E+W)
usbdetective_current.insert(0,config['CURRENT']['usbdetective'])
usbdetective_latest = Entry(window, width=8, state='readonly')
usbdetective_latest.grid(column=2, row=8, sticky=N+S+E+W)
usbdetective_update = Label(text='')
usbdetective_update.grid(column=3, row=8)
usbdetective_update.bind('<ButtonRelease-1>', lambda e:callback('https://usbdetective.com/release-notes/'))

ftk = Label(window, text='FTK', padx=5)
ftk.grid(column=0, row=9, sticky=W)
ftk_current = Entry(window, width=8)
ftk_current.grid(column=1, row=9, sticky=N+S+E+W)
ftk_current.insert(0,config['CURRENT']['ftk'])
ftk_latest = Entry(window, width=8, state='readonly')
ftk_latest.grid(column=2, row=9, sticky=N+S+E+W)
ftk_update = Label(text='')
ftk_update.grid(column=3, row=9)
ftk_update.bind('<ButtonRelease-1>', lambda e:callback('https://accessdata.com/product-download'))

ftkimager = Label(window, text='FTK Imager', padx=5)
ftkimager.grid(column=0, row=10, sticky=W)
ftkimager_current = Entry(window, width=8)
ftkimager_current.grid(column=1, row=10, sticky=N+S+E+W)
ftkimager_current.insert(0,config['CURRENT']['ftkimager'])
ftkimager_latest = Entry(window, width=8, state='readonly')
ftkimager_latest.grid(column=2, row=10, sticky=N+S+E+W)
ftkimager_update = Label(text='')
ftkimager_update.grid(column=3, row=10)
ftkimager_update.bind('<ButtonRelease-1>', lambda e:callback('https://accessdata.com/product-download'))

xamn = Label(window, text='XAMN', padx=5)
xamn.grid(column=0, row=11, sticky=W)
xamn_current = Entry(window, width=8)
xamn_current.grid(column=1, row=11, sticky=N+S+E+W)
xamn_current.insert(0,config['CURRENT']['xamn'])
xamn_latest = Entry(window, width=8, state='readonly')
xamn_latest.grid(column=2, row=11, sticky=N+S+E+W)
xamn_update = Label(text='')
xamn_update.grid(column=3, row=11)
xamn_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.msab.com/downloads/'))

xways = Label(window, text='X-Ways', padx=5)
xways.grid(column=0, row=12, sticky=W)
xways_current = Entry(window, width=8)
xways_current.grid(column=1, row=12, sticky=N+S+E+W)
xways_current.insert(0,config['CURRENT']['xways'])
xways_latest = Entry(window, width=8, state='readonly')
xways_latest.grid(column=2, row=12, sticky=N+S+E+W)
xways_update = Label(text='')
xways_update.grid(column=3, row=12)
xways_update.bind('<ButtonRelease-1>', lambda e:callback('http://www.x-ways.net/winhex/license.html'))

cyberchef = Label(window, text='CyberChef', padx=5)
cyberchef.grid(column=0, row=13, sticky=W)
cyberchef_current = Entry(window, width=8)
cyberchef_current.grid(column=1, row=13, sticky=N+S+E+W)
cyberchef_current.insert(0,config['CURRENT']['cyberchef'])
cyberchef_latest = Entry(window, width=8, state='readonly')
cyberchef_latest.grid(column=2, row=13, sticky=N+S+E+W)
cyberchef_update = Label(text='')
cyberchef_update.grid(column=3, row=13)
cyberchef_update.bind('<ButtonRelease-1>', lambda e:callback('https://github.com/gchq/CyberChef/releases/latest'))

nsrl = Label(window, text='NSRL hash set', padx=5)
nsrl.grid(column=0, row=14, sticky=W)
nsrl_current = Entry(window, width=8)
nsrl_current.grid(column=1, row=14, sticky=N+S+E+W)
nsrl_current.insert(0,config['CURRENT']['nsrl'])
nsrl_latest = Entry(window, width=8, state='readonly')
nsrl_latest.grid(column=2, row=14, sticky=N+S+E+W)
nsrl_update = Label(text='')
nsrl_update.grid(column=3, row=14)
nsrl_update.bind('<ButtonRelease-1>', lambda e:callback('https://www.nist.gov/itl/ssd/software-quality-group/nsrl-download/current-rds-hash-sets'))

divider = Label(window, text='', font=('TkDefaultFont', 1, 'underline'))
divider.grid(column=1, row=15)

about = Label(window, text='?', padx=5, fg='grey', cursor='hand2')
about.grid(column=0, row=16, sticky=W)
about.bind('<ButtonRelease-1>', lambda e: about_box())

current_save = Button(window, text='Save', command=current_save)
current_save.grid(column=1, row=16, columnspan=2, sticky=N+S+E+W)

if first_run != True:
	current_save.configure(text='Checking for updates...', state='disabled')
	window.update()
	
	latest_update()
	current_save.configure(text='Save', state='normal')
	
window.mainloop()
