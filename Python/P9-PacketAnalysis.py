from scapy.all import rdpcap, Ether, IP, TCP, UDP

# Read captured packets
packets = rdpcap("wired_network.pcap")

print("=" * 70)
print(" WIRED NETWORK PACKET FORMAT ANALYSIS")
print("=" * 70)

for i, packet in enumerate(packets, start=1):
    print("\nPacket No.:", i)
    print("-" * 70)

    # Ethernet Header
    if packet.haslayer(Ether):
        eth = packet[Ether]
        print("\n[ Ethernet Header ]")
        print("Source MAC Address      :", eth.src)
        print("Destination MAC Address :", eth.dst)
        print("EtherType               :", hex(eth.type))
        print("Frame Length            :", len(packet))

    # IP Header
    if packet.haslayer(IP):
        ip = packet[IP]
        print("\n[ IP Header ]")
        print("Version                 :", ip.version)
        print("Header Length           :", ip.ihl * 4, "bytes")
        print("Type of Service         :", ip.tos)
        print("Total Length            :", ip.len)
        print("Identification          :", ip.id)
        print("TTL                     :", ip.ttl)
        print("Protocol                :", ip.proto)
        print("Source IP Address       :", ip.src)
        print("Destination IP Address  :", ip.dst)

    # TCP Header
    if packet.haslayer(TCP):
        tcp = packet[TCP]
        print("\n[ TCP Header ]")
        print("Source Port             :", tcp.sport)
        print("Destination Port        :", tcp.dport)
        print("Sequence Number         :", tcp.seq)
        print("Acknowledgement Number  :", tcp.ack)
        print("Header Length           :", tcp.dataofs * 4, "bytes")
        print("Flags                   :", tcp.flags)
        print("Window Size             :", tcp.window)
        print("Checksum                :", tcp.chksum)

    # UDP Header
    elif packet.haslayer(UDP):
        udp = packet[UDP]
        print("\n[ UDP Header ]")
        print("Source Port             :", udp.sport)
        print("Destination Port        :", udp.dport)
        print("Length                  :", udp.len)
        print("Checksum                :", udp.chksum)

    print("-" * 70)
