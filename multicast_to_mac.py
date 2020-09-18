"""
        This class converts given MAC-addresses to their corresponding
        IP-addresses.
"""

import sys

from read_csv import ReadCSV as rcsv


class MulticastIPToMAC:
    def __init__(self, multicast_list):
        self.multicast = multicast_list

    def verify_ip(self, multicast_ip):
        """

        This function takes a multicast IP(string) as an argument

        and returns True if IP address is correct

        """

        if len(multicast_ip) < 9 or len(multicast_ip) > 15:
            print("Multicast IP address length is incorrect !")

            return False

        octets = multicast_ip.split('.')

        if len(octets) < 4:
            print("Incorrect number of octets in multicast IP address !")

            return False

        for idx in range(0, 4):

            if not (self.verify_octet(octets[idx])):
                print("One of the octets is incorrect !")

                return False

        # Check if first octet is from multicast range

        if int(octets[0]) < 224 or int(octets[0]) > 239:
            print(f"First octet isn’t from multicast range !"
                  f"Should be 224 … 239 !")

            return False

        return True

    @staticmethod
    def verify_octet(octet):

        """

        This function returns True if string parameter ‘octet’
        is a number in the range 0…255

        """

        if octet.isdigit:

            octet_num = int(octet)

            if 0 <= octet_num <= 255:
                return True

        return False

    def ip2mac(self):

        """

        Function ip2mac takes multicast IP address as an argument
        and returns multicast MAC address

        """
        multicasts = rcsv.read_multicast_addresses_from_csv(self.multicast)
        mac_list = []

        for multicast in multicasts:
            if not (self.verify_ip(multicast)):
                print(f"Parameter provided is not a valid multicast IP !"
                      f"Should be 224.0.0.1 … 239.255.255.255")

            multicast_to_mac = '01-00-5e-'
            octets = multicast.split('.')
            second_oct = int(octets[1]) & 127
            third_oct = int(octets[2])
            fourth_oct = int(octets[3])

            multicast_to_mac = (f"{multicast_to_mac}{format(second_oct, '02x')}-"
                                f"{format(third_oct, '02x')}-"
                                f"{format(fourth_oct, '02x')}")
            mac_list.append(multicast_to_mac)

        return mac_list
