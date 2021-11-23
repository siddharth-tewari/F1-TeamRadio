import urllib.request as request
import json
import requests
from jsonstream import load
from io import StringIO
import logging

def list():
    print("Driver List")
    with request.urlopen('http://livetiming.formula1.com/static/SessionInfo.json') as response:
        if response.getcode() == 200:
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info('Getting the URL')
                source = response.read()
                data = json.loads(source)
                location = "http://livetiming.formula1.com/static/" + data['Path'] + "DriverList.json"
                logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
                logging.info('URL Successfully Found')
                url = location
                print(url)
                r = requests.get(location)
                r.encoding = 'utf-8-sig'
                out = json.loads(r.text)
                print(json.dumps(out, indent = 4))
                output = json.dumps(out, indent = 4)
                
        else:
            print('Unknown Error Occured')

list()





