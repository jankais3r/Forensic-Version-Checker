#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import time
import queue
import base64
import webbrowser
import configparser
from sys import platform
from threading import Thread
from xml.etree import ElementTree

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
	from tkinter import *
	from tkinter import messagebox
except:
	print('Install tkinter with "sudo apt install python3-tk"')
	quit()
try:
	from bs4 import BeautifulSoup
except:
	print('Install BeautifulSoup with "pip3 install beautifulsoup4"')
	quit()
try:
	from tkscrolledframe import ScrolledFrame
except:
	print('Install tkScrolledFrame with "pip3 install tkScrolledFrame"')
	quit()

if os.path.isfile('current_versions.ini') == False:
	default_config = '''[CURRENT]
gui = Display all
aim = 
atola = 
autopsy = 
axiom = 
bec = 
blacklight = 
caine = 
cyberchef = 
deft = 
eift = 
encase = 
exiftool = 
ez_amcacheparser = 
ez_appcompatcacheparser = 
ez_bstrings = 
ez_evtxex = 
ez_jlecmd = 
ez_jumplistex = 
ez_lecmd = 
ez_mftecmd = 
ez_mftexplorer = 
ez_pecmd = 
ez_rbcmd = 
ez_recentfilecacheparser = 
ez_registryex = 
ez_sdbex = 
ez_shellbagex = 
ez_timelineex = 
ez_vscmount = 
ez_wxtcmd = 
fec = 
forensicexplorer = 
ffn = 
ftk = 
ftkimager = 
hashcat = 
hstex = 
irec = 
ive = 
macquisition = 
mobiledit = 
mountimagepro = 
netanalysis = 
nirsoft = 
nsrl = 
osf = 
oxygen = 
paraben = 
passware = 
physicalanalyzer = 
sleuthkit = 
ufed4pc = 
usbdetective = 
veracrypt = 
xamn = 
xways = 
'''

	try:
		configfile = open('current_versions.ini', 'w')
		configfile.write(default_config)
		configfile.close()
	except:
		print('Can\'t save the config file. Please check your permissions.')
		quit()
	first_run = True
else:
	first_run = False

config = configparser.ConfigParser()
config.read('current_versions.ini')

mt_queue = queue.Queue()
response = []

used_tools = []
used_tools_counter = 1

try:
	parsers_url = ['https://raw.githubusercontent.com/jankais3r/Forensic-Version-Checker/master/parsers.ini']
	parsers_get = (grequests.get(u) for u in parsers_url)
	parsers_responses = grequests.map(parsers_get)
	for r in parsers_responses:
		if r.status_code == 200:
			parsersfile = open('parsers.ini', 'wb')
			parsersfile.write(r.content)
			parsersfile.close()
			r.close()
		else:
			print('Couldn\'t download parser definitions. Please check your Internet connection.')
			quit()
except:
	print('Couldn\'t download parser definitions. Please check your Internet connection.')
	quit()

parsers = configparser.ConfigParser()
parsers.read('parsers.ini')

