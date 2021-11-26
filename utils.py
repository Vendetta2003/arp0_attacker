import subprocess
#import time
import socket 
import threading
#need to run ping scan 1st  - need to make a module for it
#need to do code cleanup
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
            #print(ip)
            #mac = a[26:43].strip()
            c+=1
            try:
                h_name = socket.gethostbyaddr(ip)[0]
                #print(mac)
                #print(h_name)
                #time.sleep(1)
                a+=f"   {h_name}"
                print(a)
                #print(ip,mac,h_name)
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
                #pass
    return s_values
    #print(s_values)
    
#print(get_mac())
#0-> 192.168.0.1           f0:b4:d2:de:97:6a     dynamic

def get_mymac():
    out = subprocess.getoutput("ipconfig")

def get_ip(a):
    return  a[a.index(">")+1:17].strip()
def get_mac(a):
    return a[26:43].strip()

def ping_all():
    def ping(ip_id):
         k = subprocess.getoutput(f"ping 192.168.0.{ip_id}")
         #print(k)
    threads = []
    for x in range (255):
        t = threading.Thread(target=ping , args=(str(x),))
        t.daemon = False
        threads.append(t)
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()
    

#print(get_mac("0-> 192.168.0.1           f0:b4:d2:de:97:6a     dynamic"))
#ping_all()