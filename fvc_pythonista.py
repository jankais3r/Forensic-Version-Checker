#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import re
import sys
import time
import queue
import base64
import console
import requests
import configparser
from threading import Thread
from bs4 import BeautifulSoup
from xml.etree import ElementTree

try:
	from tabulate import tabulate
except:
	print('Install tabulate using StaSh with "pip install tabulate"')
	quit()

if os.path.isfile('current_versions.ini') == False:
	default_config = '''[CURRENT]
gui = CLI mode
aim = 
aleapp = 
atola = 
autopsy = 
avml = 
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
fresponse = 
ftk = 
ftkimager = 
hashcat = 
hstex = 
ileapp = 
irec = 
ive = 
kali = 
kape = 
lime = 
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
tzworks = 
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
	print('Config file \'current_versions.ini\' has been created. Please populate it with your current versions and re-run the script.')
	quit()

config = configparser.ConfigParser()
config.read('current_versions.ini')

response = []

used_tools = []
used_tools_counter = 1

try:
	parsers_get = requests.get('https://raw.githubusercontent.com/jankais3r/Forensic-Version-Checker/master/parsers.ini')
	if parsers_get.status_code == 200:
		parsersfile = open('parsers.ini', 'wb')
		parsersfile.write(parsers_get.content)
		parsersfile.close()
	else:
		print('Couldn\'t download parser definitions. Please check your Internet connection.')
		quit()
except:
	print('Couldn\'t download parser definitions. Please check your Internet connection.')
	quit()

parsers = configparser.ConfigParser()
parsers.read('parsers.ini')

aim_parser = (parsers['PARSERS']['aim_parser']).replace('\\t', '\t')
aleapp_parser = (parsers['PARSERS']['aleapp_parser']).replace('\\t', '\t')
atola_parser = (parsers['PARSERS']['atola_parser']).replace('\\t', '\t')
autopsy_parser = (parsers['PARSERS']['autopsy_parser']).replace('\\t', '\t')
avml_parser = (parsers['PARSERS']['avml_parser']).replace('\\t', '\t')
axiom_parser = (parsers['PARSERS']['axiom_parser']).replace('\\t', '\t')
bec_parser = (parsers['PARSERS']['bec_parser']).replace('\\t', '\t')
blacklight_parser = (parsers['PARSERS']['blacklight_parser']).replace('\\t', '\t')
caine_parser = (parsers['PARSERS']['caine_parser']).replace('\\t', '\t')
cyberchef_parser = (parsers['PARSERS']['cyberchef_parser']).replace('\\t', '\t')
deft_parser = (parsers['PARSERS']['deft_parser']).replace('\\t', '\t')
eift_parser = (parsers['PARSERS']['eift_parser']).replace('\\t', '\t')
encase_parser = (parsers['PARSERS']['encase_parser']).replace('\\t', '\t')
exiftool_parser = (parsers['PARSERS']['exiftool_parser']).replace('\\t', '\t')
ez_amcacheparser_parser = (parsers['PARSERS']['ez_amcacheparser_parser']).replace('\\t', '\t')
ez_appcompatcacheparser_parser = (parsers['PARSERS']['ez_appcompatcacheparser_parser']).replace('\\t', '\t')
ez_bstrings_parser = (parsers['PARSERS']['ez_bstrings_parser']).replace('\\t', '\t')
ez_evtxex_parser = (parsers['PARSERS']['ez_evtxex_parser']).replace('\\t', '\t')
ez_jlecmd_parser = (parsers['PARSERS']['ez_jlecmd_parser']).replace('\\t', '\t')
ez_jumplistex_parser = (parsers['PARSERS']['ez_jumplistex_parser']).replace('\\t', '\t')
ez_lecmd_parser = (parsers['PARSERS']['ez_lecmd_parser']).replace('\\t', '\t')
ez_mftecmd_parser = (parsers['PARSERS']['ez_mftecmd_parser']).replace('\\t', '\t')
ez_mftexplorer_parser = (parsers['PARSERS']['ez_mftexplorer_parser']).replace('\\t', '\t')
ez_pecmd_parser = (parsers['PARSERS']['ez_pecmd_parser']).replace('\\t', '\t')
ez_rbcmd_parser = (parsers['PARSERS']['ez_rbcmd_parser']).replace('\\t', '\t')
ez_recentfilecacheparser_parser = (parsers['PARSERS']['ez_recentfilecacheparser_parser']).replace('\\t', '\t')
ez_registryex_parser = (parsers['PARSERS']['ez_registryex_parser']).replace('\\t', '\t')
ez_sdbex_parser = (parsers['PARSERS']['ez_sdbex_parser']).replace('\\t', '\t')
ez_shellbagex_parser = (parsers['PARSERS']['ez_shellbagex_parser']).replace('\\t', '\t')
ez_timelineex_parser = (parsers['PARSERS']['ez_timelineex_parser']).replace('\\t', '\t')
ez_vscmount_parser = (parsers['PARSERS']['ez_vscmount_parser']).replace('\\t', '\t')
ez_wxtcmd_parser = (parsers['PARSERS']['ez_wxtcmd_parser']).replace('\\t', '\t')
fec_parser = (parsers['PARSERS']['fec_parser']).replace('\\t', '\t')
forensicexplorer_parser = (parsers['PARSERS']['forensicexplorer_parser']).replace('\\t', '\t')
ffn_parser = (parsers['PARSERS']['ffn_parser']).replace('\\t', '\t')
fresponse_parser = (parsers['PARSERS']['fresponse_parser']).replace('\\t', '\t')
ftk_parser = (parsers['PARSERS']['ftk_parser']).replace('\\t', '\t')
ftkimager_parser = (parsers['PARSERS']['ftkimager_parser']).replace('\\t', '\t')
hashcat_parser = (parsers['PARSERS']['hashcat_parser']).replace('\\t', '\t')
hstex_parser = (parsers['PARSERS']['hstex_parser']).replace('\\t', '\t')
ileapp_parser = (parsers['PARSERS']['ileapp_parser']).replace('\\t', '\t')
irec_parser = (parsers['PARSERS']['irec_parser']).replace('\\t', '\t')
ive_parser = (parsers['PARSERS']['ive_parser']).replace('\\t', '\t')
kali_parser = (parsers['PARSERS']['kali_parser']).replace('\\t', '\t')
lime_parser = (parsers['PARSERS']['lime_parser']).replace('\\t', '\t')
macquisition_parser = (parsers['PARSERS']['macquisition_parser']).replace('\\t', '\t')
mobiledit_parser = (parsers['PARSERS']['mobiledit_parser']).replace('\\t', '\t')
mountimagepro_parser = (parsers['PARSERS']['mountimagepro_parser']).replace('\\t', '\t')
netanalysis_parser = (parsers['PARSERS']['netanalysis_parser']).replace('\\t', '\t')
nirsoft_parser = (parsers['PARSERS']['nirsoft_parser']).replace('\\t', '\t')
nsrl_parser = (parsers['PARSERS']['nsrl_parser']).replace('\\t', '\t')
osf_parser = (parsers['PARSERS']['osf_parser']).replace('\\t', '\t')
oxygen_parser = (parsers['PARSERS']['oxygen_parser']).replace('\\t', '\t')
paraben_parser = (parsers['PARSERS']['paraben_parser']).replace('\\t', '\t')
passware_parser = (parsers['PARSERS']['passware_parser']).replace('\\t', '\t')
physicalanalyzer_parser = (parsers['PARSERS']['physicalanalyzer_parser']).replace('\\t', '\t')
sleuthkit_parser = (parsers['PARSERS']['sleuthkit_parser']).replace('\\t', '\t')
tzworks_parser = (parsers['PARSERS']['tzworks_parser']).replace('\\t', '\t')
ufed4pc_parser = (parsers['PARSERS']['ufed4pc_parser']).replace('\\t', '\t')
usbdetective_parser = (parsers['PARSERS']['usbdetective_parser']).replace('\\t', '\t')
veracrypt_parser = (parsers['PARSERS']['veracrypt_parser']).replace('\\t', '\t')
xamn_parser = (parsers['PARSERS']['xamn_parser']).replace('\\t', '\t')
xways_parser = (parsers['PARSERS']['xways_parser']).replace('\\t', '\t')

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
		table.append([\'''' + displayname + '''\', current, version, '¿' + \'''' + fieldname + '''\' + '¿'])
	used_tools_counter += 1
''', '<string>', 'exec')
	exec(code, globals(), globals())