aim_parser = '\t\t\t'+(parsers['PARSERS']['aim_parser']).replace('\n', '\n\t\t\t')
atola_parser = '\t\t\t'+(parsers['PARSERS']['atola_parser']).replace('\n', '\n\t\t\t')
autopsy_parser = '\t\t\t'+(parsers['PARSERS']['autopsy_parser']).replace('\n', '\n\t\t\t')
axiom_parser = '\t\t\t'+(parsers['PARSERS']['axiom_parser']).replace('\n', '\n\t\t\t')
bec_parser = '\t\t\t'+(parsers['PARSERS']['bec_parser']).replace('\n', '\n\t\t\t')
blacklight_parser = '\t\t\t'+(parsers['PARSERS']['blacklight_parser']).replace('\n', '\n\t\t\t')
caine_parser = '\t\t\t'+(parsers['PARSERS']['caine_parser']).replace('\n', '\n\t\t\t')
cyberchef_parser = '\t\t\t'+(parsers['PARSERS']['cyberchef_parser']).replace('\n', '\n\t\t\t')
deft_parser = '\t\t\t'+(parsers['PARSERS']['deft_parser']).replace('\n', '\n\t\t\t')
eift_parser = '\t\t\t'+(parsers['PARSERS']['eift_parser']).replace('\n', '\n\t\t\t')
encase_parser = '\t\t\t'+(parsers['PARSERS']['encase_parser']).replace('\n', '\n\t\t\t')
exiftool_parser = '\t\t\t'+(parsers['PARSERS']['exiftool_parser']).replace('\n', '\n\t\t\t')
ez_amcacheparser_parser = '\t\t\t'+(parsers['PARSERS']['ez_amcacheparser_parser']).replace('\n', '\n\t\t\t')
ez_appcompatcacheparser_parser = '\t\t\t'+(parsers['PARSERS']['ez_appcompatcacheparser_parser']).replace('\n', '\n\t\t\t')
ez_bstrings_parser = '\t\t\t'+(parsers['PARSERS']['ez_bstrings_parser']).replace('\n', '\n\t\t\t')
ez_evtxex_parser = '\t\t\t'+(parsers['PARSERS']['ez_evtxex_parser']).replace('\n', '\n\t\t\t')
ez_jlecmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_jlecmd_parser']).replace('\n', '\n\t\t\t')
ez_jumplistex_parser = '\t\t\t'+(parsers['PARSERS']['ez_jumplistex_parser']).replace('\n', '\n\t\t\t')
ez_lecmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_lecmd_parser']).replace('\n', '\n\t\t\t')
ez_mftecmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_mftecmd_parser']).replace('\n', '\n\t\t\t')
ez_mftexplorer_parser = '\t\t\t'+(parsers['PARSERS']['ez_mftexplorer_parser']).replace('\n', '\n\t\t\t')
ez_pecmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_pecmd_parser']).replace('\n', '\n\t\t\t')
ez_rbcmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_rbcmd_parser']).replace('\n', '\n\t\t\t')
ez_recentfilecacheparser_parser = '\t\t\t'+(parsers['PARSERS']['ez_recentfilecacheparser_parser']).replace('\n', '\n\t\t\t')
ez_registryex_parser = '\t\t\t'+(parsers['PARSERS']['ez_registryex_parser']).replace('\n', '\n\t\t\t')
ez_sdbex_parser = '\t\t\t'+(parsers['PARSERS']['ez_sdbex_parser']).replace('\n', '\n\t\t\t')
ez_shellbagex_parser = '\t\t\t'+(parsers['PARSERS']['ez_shellbagex_parser']).replace('\n', '\n\t\t\t')
ez_timelineex_parser = '\t\t\t'+(parsers['PARSERS']['ez_timelineex_parser']).replace('\n', '\n\t\t\t')
ez_vscmount_parser = '\t\t\t'+(parsers['PARSERS']['ez_vscmount_parser']).replace('\n', '\n\t\t\t')
ez_wxtcmd_parser = '\t\t\t'+(parsers['PARSERS']['ez_wxtcmd_parser']).replace('\n', '\n\t\t\t')
fec_parser = '\t\t\t'+(parsers['PARSERS']['fec_parser']).replace('\n', '\n\t\t\t')
forensicexplorer_parser = '\t\t\t'+(parsers['PARSERS']['forensicexplorer_parser']).replace('\n', '\n\t\t\t')
ffn_parser = '\t\t\t'+(parsers['PARSERS']['ffn_parser']).replace('\n', '\n\t\t\t')
ftk_parser = '\t\t\t'+(parsers['PARSERS']['ftk_parser']).replace('\n', '\n\t\t\t')
ftkimager_parser = '\t\t\t'+(parsers['PARSERS']['ftkimager_parser']).replace('\n', '\n\t\t\t')
hashcat_parser = '\t\t\t'+(parsers['PARSERS']['hashcat_parser']).replace('\n', '\n\t\t\t')
hstex_parser = '\t\t\t'+(parsers['PARSERS']['hstex_parser']).replace('\n', '\n\t\t\t')
irec_parser = '\t\t\t'+(parsers['PARSERS']['irec_parser']).replace('\n', '\n\t\t\t')
ive_parser = '\t\t\t'+(parsers['PARSERS']['ive_parser']).replace('\n', '\n\t\t\t')
macquisition_parser = '\t\t\t'+(parsers['PARSERS']['macquisition_parser']).replace('\n', '\n\t\t\t')
mobiledit_parser = '\t\t\t'+(parsers['PARSERS']['mobiledit_parser']).replace('\n', '\n\t\t\t')
mountimagepro_parser = '\t\t\t'+(parsers['PARSERS']['mountimagepro_parser']).replace('\n', '\n\t\t\t')
netanalysis_parser = '\t\t\t'+(parsers['PARSERS']['netanalysis_parser']).replace('\n', '\n\t\t\t')
nirsoft_parser = '\t\t\t'+(parsers['PARSERS']['nirsoft_parser']).replace('\n', '\n\t\t\t')
nsrl_parser = '\t\t\t'+(parsers['PARSERS']['nsrl_parser']).replace('\n', '\n\t\t\t')
osf_parser = '\t\t\t'+(parsers['PARSERS']['osf_parser']).replace('\n', '\n\t\t\t')
oxygen_parser = '\t\t\t'+(parsers['PARSERS']['oxygen_parser']).replace('\n', '\n\t\t\t')
paraben_parser = '\t\t\t'+(parsers['PARSERS']['paraben_parser']).replace('\n', '\n\t\t\t')
passware_parser = '\t\t\t'+(parsers['PARSERS']['passware_parser']).replace('\n', '\n\t\t\t')
physicalanalyzer_parser = '\t\t\t'+(parsers['PARSERS']['physicalanalyzer_parser']).replace('\n', '\n\t\t\t')
sleuthkit_parser = '\t\t\t'+(parsers['PARSERS']['sleuthkit_parser']).replace('\n', '\n\t\t\t')
ufed4pc_parser = '\t\t\t'+(parsers['PARSERS']['ufed4pc_parser']).replace('\n', '\n\t\t\t')
usbdetective_parser = '\t\t\t'+(parsers['PARSERS']['usbdetective_parser']).replace('\n', '\n\t\t\t')
veracrypt_parser = '\t\t\t'+(parsers['PARSERS']['veracrypt_parser']).replace('\n', '\n\t\t\t')
xamn_parser = '\t\t\t'+(parsers['PARSERS']['xamn_parser']).replace('\n', '\n\t\t\t')
xways_parser = '\t\t\t'+(parsers['PARSERS']['xways_parser']).replace('\n', '\n\t\t\t')

