import subprocess
import socket 
import threading

def get_info():
    print("[+] Fetching list in IP , MAC , TYPE , HOST NAME sequence...This will take a while\n")
    ping_all()
    val = subprocess.getoutput("arp -a")
    values = str(val).split("\n")[3:]
    s_values = []
    c = 0
    for x in values:
        if(("dynamic" in x or "static" in x )and "192.168" in x ):
            a = str(c)+"-> "+(x.replace("-",":").strip())
            ip = a[a.index(">")+1:17].strip()
            
            c+=1
            try:
                h_name = socket.gethostbyaddr(ip)[0]
                
                a+=f"   {h_name}"
                print(a)
                
                s_values.append(a)
                print("---------------------------------------------------------------------------")
            except Exception as e :
                if ("192.168.0.255" in a):
                    pass
                else:
                    a+=f"   HostNameNotAvilable"
                    print(a)
                    print("---------------------------------------------------------------------------")
                    s_values.append(a)
                
    return s_values
    


def get_mymac():#need to work on it
    out = subprocess.getoutput("ipconfig")

#accepts string from list of ip , mac , hostname sequence
def get_ip(a):
    return  a[a.index(">")+1:17].strip()
def get_mac(a):
    return a[26:43].strip()

#pings all devices in network to get arp table
def ping_all():
    def ping(ip_id):
         k = subprocess.getoutput(f"ping 192.168.0.{ip_id}")
    threads = []
    for x in range (255):
        t = threading.Thread(target=ping , args=(str(x),))
        t.daemon = False
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
