CN PRACTICAL CODES - TY B.Tech Computer Engineering, Sem V

HOW TO RUN
  Ubuntu :  python3 P2-Hamming.py
  Windows:  python P2-Hamming.py
  (cd into this folder first)

FILES
  P2-Hamming.py                      Hamming code - general, any number of data bits
  P3-SlidingWindow-LongVersion.py    USE THIS ONE - lost frame per window, shows
                                     "going back" and receiver discarding/buffering
  P4-DistanceVector.py               Distance vector routing (Bellman-Ford)
  P5-Commands.txt                    Topologies + VLAN - Packet Tracer commands
  P6-Commands.txt                    Static / RIP / OSPF - Packet Tracer commands
  P7-LeakyBucket.py                  Leaky bucket congestion control
  P8-TCP-Server.py / P8-TCP-Client.py    run SERVER first, client in a 2nd terminal
  P8-UDP-Server.py / P8-UDP-Client.py    run SERVER first, client in a 2nd terminal
  P9-Wireshark-Steps.txt             Wireshark steps + filters
  P9-PacketAnalysis.py               optional, needs scapy + wired_network.pcap

ALTERNATE VERSIONS (use only if asked)
  P2-Hamming-ShortVersion.py         fixed Hamming (7,4), 4 data bits only
  P3-SlidingWindow.py                short version, one lost frame for whole run

CODE LINE COUNTS (comments and blanks excluded)
  P7 = 34    P8 = 36 total    P9 = 46    P3 long = 60    P4 = 60    P2 = 61

NOTES
  P3: press 3 at the menu to exit cleanly.
  P8: if you get "Address already in use", wait a minute or change the port number.
  P6: OSPF wildcard mask is the INVERSE of the subnet mask (/24 -> 0.0.0.255).
  Python uses INDENTATION as syntax - 4 spaces per level, never mix tabs and spaces.
