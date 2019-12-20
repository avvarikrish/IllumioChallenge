import csv
from rule import Rule


class Firewall:

    directions = ['inbound', 'outbound']
    protocols = ['tcp', 'udp']

    def __init__(self, path_to_csv):
        self._rules = dict()
        # initialize main structure
        for direction in self.directions:
            self._rules[direction] = {}
            for protocol in self.protocols:
                self._rules[direction][protocol] = []
        self._read_csv_input(path_to_csv)

# private

    def _read_csv_input(self, path_to_csv):
        with open(path_to_csv) as csv_file:
            reader = csv.reader(csv_file)
            # loop through all lines of file
            for rule in reader:
                # store each rule object in the specified direction and protocol list
                current_rule = Rule(rule[0], rule[1], rule[2], rule[3])
                self._rules[rule[0]][rule[1]].append(current_rule)

# public

    def accept_packet(self, direction, protocol, port, ip_address):
        try:
            # loop through all the rules within specified direction and protocol
            for rule in self._rules[direction][protocol]:
                # check for matches of port and ip
                if rule.port().in_range(port) and rule.ip().in_range(ip_address):
                    return True
            return False
        except KeyError:
            raise Exception('Invalid argument. Direction or protocol does not exist')
