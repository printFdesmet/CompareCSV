"""
TODO: write method to generate second octet. DONE
TODO: write method to generate third octet.DONE
TODO: write method to combine all the octets together to create the
      unique IP. DONE
TODO: Write the IP's with the correct port towards the config file.
IMPORTANT: For the second octet only 7 bits are being used, from which the
           the first 3 are for the vehicle type and the following 4 for
           the VLAN ID.
VLAN ID     |Vehicle type
X.64.32.16.8|.4.2.1
------------------
8.7 .6 .5 .4|.3.2.1

VLANs in use: 2, 7, 9, 10, 12
Vehicle types: 1, 6, 7
"""


class GenerateIPForStadler:
    """
    A Class to generate the second and third octet of an IP using
    a combination of the VLAN ID and vehicle type for the second and the car
    number for the third one.
    """

    def __init__(self, car_number, ip, vehicle_type, vlan_id):
        self.car_number = car_number
        self.ip = ip
        self.vehicle_type = vehicle_type
        self.vlan_id = vlan_id

    def generate_second_octet(self):
        """
        This method takes the VLAN ID and the vehicle type to generate the
        correct byte.
        """

        vlan_to_ip = {
            "vlan 2": "16",
            "vlan 7": "56",
            "vlan 9": "72",
            "vlan 10": "80",
            "vlan 12": "96",
        }

        vehicle_type_to_ip = {
            "lot 1b": "1",  # Vehicle name: DMU4
            "lot 4a": "6",  # Vehicle name: BMU-B3
            "lot 4b": "7",  # Vehicle name: BMU-B4
        }

        vehicle_ip = vehicle_type_to_ip.get(self.vehicle_type)
        vlan_ip = vlan_to_ip.get(self.vlan_id)

        second_octet = int(vehicle_ip) + int(vlan_ip)

        return str(second_octet)

    def generate_third_octet(self):
        """
        This method takes the car number and creates the third octet.
        """

        return self.car_number

    def generate_unique_ip(self):
        """
        This method takes the original IP template (without the second and
        third octet) and fills those empty values with the generated octets
        from the above methods.
        """

        second_octet = self.generate_second_octet()
        third_octet = self.generate_third_octet()

        altered_ip_with_octets =\
            self.ip.replace("x", second_octet).replace("y", third_octet)

        return altered_ip_with_octets


if __name__ == '__main__':
    GIS = GenerateIPForStadler('3', '10.x.y.3', 'lot 4a', 'vlan 12')
    print(GIS.generate_unique_ip())
