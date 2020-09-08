"""
    This class reads in both CSV files, compares the two of them and
    returns its unique values.
"""


import csv

from header_manipulation import HeaderManipulation

class DifferentiateCSV():
    def __init__(self, first_csv, second_csv):
        self.first_csv = first_csv
        self.second_csv = second_csv

    def genereate_header_files (self):
        """
            This method calls the read_csv method, then appends the output
            as arguments for the class instantiation. Finally calls the method
            to trigger the header class.
        """
        first_file = self.read_csv(self.first_csv)
        second_file = self.read_csv(self.second_csv)

        header_m = HeaderManipulation(first_file, second_file)

        return header_m.get_unique_headers()

    def read_csv(self, selected_csv):
        """
            This method reads in the provided CSV and extracts the headers.
        """
        try:
            with open(selected_csv, 'r') as open_csv_file:
                reader = csv.reader(open_csv_file)
                headers = next(reader, None)
        except FileNotFoundError as no_file:
            print(f"Could not found {no_file}.")

        return headers
    
