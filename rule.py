from ip import Ip
from port import Port


class Rule:

    def __init__(self, direction, protocol, port, ip):
        self._direction = direction
        self._protocol = protocol
        self._port = Port(port)
        self._ip = Ip(ip)

    def direction(self):
        return self._direction

    def protocol(self):
        return self._protocol

    def port(self):
        return self._port

    def ip(self):
        return self._ip
