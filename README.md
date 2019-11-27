# Forensic Version Checker
Script that checks for available updates for the most commonly used Digital Forensics tools.

![FVC screenshot](https://github.com/jankais3r/Forensic-Version-Checker/blob/master/screen.png)


![CLI interface](https://github.com/jankais3r/Forensic-Version-Checker/blob/master/cli.png)

## Supported tools
- Arsenal Image Mounter
- Atola TaskForce
- Autopsy
- AXIOM
- Belkasoft Evidence Center
- BlackLight
- CAINE
- CyberChef
- DEFT
- EnCase
- ExifTool
- Forensic Email Collector
- Forensic Explorer
- Forensic Falcon Neo
- FTK
- FTK Imager
- hashcat
- HstEx
- MacQuisition
- Mount Image Pro
- NetAnalysis
- NSRL hash list
- OSForensics
- Paraben E3
- Passware
- Physical Analyzer
- The Sleuth Kit
- UFED 4PC
- USB Detective
- VeraCrypt
- XAMN
- X-Ways

If your favorite tool is missing, feel free to open an Issue and provide me with a link to that tool's website.

## Dependencies
```
pip3 install tabulate
pip3 install grequests
pip3 install beautifulsoup4
```

## Tested with Python 3.7 under
- Windows 10
- Ubuntu WSL (requires X server, e.g. Xming)
