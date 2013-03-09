import requests
import datetime
from requests.exceptions import ConnectionError

f=open('/h/u15/g1/00/g1canasf/CSC309/csc309-a2/tracking_log', 'a')
try:
    r=requests.get('http://127.0.0.1:30945/track')
except ConnectionError:
    r='Connection Error'
    
f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
f.close()
