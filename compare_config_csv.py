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
from header_manipulation import HeaderManipulation

def main():
    """
        This function provides the arguments for the DifferentiateCSV class.
        After doing so calls the method that triggers the proces.
    """
    rcsv = DifferentiateCSV("consist_info.csv",
                            "consist_info2.csv")
    
    rcsv.genereate_header_files()


if __name__ == "__main__":
    main()
