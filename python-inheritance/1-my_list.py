#!/usr/bin/python3
class MyList(list):
    def print_sorted(self):
        # Sort the list and print it
        print(sorted(self))

# Create an instance of MyList
my_list = MyList()

# Add some elements to the list
my_list.append(3)
my_list.append(1)
my_list.append(4)
my_list.append(1)
my_list.append(5)
my_list.append(9)

# Print the original list
print("Original list:")
print(my_list)

# Print the sorted list using the print_sorted method
print("Sorted list:")
my_list.print_sorted()
