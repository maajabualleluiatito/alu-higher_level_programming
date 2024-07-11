#!/usr/bin/python3
"""
A module to print a list in ascending order
"""


class MyList(list):
    """
    A class to customize the list class
    """

    def print_sorted(self):
        """
        Prints a list in ascending order

        Sorts a list and then prints it to the output
        """
        print(sorted(self))

# Example usage
if __name__ == "__main__":
    my_list = MyList([3, 1, 4, 1, 5, 9, 2, 6, 5])
    my_list.print_sorted()  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
