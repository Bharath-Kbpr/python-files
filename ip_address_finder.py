#python to display hostname and ip address

import socket
def get_host_name_ip():
    try:
        host_name=socket.gethostname()
        host_ip=socket.gethostbyname(host_name)
        print('HostName:',host_name)
        print('IP:',host_ip)
    except:
        print('unable to get hostname and ip')
get_host_name_ip()
