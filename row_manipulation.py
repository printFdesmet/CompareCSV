"""
    This Class focusses on reading in the rows and elimenating duplicate
    values from the server addresses.
    Currently there are 4 addresses provided to the server, this for the
    4 different applications. Now this has been resolved and the server needs
    only one address (the others are being resolved (DNS)).
    The only one that has to be preserved is the one with the .248 octet.
"""
import csv

import pandas as pd

from read_csv import ReadCSV as RCSV


class RowManipulation():
    data_list = []

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def show_duplicate_rows(self):
        """
            This method creates a dataframe from the given file, loops over
            it and if duplicates are found the shows the corresponding ones
            with their index.
        """
        # pd.set_option("display.max_rows", None, "display.max_columns", None)
        data = pd.read_csv(self.csv_file, encoding="ISO-8859-1", header=0)
        previous_value = 0
        index = 0
        rows_to_remove = []
        for column in data['#PORT_']:
            if previous_value == column:
                print(
                    f"\trow line: \033[1m \033[31m{index}\033[0m \033[30m with"
                    f" duplicate: \033[1m \033[31m{column}\033[0m \033[30m")
                rows_to_remove.append(index)

            index += 1
            previous_value = column
        if not rows_to_remove:
            return print("no rows to delete.")
        else:
            self.remove_duplicate_rows(data, rows_to_remove)
            self.write_new_csv()
            print(f"\n\033[92mDuplicate rows have been"
                  f"succesfully removed.\033[0m")

    def remove_duplicate_rows(self, dataframe, index_from_row):
        """
            This method converts the dataframe to a list and uses the provided
            indexes(in list form) to remove them from the list.
        """
        global data_list
        data_list = dataframe.values.tolist()
        for index in reversed(index_from_row):
            del data_list[index]

    def write_new_csv(self):
        """
            This method creates a csv file(if it doesn't exist) and writes the
            content of the global list with the headers included.
        """
        global data_list
        headers = RCSV.read_headers_from_csv(self, selected_csv=self.csv_file)
        with open('consist_info_final.csv', 'w', newline='') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerow(header for header in headers)
            writer.writerows(data_list)
