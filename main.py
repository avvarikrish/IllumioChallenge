# testing/executable file

from firewall import Firewall
import time

FILE_PATH = 'rules.csv'

x = time.time()
fw = Firewall(FILE_PATH)
print(time.time()-x)
print(fw.accept_packet("inbound", "tcp", 80, "192.168.1.2")) # matches first rule
print(fw.accept_packet("inbound", "udp", 53, "192.168.2.1")) # matches third rule
print(fw.accept_packet("outbound", "tcp", 10234, "192.168.10.11"))  # matches second rule
print(fw.accept_packet("inbound", "tcp", 81, "192.168.1.2"))
print(fw.accept_packet("inbound", "udp", 24, "52.12.48.92"))
print(fw.accept_packet("outbound", "tcp", 550, "192.229.0.0"))
print(fw.accept_packet("inbound", "tcp", 1000, "10.89.228.24"))
print(fw.accept_packet("inbound", "udp", 65535, "255.255.255.255"))
print(time.time()-x)
