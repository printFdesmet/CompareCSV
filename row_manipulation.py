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
'''
    TODO: Select the correct column. (PORT)
    TODO: Loop over the rows and print out duplicates with the same port number
    TODO: Remove the duplicates, keep original (address, 248)
    TODO: Create new CSV file with the unique rows. (check if only 3 rows less)
'''


class RowManipulation():
    data_list = []

    def __init__(self, csv_file):
        self.csv_file = csv_file

    def show_duplicate_rows(self):
        # pd.set_option("display.max_rows", None, "display.max_columns", None)
        data = pd.read_csv(self.csv_file)
        previous_value = 0
        index = 0
        rows_to_remove = []
        for column in data['#PORT_']:
            if previous_value == column:
                print(
                    f"\trow line: \033[1m \033[31m{index}\033[0m \033[30m with"
                    f"duplicate: \033[1m \033[31m{column}\033[0m \033[30m")
                rows_to_remove.append(index)

            index += 1
            previous_value = column

            
        self.remove_duplicate_rows(data, rows_to_remove)
        self.write_new_csv()

    def remove_duplicate_rows(self, dataframe, index_from_row):
        global data_list 
        data_list = dataframe.values.tolist()
        for index in reversed(index_from_row):
            print(f"removing the following row:\n{data_list[index]}")
            del data_list[index]

    
    def write_new_csv(self):
        global data_list
        with open('excluded_rows.csv', 'w') as writer_file:
            writer = csv.writer(writer_file)
            writer.writerows(data_list)

