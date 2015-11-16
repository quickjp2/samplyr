import json, requests, os, atexit

def sendP1G():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'1', 'P1R':'0',
               'P2G':'0', 'P2R':'0',
               'P3G':'0', 'P3R':'0',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
    
def sendP1R():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'1',
               'P2G':'0', 'P2R':'0',
               'P3G':'0', 'P3R':'0',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP2G():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'1', 'P2R':'0',
               'P3G':'0', 'P3R':'0',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP2R():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'0', 'P2R':'1',
               'P3G':'0', 'P3R':'0',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP3G():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'0', 'P2R':'0',
               'P3G':'1', 'P3R':'0',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP3R():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'0', 'P2R':'0',
               'P3G':'0', 'P3R':'1',
               'P4G':'0', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP4G():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'0', 'P2R':'0',
               'P3G':'0', 'P3R':'0',
               'P4G':'1', 'P4R':'0'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
  
def sendP4R():
    url = os.environ['GOOGLE-SHEET-URL']
    payload = {'P1G':'0', 'P1R':'0',
               'P2G':'0', 'P2R':'0',
               'P3G':'0', 'P3R':'0',
               'P4G':'0', 'P4R':'1'}
    headers = {'Content-Type': 'application/x-www-form-urlencoded'}
    r = requests.post(url, headers=headers, params=payload, verify=False)
