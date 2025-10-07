#Imports sys and socket for port scanning
#Imports datetime so that the program can display when the scan began and ended
import sys
import socket
from datetime import datetime

#Collects the target IP address and the range of ports that will be scanned
target = str(input("Enter your target IP address (IPv4): "))
lowPort = int(input("Enter the low end of the range of ports you wish to scan: "))
highPort = int(input("Enter the high end of the range of ports you wish to scan: "))

#Tells the user what IP address is being scanned and when the scan began
print("----------------------------------------------------------------")
print("Scanning " + target)
print("Scanning started at " + str(datetime.now()))
print("----------------------------------------------------------------")

#Opens a file full of names of common ports that will be used to display information about ports found during the scan
#commonPortsOG contains the raw lines of information, while commonPorts divides them to make port information easier to access
commonPortsFile = open("Sources/commonPorts.txt","r")
commonPortsOG = commonPortsFile.read().splitlines()
commonPorts = []
for bigLine in commonPortsOG:
      for item in bigLine.split(":::"):
            commonPorts.append(item)

#Tries to scan through different ports
#Throws exception if a keyboard interrupt happens or if an error occurs
try:
    #Keeps track of the number of open ports found so it can print "No ports found" if no ports were found
    portCount = 0
    print("Open ports: ")

    #Scans between the lowPort and highPort as defined by the user
    for port in range(lowPort, highPort):
        #Creates the currentSocket using IPv4 and the TCP protocol
        currentSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        
        #Attempts to connect to the socket, and if successful, prints the open port information and increases portCount by 1
        #If the open port is in commonPorts, more the protocol and name of the port will be displayed, otherwise it will output "Unknown" under the extra categories
        result = currentSocket.connect_ex((target, port))
        if result ==0:
            if(commonPorts.index(str(port)) != -1):
                  curIndex = commonPorts.index(str(port))
                  print("Port: " + str(port) + " | Protocol: " + commonPorts[curIndex + 1] + " | Name: " + commonPorts[curIndex + 2])
            else:
                  print("Port: " + str(port) + " | Protocol: Unknown | Name: Unknown")
            portCount += 1

        #Closes the currentSocket
        currentSocket.close()

    #Tells the user that no ports were found
    if(portCount == 0):
          print("No ports found")
    
    #Tells the user when the scanning was completed
    print("----------------------------------------------------------------")
    print("Scanning completed at " + str(datetime.now()))

#Ends the port scan if a keyboard interrupt occurs
except KeyboardInterrupt:
        print("Ending port scan...")
        sys.exit()

#Catches socket errors
except socket.error:
        print("A socket error has occurred")
        sys.exit()