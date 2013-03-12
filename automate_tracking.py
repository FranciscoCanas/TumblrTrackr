import requests
import datetime
import subprocess
from requests.exceptions import ConnectionError

f=open('/h/u15/g1/00/g1canasf/CSC309/a2/csc309-a2/tracking_log', 'a')
try:
    r=requests.get('http://redwolf.cdf.toronto.edu:30945/ping')
except ConnectionError:
    r='Connection Error'
    f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
    f.close()
    # Above code duplicated because subprocess call never really comes back
    subprocess.call(['/h/u15/g1/00/g1canasf/CSC309/a2/csc309-a2/golive.sh'])

try:
    r=requests.get('http://redwolf.cdf.toronto.edu:30945/track?key=superdupersecrettrackingkey')
except ConnectionError:
    r='Connection Error'
    
f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
f.close()
