class Port:

    def __init__(self, port):
        self._port = port
        self._lower_bound_int = 0
        self._upper_bound_int = 0
        if '-' in port:
            port_range = port.split('-')
            self._lower_bound_int = int(port_range[0])
            self._upper_bound_int = int(port_range[1])
        else:
            self._lower_bound_int = self._upper_bound_int = int(port)

    def port_value(self):
        return self._port

    def lower_bound(self):
        return self._lower_bound_int

    def upper_bound(self):
        return self._upper_bound_int

    def in_range(self, port_to_check):
        return (port_to_check >= self._lower_bound_int) and (port_to_check <= self._upper_bound_int)
