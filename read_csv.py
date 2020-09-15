"""
    This class reads in both CSV files, compares the two of them and
    returns its unique values.
"""


import csv

from header_manipulation import HeaderManipulation


class ReadCSV():
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

    def read_headers_from_csv(self, selected_csv):
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
