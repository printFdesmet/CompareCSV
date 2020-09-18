""" This class manipulates the given headers, compares them, and returns a list
    of the unique headers if it applies.
"""

from collections import Counter
from ordered_set import OrderedSet


class HeaderManipulation:

    def __init__(self, first_headers, second_headers):
        self.first_headers = first_headers
        self.second_headers = second_headers

    @staticmethod
    def count_occurrence(to_compare_headers):
        """
            This method counts the amount off occurrence inside the provided
            list.
        """
        headers_occurrence = Counter(to_compare_headers).values()

        return list(headers_occurrence)

    @staticmethod
    def create_single_contingency(first_headers, second_headers):
        """
            This method takes a list of headers and removes the
            multiple values from the list.
            Returns a tuple containing both lists.
        """
        first_header_set = OrderedSet(first_headers)
        first_header_list = list(first_header_set)

        second_header_set = OrderedSet(second_headers)
        second_header_list = list(second_header_set)

        return first_header_list, second_header_list

    def get_unique_headers(self):
        """
            This method returns a list with the unique headers between
            the different files.
        """
        unique_header_list = []

        first_headers, second_headers = self.create_single_contingency(
            self.first_headers, self.second_headers)

        total_headers = self.merge_headers(first_headers, second_headers)

        current_occurred_headers = self.count_occurrence(total_headers)

        header_dictionary = self.merge_header_names_with_occurrence(
            total_headers, current_occurred_headers)

        for unique_header, count in header_dictionary.items():
            if count == 1:
                unique_header_list.append(unique_header)

        if not unique_header_list:
            print('The files have no different headers.')
        else:
            for item in unique_header_list:
                print(f"\tUnique header in the file:"
                      f"\033[1m \033[31m{item}\033[0m \033[30m")

    @staticmethod
    def merge_headers(first_headers, second_headers):
        """
            This method merges the provided header lists.
            after merging, upper cases the result for easier comparing.
        """
        total_headers = first_headers + second_headers
        total_headers_upper_cased = \
            [header.upper() for header in total_headers]

        return total_headers_upper_cased

    @staticmethod
    def merge_header_names_with_occurrence(headers, occurrence):
        """
            This method combines the headers with their occurrences,
            for example:
            key name: value 1 == unique.
            key stuff: value 2 == common ground.
        """
        header_dictionary = {}
        unique_header = OrderedSet(headers)
        header_list = list(unique_header)

        for count in range(len(header_list)):
            header_dictionary.update(
                {header_list[count]: occurrence[count]})

        return header_dictionary
