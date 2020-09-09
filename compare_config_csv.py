"""
    This script compares the CAF provided CSV with another version.
    The purpose for this action is the creation of the new config generation
    script.
"""

from read_csv import DifferentiateCSV
from row_manipulation import RowManipulation


def main():
    """
        This function provides the arguments for the DifferentiateCSV class.
        After doing so calls the method that triggers the proces.
    """
    print()
    print("\033[4mOverview of all the unique headers:\033[0m")
    print()

    rcsv = DifferentiateCSV("consist_info.csv", "consist_info2.csv")
    rcsv.genereate_header_files()

    print("\n==============================================================\n")
    print("\033[4mOverview of the duplicate ports with their index:\033[0m")
    print()

    row_m = RowManipulation("consist_info.csv")
    row_m.show_duplicate_rows()

    print(f"\n\033[92mDuplicate rows have been succesfully removed.\033[0m")
    print(f"The new file is generated: \033[4mconsist_info_final.csv\033[0m")


if __name__ == "__main__":
    main()
