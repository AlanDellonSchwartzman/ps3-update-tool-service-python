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
  response.encoding = 'UTF-8'

  if (response.status_code == 404):
    return {'error': 'Game not found'}

  if not (response.content):
    return {'title': '', 'updates': []}
  
  dictionary = xmltodict.parse(response.text)

  packages = dictionary['titlepatch']['tag']['package']

  if (type(packages) == list):
    title = dictionary['titlepatch']['tag']['package'][-1]['paramsfo']['TITLE']
    return {'title': title, 'updates': list(map(getUpdate, packages))}
  elif (isinstance(packages, dict)):
    title = dictionary['titlepatch']['tag']['package']['paramsfo']['TITLE']
    print('TITLE: ', title)
    return {'title': title, 'updates': [getUpdate(packages)]}
  else:
    return {'title': '', 'updates': [], 'error': 'error'}
