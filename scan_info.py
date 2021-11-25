import subprocess
import time 
def get_mac():
    print("[+] Fetching list in IP , MAC , TYPE sequence...\n")
    val = subprocess.getoutput("arp -a")
    values = str(val).split("\n")[3:]

    for x in values:
        if(("dynamic" in x or "static" in x )and "192.168" in x ):
            time.sleep(1)
            print(x.replace("-",":"))
            print("-------------------------------------------------------")
#get_mac()

def get_mymac():
    out = subprocess.getoutput("ipconfig")