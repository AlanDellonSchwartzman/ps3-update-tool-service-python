import requests, xmltodict

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
    return {'error': 'Game not found'}

  if not (response.content):
    return ()
  
  dictionary = xmltodict.parse(response.text)
  packages = dictionary['titlepatch']['tag']['package']

  if (type(packages) == list):
    return list(map(getUpdate, packages))
  elif (len(packages) == 6):
    return [getUpdate(packages)]
  else:
    return {'error': 'error'}
