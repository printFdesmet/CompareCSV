"""
    This script compares the CAF provided CSV with another version.
    The purpose for this action is the creation of the new config generation
    script.
    TODO: Compare the Column names from both CSV files. DONE
    TODO: Filter only the necessary Colums. DONE
    TODO: Check the port row for duplicate vaulues.
            IF found remove the all EXCLUSIVE the original one.
"""

from read_csv import DifferentiateCSV
from row_manipulation import RowManipulation


def main():
    """
        This function provides the arguments for the DifferentiateCSV class.
        After doing so calls the method that triggers the proces.
    """
    print("\033[4moverview of all the unique headers.\033[0m")
    rcsv = DifferentiateCSV("consist_info.csv", "consist_info2.csv")
    rcsv.genereate_header_files()
    print("==================================================================")
    print("\033[4mOverview of all the duplicate ports and their index.\033[0m")
    row_m = RowManipulation("consist_info.csv")
    row_m.show_duplicate_rows()

if __name__ == "__main__":
    main()