def crawl():
	ua_headers = {
		'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.97 Safari/537.36'
	}
	
	all_urls = {'fvc'						:	parsers['URLS']['fvc'],
				'aim'						:	parsers['URLS']['aim'],
				'aleapp'					:	parsers['URLS']['aleapp'],
				'atola'						:	parsers['URLS']['atola'],
				'autopsy'					:	parsers['URLS']['autopsy'],
				'avml'						:	parsers['URLS']['avml'],
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
				'fresponse'					:	parsers['URLS']['fresponse'],
				'ftk'						:	parsers['URLS']['ftk'],
				'ftkimager'					:	parsers['URLS']['ftkimager'],
				'hashcat'					:	parsers['URLS']['hashcat'],
				'hstex'						:	parsers['URLS']['hstex'],
				'ileapp'					:	parsers['URLS']['ileapp'],
				'irec'						:	parsers['URLS']['irec'],
				'ive'						:	parsers['URLS']['ive'],
				'kali'						:	parsers['URLS']['kali'],
				'lime'						:	parsers['URLS']['lime'],
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
				'tzworks'					:	parsers['URLS']['tzworks'],
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
	
	return (requests.get(u, headers = ua_headers) for u in urls)

def run_cli():
	global response
	table_headers = ['Tool', 'Current Version', 'Latest Version', 'Update?']
	
	gather_used_tools('aim')
	gather_used_tools('aleapp')
	gather_used_tools('atola')
	gather_used_tools('autopsy')
	gather_used_tools('avml')
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
	gather_used_tools('fresponse')
	gather_used_tools('ftk')
	gather_used_tools('ftkimager')
	gather_used_tools('hashcat')
	gather_used_tools('hstex')
	gather_used_tools('ileapp')
	gather_used_tools('irec')
	gather_used_tools('ive')
	gather_used_tools('kali')
	gather_used_tools('lime')
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
	gather_used_tools('tzworks')
	gather_used_tools('ufed4pc')
	gather_used_tools('usbdetective')
	gather_used_tools('veracrypt')
	gather_used_tools('xamn')
	gather_used_tools('xways')
	
	console.show_activity()
	
	response = list(crawl())
	
	update_cli('aim', 'AIM', aim_parser)
	update_cli('aleapp', 'ALEAPP', aleapp_parser)
	update_cli('atola', 'Atola TaskForce', atola_parser)
	update_cli('autopsy', 'Autopsy', autopsy_parser)
	update_cli('avml', 'AVML', avml_parser)
	update_cli('axiom', 'AXIOM', axiom_parser)
	update_cli('bec', 'BEC', bec_parser)
	update_cli('blacklight', 'BlackLight', blacklight_parser)
	update_cli('caine', 'CAINE', caine_parser)
	update_cli('cyberchef', 'CyberChef', cyberchef_parser)
	update_cli('deft', 'DEFT', deft_parser)
	update_cli('eift', 'EIFT', eift_parser)
	update_cli('encase', 'Encase', encase_parser)
	update_cli('exiftool', 'ExifTool', exiftool_parser)
	update_cli('ez_amcacheparser', 'EZ AmcacheParser', ez_amcacheparser_parser)
	update_cli('ez_appcompatcacheparser', 'EZ AppCompatCacheParser', ez_appcompatcacheparser_parser)
	update_cli('ez_bstrings', 'EZ bstrings', ez_bstrings_parser)
	update_cli('ez_evtxex', 'EZ Evtx Explorer/EvtxECmd', ez_evtxex_parser)
	update_cli('ez_jlecmd', 'EZ JLECmd', ez_jlecmd_parser)
	update_cli('ez_jumplistex', 'EZ JumpList Explorer', ez_jumplistex_parser)
	update_cli('ez_lecmd', 'EZ LECmd', ez_lecmd_parser)
	update_cli('ez_mftecmd', 'EZ MFTECmd', ez_mftecmd_parser)
	update_cli('ez_mftexplorer', 'EZ MFTExplorer', ez_mftexplorer_parser)
	update_cli('ez_pecmd', 'EZ PECmd', ez_pecmd_parser)
	update_cli('ez_rbcmd', 'EZ RBCmd', ez_rbcmd_parser)
	update_cli('ez_recentfilecacheparser', 'EZ RecentFileCacheParser', ez_recentfilecacheparser_parser)
	update_cli('ez_registryex', 'EZ Registry Explorer/RECmd', ez_registryex_parser)
	update_cli('ez_sdbex', 'EZ SDB Explorer', ez_sdbex_parser)
	update_cli('ez_shellbagex', 'EZ ShellBags Explorer', ez_shellbagex_parser)
	update_cli('ez_timelineex', 'EZ Timeline Explorer', ez_timelineex_parser)
	update_cli('ez_vscmount', 'EZ VSCMount', ez_vscmount_parser)
	update_cli('ez_wxtcmd', 'EZ WxTCmd', ez_wxtcmd_parser)
	update_cli('fec', 'Forensic Email Collector', fec_parser)
	update_cli('forensicexplorer', 'Forensic Explorer', forensicexplorer_parser)
	update_cli('ffn', 'Forensic Falcon Neo', ffn_parser)
	update_cli('fresponse', 'F-Response', fresponse_parser)
	update_cli('ftk', 'FTK', ftk_parser)
	update_cli('ftkimager', 'FTK Imager', ftkimager_parser)
	update_cli('hashcat', 'hashcat', hashcat_parser)
	update_cli('hstex', 'HstEx', hstex_parser)
	update_cli('ileapp', 'iLEAPP', ileapp_parser)
	update_cli('irec', 'IREC', irec_parser)
	update_cli('ive', 'iVe', ive_parser)
	update_cli('kali', 'Kali', kali_parser)
	update_cli('lime', 'LiME', lime_parser)
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
	update_cli('tzworks', 'TZWorks', tzworks_parser)
	update_cli('ufed4pc', 'UFED 4PC', ufed4pc_parser)
	update_cli('usbdetective', 'USB Detective', usbdetective_parser)
	update_cli('veracrypt', 'VeraCrypt', veracrypt_parser)
	update_cli('xamn', 'XAMN', xamn_parser)
	update_cli('xways', 'X-Ways', xways_parser)
	
	update_urls = {
'xways' : 'http://www.x-ways.net/winhex/license.html',
'xamn' : 'https://www.msab.com/downloads/',
'veracrypt' : 'https://www.veracrypt.fr/en/Downloads.html',
'usbdetective' : 'https://usbdetective.com/release-notes/',
'ufed4pc' : 'https://www.cellebrite.com/en/support/product-releases/',
'tzworks' : 'https://tzworks.net/download_links.php',
'sleuthkit' : 'https://github.com/sleuthkit/sleuthkit/releases/latest',
'physicalanalyzer' : 'https://www.cellebrite.com/en/support/product-releases/',
'passware' : 'https://www.passware.com/kit-forensic/whatsnew/',
'paraben' : 'https://paraben.com/paraben-downloads/',
'oxygen' : 'http://www.oxygen-forensic.com/download/whatsnew/OFD/WhatsNew.html',
'osf' : 'https://www.osforensics.com/download.html',
'nsrl' : 'https://www.nist.gov/itl/ssd/software-quality-group/national-software-reference-library-nsrl/nsrl-download/current-rds',
'nirsoft' : 'https://launcher.nirsoft.net/downloads/index.html',
'netanalysis' : 'https://www.digital-detective.net/start/netanalysis-quick-start/',
'mountimagepro' : 'http://www.forensicexplorer.com/download.php',
'mobiledit' : 'https://www.mobiledit.com/downloads',
'macquisition' : 'https://www.blackbagtech.com/downloads/',
'lime' : 'https://github.com/504ensicsLabs/LiME/releases/latest',
'kape' : 'https://ericzimmerman.github.io/KapeDocs/#!Pages\\0.-Changelog.md',
'kali' : 'https://www.kali.org/downloads/',
'ive' : 'https://berla.co/customer-support/',
'irec' : 'https://binalyze.com/products/irec/release-notes/',
'ileapp' : 'https://github.com/abrignoni/iLEAPP',
'hstex' : 'https://www.digital-detective.net/start/hstex-quick-start/',
'hashcat' : 'https://hashcat.net/beta/',
'ftkimager' : 'https://accessdata.com/product-download',
'ftk' : 'https://accessdata.com/product-download',
'fresponse' : 'https://www.f-response.com/support/downloads',
'ffn' : 'https://www.logicube.com/knowledge/forensic-falcon-neo/',
'forensicexplorer' : 'http://www.forensicexplorer.com/download.php',
'fec' : 'http://www.metaspike.com/fec-change-log/',
'ez_wxtcmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_vscmount' : 'https://ericzimmerman.github.io/#!index.md',
'ez_timelineex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_shellbagex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_sdbex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_registryex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_recentfilecacheparser' : 'https://ericzimmerman.github.io/#!index.md',
'ez_rbcmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_pecmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_mftexplorer' : 'https://ericzimmerman.github.io/#!index.md',
'ez_mftecmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_lecmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_jumplistex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_jlecmd' : 'https://ericzimmerman.github.io/#!index.md',
'ez_evtxex' : 'https://ericzimmerman.github.io/#!index.md',
'ez_bstrings' : 'https://ericzimmerman.github.io/#!index.md',
'ez_appcompatcacheparser' : 'https://ericzimmerman.github.io/#!index.md',
'ez_amcacheparser' : 'https://ericzimmerman.github.io/#!index.md',
'exiftool' : 'https://owl.phy.queensu.ca/~phil/exiftool/',
'encase' : 'https://www.guidancesoftware.com/encase-forensic',
'eift' : 'https://www.elcomsoft.com/eift.html',
'deft' : 'http://na.mirror.garr.it/mirrors/deft/zero/',
'cyberchef' : 'https://github.com/gchq/CyberChef/releases/latest',
'caine' : 'https://www.caine-live.net/',
'blacklight' : 'https://www.blackbagtech.com/downloads/',
'bec' : 'https://belkasoft.com/get',
'axiom' : 'https://www.magnetforensics.com/downloadaxiom/',
'avml' : 'https://github.com/microsoft/avml/releases/latest',
'autopsy' : 'https://github.com/sleuthkit/autopsy/releases/latest',
'atola' : 'https://atola.com/products/taskforce/download.html',
'aleapp' : 'https://github.com/abrignoni/ALEAPP',
'aim' : 'https://arsenalrecon.com/downloads/'
}
	
	results = tabulate(table, headers = table_headers, disable_numparse = True)
	results_split = results.split('¿')
	
	for idx, result in enumerate(results_split):
		if (idx % 2 == 0):
			print(result, end = '')
		else:
			for key in update_urls.keys():
				if key == result:
					result = result.replace(key, update_urls[key])
			console.write_link('Update available!', result)
	
	### Forensic Version Checker
	try:
		soup = BeautifulSoup(response[0].text, 'html.parser')
		version = soup.find('div', {'class': 'release-header'}).select_one('a').text.strip()
		version = version.replace('v', '')
	except:
		version = '1.16'
	if (version == '1.16'):
		pass
	else:
		print('\n')
		console.write_link('FVC update available!', 'https://github.com/jankais3r/Forensic-Version-Checker/releases/latest')

table = []
run_cli()
console.hide_activity()
