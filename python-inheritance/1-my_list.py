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
    my_list = MyList()
    print(my_list)  # Output: []
    
    my_list.append(3)
    my_list.append(1)
    my_list.append(4)
    my_list.append(1)
    my_list.append(5)
    my_list.append(9)
    my_list.append(2)
    my_list.append(6)
    my_list.append(5)
    print(my_list)  # Output: [3, 1, 4, 1, 5, 9, 2, 6, 5]
    
    my_list.print_sorted()  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]
    
    my_list = MyList()
    my_list.append(-3)
    my_list.append(-1)
    my_list.append(4)
    my_list.append(-1)
    my_list.append(5)
    my_list.append(-9)
    my_list.append(2)
    my_list.append(-6)
    my_list.append(5)
    print(my_list)  # Output: [-3, -1, 4, -1, 5, -9, 2, -6, 5]
    
    my_list.print_sorted()  # Output: [-9, -6, -3, -1, -1, 2, 4, 5, 5]

