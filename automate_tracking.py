import requests
import datetime
from requests.exceptions import ConnectionError

f=open('tracking_log', 'a')
try:
    r=requests.get('http://127.0.0.1:30945/track')
except ConnectionError:
    r='Connection Error'
    
f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
f.close()
