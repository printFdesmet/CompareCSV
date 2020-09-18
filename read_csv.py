"""
    This class reads in both CSV files, compares the two of them and
    returns its unique values.
"""

import csv

import pandas as pd

from header_manipulation import HeaderManipulation


class ReadCSV:
    def __init__(self, first_csv, second_csv):
        self.first_csv = first_csv
        self.second_csv = second_csv

    def show_unique_headers(self):
        """
            This method calls the read_headers_from_csv method, then appends
            the output as arguments for the class instantiation.
            Finally calls the method to trigger the header class.
        """
        first_file = self.read_headers_from_csv(self.first_csv)
        second_file = self.read_headers_from_csv(self.second_csv)

        header_m = HeaderManipulation(first_file, second_file)

        return header_m.get_unique_headers()

    @staticmethod
    def read_headers_from_csv(selected_csv):
        """
            This method reads in the provided CSV and extracts the headers.
        """
        try:
            with open(selected_csv, 'r') as open_csv_file:
                reader = csv.reader(open_csv_file)
                headers = next(reader, None)
                return headers
        except FileNotFoundError as no_file:
            print(f"Could not found {no_file}.")

    @staticmethod
    def read_multicast_addresses_from_csv(selected_csv):
        """This method creates a list of multicast addresses from the csv.
        """

        multicast_list = []
        data = pd.read_csv(selected_csv, encoding="ISO-8859-1", header=0)

        for item in data["STATICMULTICAST"]:
            multicast_list.append(item)

        stringed_list = str(multicast_list)
        final_list = stringed_list.split(',')
        return print(final_list)
