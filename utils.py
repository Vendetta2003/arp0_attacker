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
    key  = get_gateway()[:10]
    for x in values:
        if(("dynamic" in x or "static" in x )and key in x ):
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
                if (f"{key}255" in a):
                    continue
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


#returns default gateway    
def get_gateway():
    c = None
    raw = subprocess.getoutput("ipconfig").split("\n")

    for line in raw:
        if(c==0):
            return(line.strip()) 
            c=None
        elif(("Default Gateway" in line and len(line)>39)):
            c=0


#pings all devices in network to get arp table
def ping_all():
    key  = get_gateway()[:10]
    def ping(key, ip_id): #key - 192.168.0.  , ip_id = 1
         k = subprocess.getoutput(f"ping {key}{ip_id}")
    threads = []
    for x in range (255):
        t = threading.Thread(target=ping , args=(str(key),str(x),))
        t.daemon = False
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    