def spinning_cursor():
	while True:
		for cursor in '|/–\\':
			yield cursor

def build_gui(fieldname, displayname, url):
	code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (gui == 'Display all' or current != ''):
	''' + fieldname + ''' = Label(inner_frame, text = \'''' + displayname + '''\', font = ('TkDefaultFont', fontsize), padx = 5)
	''' + fieldname + '''.grid(column = 0, row = rowID, sticky = W)
	''' + fieldname + '''_current = Entry(inner_frame, font = ('TkDefaultFont', fontsize), width = 8)
	''' + fieldname + '''_current.grid(column = 1, row = rowID, sticky = N+S+E+W)
	''' + fieldname + '''_current.insert(0, current)
	''' + fieldname + '''_latest = Entry(inner_frame, font = ('TkDefaultFont', fontsize), width = 8, state = 'readonly')
	''' + fieldname + '''_latest.grid(column = 2, row = rowID, sticky = N+S+E+W)
	''' + fieldname + '''_update = Label(inner_frame, text = '', font = ('TkDefaultFont', fontsize))
	''' + fieldname + '''_update.grid(column = 3, row = rowID, sticky = W)
	''' + fieldname + '''_update.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new(\'''' + url + '''\'))
	widget_order.append(''' + fieldname + '''_current)
	used_tools.append(\'''' + fieldname + '''\')
	rowID += 1
''', '<string>', 'exec')
	exec(code, globals(), globals())

def update_gui(fieldname, parsing):
	code = compile('''
global response
global used_tools_counter
try:
	current = ''' + fieldname + '''_current.get()
except:
	current = ''
if (gui == 'Display all' or current != ''):
	try:
''' + parsing + '''
	except:
		version = 'Error'
		''' + fieldname + '''_latest.configure(readonlybackground = 'red')
try:
	''' + fieldname + '''_latest.configure(state = 'normal')
	''' + fieldname + '''_latest.delete(0, END)
	''' + fieldname + '''_latest.insert(0, version)
	''' + fieldname + '''_latest.configure(state = 'readonly')
	if ''' + fieldname + '''_current.get() == ''' + fieldname + '''_latest.get():
		''' + fieldname + '''_latest.configure(readonlybackground = 'limegreen')
		''' + fieldname + '''_update.configure(text = '', cursor = '')
	elif ((''' + fieldname + '''_current.get() != '') and (''' + fieldname + '''_latest.get() != 'Error')):
		''' + fieldname + '''_latest.configure(readonlybackground = 'orange')
		''' + fieldname + '''_update.configure(text = 'Update', fg = 'blue', cursor = 'hand2')
	used_tools_counter += 1
except:
	pass
''', '<string>', 'exec')
	exec(code, globals(), globals())

def gather_used_tools(fieldname):
	code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (current != ''):
	used_tools.append(\'''' + fieldname + '''\')
''', '<string>', 'exec')
	exec(code, globals(), globals())

def update_cli(fieldname, displayname, parsing):
	code = compile('''
try:
	current = config['CURRENT'][\'''' + fieldname + '''\']
except:
	current = ''
if (current != ''):
	try:
''' + parsing + '''
	except:
		version = 'Error'
	if ((current == version) or (version == 'Error')):
		table.append([\'''' + displayname + '''\', current, version, ''])
	else:
		table.append([\'''' + displayname + '''\', current, version, 'Update available!'])
	used_tools_counter += 1
''', '<string>', 'exec')
	exec(code, globals(), globals())

def crawl():
	ua_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
	}
	
	all_urls = {'fvc'						:	parsers['URLS']['fvc'],
				'aim'						:	parsers['URLS']['aim'],
				'atola'						:	parsers['URLS']['atola'],
				'autopsy'					:	parsers['URLS']['autopsy'],
				'axiom'						:	parsers['URLS']['axiom'],
				'bec'						:	parsers['URLS']['bec'],
				'blacklight'				:	parsers['URLS']['blacklight'],
				'caine'						:	parsers['URLS']['caine'],
				'cyberchef'					:	parsers['URLS']['cyberchef'],
				'deft'						:	parsers['URLS']['deft'],
				'eift'						:	parsers['URLS']['eift'],
				'encase'					:	parsers['URLS']['encase'],
				'exiftool'					:	parsers['URLS']['exiftool'],
				'ez_amcacheparser'			:	parsers['URLS']['ez_amcacheparser'],
				'ez_appcompatcacheparser'	:	parsers['URLS']['ez_appcompatcacheparser'],
				'ez_bstrings'				:	parsers['URLS']['ez_bstrings'],
				'ez_evtxex'					:	parsers['URLS']['ez_evtxex'],
				'ez_jlecmd'					:	parsers['URLS']['ez_jlecmd'],
				'ez_jumplistex'				:	parsers['URLS']['ez_jumplistex'],
				'ez_lecmd'					:	parsers['URLS']['ez_lecmd'],
				'ez_mftecmd'				:	parsers['URLS']['ez_mftecmd'],
				'ez_mftexplorer'			:	parsers['URLS']['ez_mftexplorer'],
				'ez_pecmd'					:	parsers['URLS']['ez_pecmd'],
				'ez_rbcmd'					:	parsers['URLS']['ez_rbcmd'],
				'ez_recentfilecacheparser'	:	parsers['URLS']['ez_recentfilecacheparser'],
				'ez_registryex'				:	parsers['URLS']['ez_registryex'],
				'ez_sdbex'					:	parsers['URLS']['ez_sdbex'],
				'ez_shellbagex'				:	parsers['URLS']['ez_shellbagex'],
				'ez_timelineex'				:	parsers['URLS']['ez_timelineex'],
				'ez_vscmount'				:	parsers['URLS']['ez_vscmount'],
				'ez_wxtcmd'					:	parsers['URLS']['ez_wxtcmd'],
				'fec'						:	parsers['URLS']['fec'],
				'forensicexplorer'			:	parsers['URLS']['forensicexplorer'],
				'ffn'						:	parsers['URLS']['ffn'],
				'ftk'						:	parsers['URLS']['ftk'],
				'ftkimager'					:	parsers['URLS']['ftkimager'],
				'hashcat'					:	parsers['URLS']['hashcat'],
				'hstex'						:	parsers['URLS']['hstex'],
				'irec'						:	parsers['URLS']['irec'],
				'ive'						:	parsers['URLS']['ive'],
				'macquisition'				:	parsers['URLS']['macquisition'],
				'mobiledit'					:	parsers['URLS']['mobiledit'],
				'mountimagepro'				:	parsers['URLS']['mountimagepro'],
				'netanalysis'				:	parsers['URLS']['netanalysis'],
				'nirsoft'					:	parsers['URLS']['nirsoft'],
				'nsrl'						:	parsers['URLS']['nsrl'],
				'osf'						:	parsers['URLS']['osf'],
				'oxygen'					:	parsers['URLS']['oxygen'],
				'paraben'					:	parsers['URLS']['paraben'],
				'passware'					:	parsers['URLS']['passware'],
				'physicalanalyzer'			:	parsers['URLS']['physicalanalyzer'],
				'sleuthkit'					:	parsers['URLS']['sleuthkit'],
				'ufed4pc'					:	parsers['URLS']['ufed4pc'],
				'usbdetective'				:	parsers['URLS']['usbdetective'],
				'veracrypt'					:	parsers['URLS']['veracrypt'],
				'xamn'						:	parsers['URLS']['xamn'],
				'xways'						:	parsers['URLS']['xways']
	}
	
	urls = []
	urls.append(all_urls['fvc'])
	for tool in used_tools:
		urls.append(all_urls[tool])
	
	mt_queue.put(grequests.map((grequests.get(u, headers = ua_headers) for u in urls)))

def refresh_gui():
	global response
	global used_tools_counter
	used_tools_counter = 1
	
	current_save.configure(state = 'disabled')
	gui_toggle.configure(state = 'disabled')
	for widget in widget_order:
		widget.configure(state = 'disabled')
	
	thread = Thread(target = crawl)
	thread.start()
	
	while(thread.is_alive()):
		current_save.configure(text = 'Checking for updates·..')
		root.update()
		time.sleep(0.15)
		current_save.configure(text = 'Checking for updates.·.')
		root.update()
		time.sleep(0.15)
		current_save.configure(text = 'Checking for updates..·')
		root.update()
		time.sleep(0.15)
		current_save.configure(text = 'Checking for updates...')
		for _ in range(10):
			root.update()
			time.sleep(0.15)
	
	response = mt_queue.get()
	
	update_gui('aim', aim_parser)	
	update_gui('atola', atola_parser)
	update_gui('autopsy', autopsy_parser)
	update_gui('axiom', axiom_parser)
	update_gui('bec', bec_parser)
	update_gui('blacklight', blacklight_parser)
	update_gui('caine', caine_parser)
	update_gui('cyberchef', cyberchef_parser)
	update_gui('deft', deft_parser)
	update_gui('eift', eift_parser)
	update_gui('encase', encase_parser)
	update_gui('exiftool', exiftool_parser)
	update_gui('ez_amcacheparser', ez_amcacheparser_parser)
	update_gui('ez_appcompatcacheparser', ez_appcompatcacheparser_parser)
	update_gui('ez_bstrings', ez_bstrings_parser)
	update_gui('ez_evtxex', ez_evtxex_parser)
	update_gui('ez_jlecmd', ez_jlecmd_parser)
	update_gui('ez_jumplistex', ez_jumplistex_parser)
	update_gui('ez_lecmd', ez_lecmd_parser)
	update_gui('ez_mftecmd', ez_mftecmd_parser)
	update_gui('ez_mftexplorer', ez_mftexplorer_parser)
	update_gui('ez_pecmd', ez_pecmd_parser)
	update_gui('ez_rbcmd', ez_rbcmd_parser)
	update_gui('ez_recentfilecacheparser', ez_recentfilecacheparser_parser)
	update_gui('ez_registryex', ez_registryex_parser)
	update_gui('ez_sdbex', ez_sdbex_parser)
	update_gui('ez_shellbagex', ez_shellbagex_parser)
	update_gui('ez_timelineex', ez_timelineex_parser)
	update_gui('ez_vscmount', ez_vscmount_parser)
	update_gui('ez_wxtcmd', ez_wxtcmd_parser)
	update_gui('fec', fec_parser)
	update_gui('forensicexplorer', forensicexplorer_parser)
	update_gui('ffn', ffn_parser)
	update_gui('ftk', ftk_parser)
	update_gui('ftkimager', ftkimager_parser)
	update_gui('hashcat', hashcat_parser)
	update_gui('hstex', hstex_parser)
	update_gui('irec', irec_parser)
	update_gui('ive', ive_parser)
	update_gui('macquisition', macquisition_parser)
	update_gui('mobiledit', mobiledit_parser)
	update_gui('mountimagepro', mountimagepro_parser)
	update_gui('netanalysis', netanalysis_parser)
	update_gui('nirsoft', nirsoft_parser)
	update_gui('nsrl', nsrl_parser)
	update_gui('osf', osf_parser)
	update_gui('oxygen', oxygen_parser)
	update_gui('paraben', paraben_parser)
	update_gui('passware', passware_parser)
	update_gui('physicalanalyzer', physicalanalyzer_parser)
	update_gui('sleuthkit', sleuthkit_parser)
	update_gui('ufed4pc', ufed4pc_parser)
	update_gui('usbdetective', usbdetective_parser)
	update_gui('veracrypt', veracrypt_parser)
	update_gui('xamn', xamn_parser)
	update_gui('xways', xways_parser)
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[0].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v', '')
	except:
		version = '1.11'
	if version != '1.11':
		about.configure(text = 'Update FVC', fg = 'blue', cursor = 'hand2')
		about.bind('<ButtonRelease-1>', lambda e:webbrowser.open_new('https://github.com/jankais3r/Forensic-Version-Checker/releases/latest'))
	
	current_save.configure(text = 'Save', state = 'normal')
	gui_toggle.configure(state = 'normal')
	
	for widget in widget_order:
		widget.configure(state = 'normal')

def run_cli():
	global response
	table_headers = ['Tool', 'Current Version', 'Latest Version', 'Update?']
	
	gather_used_tools('aim')
	gather_used_tools('atola')
	gather_used_tools('autopsy')
	gather_used_tools('axiom')
	gather_used_tools('bec')
	gather_used_tools('blacklight')
	gather_used_tools('caine')
	gather_used_tools('cyberchef')
	gather_used_tools('deft')
	gather_used_tools('eift')
	gather_used_tools('encase')
	gather_used_tools('exiftool')
	gather_used_tools('ez_amcacheparser')
	gather_used_tools('ez_appcompatcacheparser')
	gather_used_tools('ez_bstrings')
	gather_used_tools('ez_evtxex')
	gather_used_tools('ez_jlecmd')
	gather_used_tools('ez_jumplistex')
	gather_used_tools('ez_lecmd')
	gather_used_tools('ez_mftecmd')
	gather_used_tools('ez_mftexplorer')
	gather_used_tools('ez_pecmd')
	gather_used_tools('ez_rbcmd')
	gather_used_tools('ez_recentfilecacheparser')
	gather_used_tools('ez_registryex')
	gather_used_tools('ez_sdbex')
	gather_used_tools('ez_shellbagex')
	gather_used_tools('ez_timelineex')
	gather_used_tools('ez_vscmount')
	gather_used_tools('ez_wxtcmd')
	gather_used_tools('fec')
	gather_used_tools('forensicexplorer')
	gather_used_tools('ffn')
	gather_used_tools('ftk')
	gather_used_tools('ftkimager')
	gather_used_tools('hashcat')
	gather_used_tools('hstex')
	gather_used_tools('irec')
	gather_used_tools('ive')
	gather_used_tools('macquisition')
	gather_used_tools('mobiledit')
	gather_used_tools('mountimagepro')
	gather_used_tools('netanalysis')
	gather_used_tools('nirsoft')
	gather_used_tools('nsrl')
	gather_used_tools('osf')
	gather_used_tools('oxygen')
	gather_used_tools('paraben')
	gather_used_tools('passware')
	gather_used_tools('physicalanalyzer')
	gather_used_tools('sleuthkit')
	gather_used_tools('ufed4pc')
	gather_used_tools('usbdetective')
	gather_used_tools('veracrypt')
	gather_used_tools('xamn')
	gather_used_tools('xways')
	
	thread = Thread(target = crawl)
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
	
	update_cli('aim', 'AIM', aim_parser)
	update_cli('atola', 'Atola TaskForce', atola_parser)
	update_cli('autopsy', 'Autopsy', autopsy_parser)
	update_cli('axiom', 'AXIOM', axiom_parser)
	update_cli('bec', 'BEC', bec_parser)
	update_cli('blacklight', 'BlackLight', blacklight_parser)
	update_cli('caine', 'CAINE', caine_parser)
	update_cli('cyberchef', 'CyberChef', cyberchef_parser)
	update_cli('deft', 'DEFT', deft_parser)
	update_cli('eift', 'EIFT', eift_parser)
	update_cli('encase', 'Encase', encase_parser)
	update_cli('exiftool', 'ExifTool', exiftool_parser)
	update_cli('ez_amcacheparser', 'EZ AmcacheParser',  ez_amcacheparser_parser)
	update_cli('ez_appcompatcacheparser', 'EZ AppCompatCacheParser',  ez_appcompatcacheparser_parser)
	update_cli('ez_bstrings', 'EZ bstrings',  ez_bstrings_parser)
	update_cli('ez_evtxex', 'EZ Evtx Explorer/EvtxECmd',  ez_evtxex_parser)
	update_cli('ez_jlecmd', 'EZ JLECmd',  ez_jlecmd_parser)
	update_cli('ez_jumplistex', 'EZ JumpList Explorer',  ez_jumplistex_parser)
	update_cli('ez_lecmd', 'EZ LECmd',  ez_lecmd_parser)
	update_cli('ez_mftecmd', 'EZ MFTECmd',  ez_mftecmd_parser)
	update_cli('ez_mftexplorer', 'EZ MFTExplorer',  ez_mftexplorer_parser)
	update_cli('ez_pecmd', 'EZ PECmd',  ez_pecmd_parser)
	update_cli('ez_rbcmd', 'EZ RBCmd',  ez_rbcmd_parser)
	update_cli('ez_recentfilecacheparser', 'EZ RecentFileCacheParser',  ez_recentfilecacheparser_parser)
	update_cli('ez_registryex', 'EZ Registry Explorer/RECmd',  ez_registryex_parser)
	update_cli('ez_sdbex', 'EZ SDB Explorer',  ez_sdbex_parser)
	update_cli('ez_shellbagex', 'EZ ShellBags Explorer',  ez_shellbagex_parser)
	update_cli('ez_timelineex', 'EZ Timeline Explorer',  ez_timelineex_parser)
	update_cli('ez_vscmount', 'EZ VSCMount',  ez_vscmount_parser)
	update_cli('ez_wxtcmd', 'EZ WxTCmd',  ez_wxtcmd_parser)
	update_cli('fec', 'Forensic Email Collector', fec_parser)
	update_cli('forensicexplorer', 'Forensic Explorer', forensicexplorer_parser)
	update_cli('ffn', 'Forensic Falcon Neo', ffn_parser)
	update_cli('ftk', 'FTK', ftk_parser)
	update_cli('ftkimager', 'FTK Imager', ftkimager_parser)
	update_cli('hashcat', 'hashcat', hashcat_parser)
	update_cli('hstex', 'HstEx', hstex_parser)
	update_cli('irec', 'IREC', irec_parser)
	update_cli('ive', 'iVe', ive_parser)
	update_cli('macquisition', 'MacQuisition', macquisition_parser)
	update_cli('mobiledit', 'MobilEdit', mobiledit_parser)
	update_cli('mountimagepro', 'Mount Image Pro', mountimagepro_parser)
	update_cli('netanalysis', 'NetAnalysis', netanalysis_parser)
	update_cli('nirsoft', 'NirSoft Launcher', nirsoft_parser)
	update_cli('nsrl', 'NSRL hash set', nsrl_parser)
	update_cli('osf', 'OSForensics', osf_parser)
	update_cli('oxygen', 'Oxygen Forensic', oxygen_parser)
	update_cli('paraben', 'Paraben E3', paraben_parser)
	update_cli('passware', 'Passware', passware_parser)
	update_cli('physicalanalyzer', 'Physical Analyzer', physicalanalyzer_parser)
	update_cli('sleuthkit', 'The Sleuth Kit', sleuthkit_parser)
	update_cli('ufed4pc', 'UFED 4PC', ufed4pc_parser)
	update_cli('usbdetective', 'USB Detective', usbdetective_parser)
	update_cli('veracrypt', 'VeraCrypt', veracrypt_parser)
	update_cli('xamn', 'XAMN', xamn_parser)
	update_cli('xways', 'X-Ways', xways_parser)
	
	print(tabulate(table, headers = table_headers, disable_numparse = True))
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[0].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v', '')
	except:
		version = '1.11'
	if (version == '1.11'):
		pass
	else:
		print('')
		print('FVC update available!')

def save():
	config['CURRENT']['gui'] = gui_option.get()
	for tool in used_tools:
		code = compile('''
config['CURRENT'][\'''' + tool + '''\'] = ''' + tool + '''_current.get()
''', '<string>', 'exec')
		exec(code, globals(), globals())
	
	with open('current_versions.ini', 'w') as configfile:
		config.write(configfile)
	
	refresh_gui()
	current_save.configure(text = 'Current versions saved', state = 'normal')
	gui_toggle.configure(state = 'normal')

def about_box():
	messagebox.showinfo('About', 'Forensic Version Checker v1.11\n\n\
Tool\'s homepage:\nhttps://github.com/jankais3r/Forensic-Version-Checker\n\n\
Digital Forensics Discord:\nhttps://discord.gg/pNMZunG')

def get_max_height():
	helper = Tk()
	helper.attributes('-alpha', 0)
	if os.name == 'nt':
		helper.state('zoomed')
		helper.update()
		usable_height = helper.winfo_height()
	else:
		usable_height = helper.winfo_screenheight()
	helper.destroy()
	return usable_height

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
	root = Tk()
	root.attributes('-alpha', 0)
	root.title('Forensic Version Checker')
	
	sf = ScrolledFrame(root, scrollbars = 'vertical')
	sf.pack(side = 'top', expand = True, fill = 'both')
	sf.bind_scroll_wheel(root)
	inner_frame = sf.display_widget(Frame)
	
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
	try:
		icon = base64.b64decode(icon)
		icon = PhotoImage(data = icon)
		root.tk.call('wm', 'iconphoto', root._w, icon)
	except:
		pass
	
	if os.name == 'nt':
		fontsize = 9
	elif platform == 'darwin':
		fontsize = 12
	else:
		fontsize = 10
	
	rowID = 0
	tool = Label(inner_frame, text = 'Tool', font = ('TkDefaultFont', fontsize, 'underline'), padx = 5, pady = 3)
	tool.grid(column = 0, row = rowID, sticky = W)
	current = Label(inner_frame, text = 'Current Version', font = ('TkDefaultFont', fontsize, 'underline'), pady = 3)
	current.grid(column = 1, row = rowID)
	latest = Label(inner_frame, text = 'Latest Version', font = ('TkDefaultFont', fontsize, 'underline'), pady = 3)
	latest.grid(column = 2, row = rowID)
	latest = Label(inner_frame, text = 'Update', font = ('TkDefaultFont', fontsize, 'underline'), pady = 3)
	latest.grid(column = 3, row = rowID, padx = (0, 10), sticky = W)
	rowID += 1
	
	widget_order = []
	
	build_gui('aim', 'AIM', 'https://arsenalrecon.com/downloads/')
	build_gui('atola', 'Atola TaskForce', 'https://atola.com/products/taskforce/download.html')
	build_gui('autopsy', 'Autopsy', 'https://github.com/sleuthkit/autopsy/releases/latest')
	build_gui('axiom', 'AXIOM', 'https://www.magnetforensics.com/downloadaxiom/')
	build_gui('bec', 'BEC', 'https://belkasoft.com/get')
	build_gui('blacklight', 'BlackLight', 'https://www.blackbagtech.com/downloads/')
	build_gui('caine', 'CAINE', 'https://www.caine-live.net/')
	build_gui('cyberchef', 'CyberChef', 'https://github.com/gchq/CyberChef/releases/latest')
	build_gui('deft', 'DEFT', 'http://na.mirror.garr.it/mirrors/deft/zero/')
	build_gui('eift', 'EIFT', 'https://www.elcomsoft.com/eift.html')
	build_gui('encase', 'EnCase', 'https://www.guidancesoftware.com/encase-forensic')
	build_gui('exiftool', 'ExifTool', 'https://owl.phy.queensu.ca/~phil/exiftool/')
	build_gui('ez_amcacheparser', 'EZ AmcacheParser', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_appcompatcacheparser', 'EZ AppCompatCacheParser', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_bstrings', 'EZ bstrings', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_evtxex', 'EZ Evtx Explorer/EvtxECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_jlecmd', 'EZ JLECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_jumplistex', 'EZ JumpList Explorer', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_lecmd', 'EZ LECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_mftecmd', 'EZ MFTECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_mftexplorer', 'EZ MFTExplorer', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_pecmd', 'EZ PECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_rbcmd', 'EZ RBCmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_recentfilecacheparser', 'EZ RecentFileCacheParser', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_registryex', 'EZ Registry Explorer/RECmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_sdbex', 'EZ SDB Explorer', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_shellbagex', 'EZ ShellBags Explorer', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_timelineex', 'EZ Timeline Explorer', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_vscmount', 'EZ VSCMount', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('ez_wxtcmd', 'EZ WxTCmd', 'https://ericzimmerman.github.io/#!index.md')
	build_gui('fec', 'Forensic Email Collector', 'http://www.metaspike.com/fec-change-log/')
	build_gui('forensicexplorer', 'Forensic Explorer', 'http://www.forensicexplorer.com/download.php')
	build_gui('ffn', 'Forensic Falcon Neo', 'https://www.logicube.com/knowledge/forensic-falcon-neo/')
	build_gui('ftk', 'FTK', 'https://accessdata.com/product-download')
	build_gui('ftkimager', 'FTK Imager', 'https://accessdata.com/product-download')
	build_gui('hashcat', 'hashcat', 'https://hashcat.net/beta/')
	build_gui('hstex', 'HstEx', 'https://www.digital-detective.net/start/hstex-quick-start/')
	build_gui('irec', 'IREC', 'https://binalyze.com/products/irec/release-notes/')
	build_gui('ive', 'iVe', 'https://berla.co/customer-support/')
	build_gui('macquisition', 'MacQuisition', 'https://www.blackbagtech.com/downloads/')
	build_gui('mobiledit', 'MobilEdit', 'https://www.mobiledit.com/downloads')
	build_gui('mountimagepro', 'Mount Image Pro', 'http://www.forensicexplorer.com/download.php')
	build_gui('netanalysis', 'NetAnalysis', 'https://www.digital-detective.net/start/netanalysis-quick-start/')
	build_gui('nirsoft', 'NirSoft Launcher', 'https://launcher.nirsoft.net/downloads/index.html')
	build_gui('nsrl', 'NSRL hash set', 'https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds')
	build_gui('osf', 'OSForensics', 'https://www.osforensics.com/download.html')
	build_gui('oxygen', 'Oxygen Forensic', 'http://www.oxygen-forensic.com/download/whatsnew/OFD/WhatsNew.html')
	build_gui('paraben', 'Paraben E3', 'https://paraben.com/paraben-downloads/')
	build_gui('passware', 'Passware', 'https://www.passware.com/kit-forensic/whatsnew/')
	build_gui('physicalanalyzer', 'Physical Analyzer', 'https://www.cellebrite.com/en/support/product-releases/')
	build_gui('sleuthkit', 'The Sleuth Kit', 'https://github.com/sleuthkit/sleuthkit/releases/latest')
	build_gui('ufed4pc', 'UFED 4PC', 'https://www.cellebrite.com/en/support/product-releases/')
	build_gui('usbdetective', 'USB Detective', 'https://usbdetective.com/release-notes/')
	build_gui('veracrypt', 'VeraCrypt', 'https://www.veracrypt.fr/en/Downloads.html')
	build_gui('xamn', 'XAMN', 'https://www.msab.com/downloads/')
	build_gui('xways', 'X-Ways', 'http://www.x-ways.net/winhex/license.html')
	
	gui_option = StringVar()
	gui_option.set(gui)
	gui_toggle = OptionMenu(inner_frame, gui_option, 'Display all', 'Display used', 'CLI mode')
	
	current_save = Button(inner_frame, text = 'Save', command = save)
	current_save.grid(column = 1, row = rowID, columnspan = 2, sticky = E+W, pady = (7, 7))
	
	pixel = PhotoImage(width = 1, height = 1)
	if os.name == 'nt':
		gui_toggle.config(image = pixel, height = 14, compound = 'c')
		gui_toggle.grid(column = 0, row = rowID, sticky = N+S+W, padx = (5, 0), pady = (7, 7))
		current_save.config(image = pixel, height = 18, compound = 'c')
	elif platform == 'darwin':
		gui_toggle.config(image = pixel, height = 18, compound = 'c')
		gui_toggle.grid(column = 0, row = rowID, sticky = N+S+W, padx = (4, 0), pady = (5, 7))
		current_save.config(image = pixel, height = 14, compound = 'c')
	else:
		gui_toggle.config(image = pixel, height = 16, compound = 'c')
		gui_toggle.grid(column = 0, row = rowID, sticky = N+S+W, padx = (4, 0), pady = (7, 7))
		current_save.config(image = pixel, height = 16, compound = 'c')
	
	about = Label(inner_frame, text = '    ?', font = ('TkDefaultFont', fontsize), fg = 'grey', cursor = 'hand2')
	about.grid(column = 3, row = rowID, pady = (7, 7), sticky = W)
	about.bind('<ButtonRelease-1>', lambda e: about_box())
	
	root.update()
	max_heigth = get_max_height()
	
	if (inner_frame.winfo_height() > (max_heigth - 100)) and max_heigth != 200:
		sf.configure(height = max_heigth - 100, width = inner_frame.winfo_width() + 20)
		root.resizable(False, True)
	else:
		sf.configure(height = inner_frame.winfo_height(), width = inner_frame.winfo_width() + 20)
		root.resizable(False, True)
	
	root.attributes('-alpha', 1)
	root.lift()
	root.attributes('-topmost', True)
	root.attributes('-topmost', False)
	
	if first_run != True:
		refresh_gui()
	else:
		messagebox.showinfo('Welcome', 'A new config file has been created.\n\n\
Please populate your current tool versions,\nchoose a display mode, and click Save.')
	
	for widget in widget_order:
		widget.lift()
	
	while True:
		try:
			root.mainloop()
			break
		except UnicodeDecodeError:
			pass
else:
	table = []
	run_cli()
