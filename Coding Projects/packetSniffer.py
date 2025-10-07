#This program requires scapy installed (you can do so via pip)
#Winpcap is required if on a Windows computer

#Imports scapy and specific classes from it
from scapy.all import sniff
from scapy.layers.inet import IP, TCP, UDP, ICMP

#Checks to see if a packet has an IP layer and a protocol that is either ICMP, TCP, or UDP
#If it does, the function will print the protocol, source IP, and destination IP
def packetAnalysis(packet):
    #The function only works if the packet has an IP header
    if IP in packet:
        #Stores the protocol number, source IP, and destination IP
        protocol = packet[IP].proto
        source = protocol.src
        destination = protocol.dst

        #Determines the protocol being used and stores it in protocolName
        allProtocols = {
            1 : "ICMP",
            6 : "TCP",
            17: "UDP"
        }
        protocolName = allProtocols.get(protocol, lambda : "Unknown Protocol")

        #Prints the info about the packet
        print("Protocol: " + protocolName)
        print("Source IP: " + source)
        print("Destination IP: " + destination)
        print("--------------------------------------------------------------")

#Sniffs for IP packets 5 times
sniff(prn = packetAnalysis, count = 5, filter = "IP", store = 0)