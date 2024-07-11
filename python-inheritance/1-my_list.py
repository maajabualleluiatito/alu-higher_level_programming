#!/usr/bin/python3
"""
Module 1-my_list

Contains class MyList
inherits from list; has public instance method to print sorted
"""

class MyList(list):
    """Inherits from list

    Methods:
    print_sorted(self)
    """
    
    def print_sorted(self):
        """Prints the list of integers in ascending order"""
        print(sorted(self))


"""
Module to test the functionality of MyList class
"""

# Import the MyList class from the 1-my_list module
MyList = __import__('1-my_list').MyList

def main():
    # Create an instance of MyList
    my_list = MyList()

    # Append elements to the list
    my_list.append(1)
    my_list.append(4)
    my_list.append(2)
    my_list.append(3)
    my_list.append(5)

    # Print the original list
    print("Original list:", my_list)

    # Use the print_sorted method to print the sorted list
    print("Sorted list:", end=" ")
    my_list.print_sorted()

    # Print the original list again to show that it hasn't been modified
    print("Original list after sorting:", my_list)

if __name__ == "__main__":
    main()
