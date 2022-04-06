import requests, xmltodict, json
from fastapi import HTTPException

def getUpdate(package):
  return {
    'version': package['@version'],
    'url': package['@url'],
    'size': package['@size']
  }

def main(serial):
  url = f'https://a0.ww.np.dl.playstation.net/tpl/np/{serial}/{serial}-ver.xml'

  response = requests.get(url, verify=False)

  if (response.status_code == 404): 
    return {'error': 'not found'}
    
  dictionary = xmltodict.parse(response.text)

  return list(map(getUpdate, dictionary['titlepatch']['tag']['package']))
