import requests
import datetime
import subprocess
from requests.exceptions import ConnectionError

f=open('/h/u15/g1/00/g1canasf/CSC309/csc309-a2/monitor_log', 'a')
try:
    r=requests.get('http://127.0.0.1:30945/ping')
except ConnectionError:
    r='Connection Error'
    f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
    f.close()
    # Above code duplicated because subprocess call never really comes back
    subprocess.call(['/h/u15/g1/00/g1canasf/CSC309/csc309-a2/trackr/start.sh'])
        
    
f.write(str(datetime.datetime.now()) + ':' + str(r) + '\n')
f.close()
