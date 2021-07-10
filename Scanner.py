#!/usr/bin/python3
import sys
import socket #Module to connect to the given IP and each port
from datetime import datetime    #Module to show scan time
print('/#*'* 50);


print ("IP Address format - xxx.xxx.xxx.xxx (1,2 and 3 digit octets can be entered in this field)");
print("Port Submission format - xx - xx");

print('/#*' * 50);      #Banner

IPAddress = input("Define the IP Address to scan = ");  #IP Address input field
port_range = input("Define the port range to scan = "); #Ports inpur field


IPAddress = socket.gethostbyname;    #If given a IPv6 Address,it will be converted to standard Iv4 type                                       

low_port = int(port_range.split('-') [0]);   #Start of input port array
high_port = int(port_range.split('-') [1]);  #End of input port array


print ("Scanning Host",IPAddress);                  #Scan message
print ("Scan Start" + str(datetime.now()));         #Provide time of current scan's start

try:
    for port in range(low_port,high_port):         #This loop will cycle through the input arra                                                   y of ports to scan
        s = socket.socket(socket.AF_INET , socket.SOCK_STREAM); #Connect to IP and one port at                                                                 a time.
        
#Socket = IP Address + Port
        status = s.connect_ex((IPAddress , port));
        if(status == 0):
            print ("Port No:" + str(port) + "open");
        else:
            print ("Port No:" + str(port) + "not open");
            s.close();  

except KeyboardInterrupt:
    print("Exiting program : Reason - User Interrupt");
    sys.exit();
except socket.gaierror:
    print("Hostname could not be resolved");
    sys.exit();
except socket.error:
    print("Could not connect to server");
    sys.exit();
