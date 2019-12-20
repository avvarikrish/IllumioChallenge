class Ip:

    def __init__(self, ip):
        self._ip = ip
        self._lower_bound = ''
        self._upper_bound = ''
        self._lower_bound_int = 0
        self._upper_bound_int = 0
        if '-' in ip:
            address_range = ip.split('-')
            self._lower_bound = address_range[0]
            self._lower_bound_int = self._convert_to_int(address_range[0])
            self._upper_bound = address_range[1]
            self._upper_bound_int = self._convert_to_int(address_range[1])
        else:
            self._lower_bound = self._upper_bound = ip
            self._lower_bound_int = self._upper_bound_int = self._convert_to_int(ip)

# private

    # pulled from stackoverflow
    def _convert_to_int(self, ip_value):
        octets = ip_value.split('.')
        int_value = (16777216 * int(octets[0])) + (65536 * int(octets[1])) + (256 * int(octets[2])) + int(octets[3])
        return int_value

# public

    def ip_value(self):
        return self._ip

    def lower_bound(self):
        return self._lower_bound

    def upper_bound(self):
        return self._upper_bound

    def in_range(self, ip_to_check):
        ip_to_check_int = self._convert_to_int(ip_to_check)
        return (ip_to_check_int >= self._lower_bound_int) and (ip_to_check_int <= self._upper_bound_int)
