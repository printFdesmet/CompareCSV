"""
        This class converts given MAC-addresses to their corresponding
        IP-addresses.
"""

import re
import socket
import sys


class MacToIP():
    def __init__(self, multicast_list):
        self.multicast_list = multicast_list

    def convert_multicast_ip_to_mac(self):
        """
            Convert the Multicast IP to it's equivalent Multicast MAC.
        """


    def verify_ip(self, mcast_ip):

        """

        This function takes a multicast IP(string) as an argument

        and returns True if IP address is correct

        """

        if len(mcast_ip) < 9 or len(mcast_ip) > 15:

            print("Multicast IP address length is incorrect !")

            return False

        octets = mcast_ip.split(',')

        if len(octets) < 4:

            print("Incorrect number of octets in multicast IP address !")

            return False

        for idx in range(0, 4):

            if not(self.verify_octet(octets[idx])):

                print("One of the octets is incorrect !")

                return False

        # Check if first octet is from mcast range

        if int(octets[0]) < 224 or int(octets[0]) > 239:

            print("First octet isn’t from multicast range ! Should be 224 … 239 !")

            return False

        return True


    def verify_octet(self, octet):

        """

        This function returns True if string parameter ‘octet’ is a number in the range 0…255

        """

        if octet.isdigit:

            octet_num = int(octet)

            if octet_num >= 0 and octet_num <= 255:

                return True

        return False


    def ip2mac(self, mcast_ip):

        """

        Function ip2mac takes multicast IP address as an argument and returns multicast MAC address

        """

        if not(self.verify_ip(mcast_ip)):

            print("Parameter provided is not a valid multicast IP ! Should be 224.0.0.1 … 239.255.255.255")

            sys.exit(0)

        mcast_mac = '01: 00: 5e: '

        octets = mcast_ip.split('.')

        second_oct = int(octets[1]) & 127

        third_oct = int(octets[2])

        fourth_oct = int(octets[3])

        mcast_mac = mcast_mac + format(second_oct, '02x') + ': ' + format(third_oct, '02x') + ': ' + format(fourth_oct, '02x')

        return mcast_mac
