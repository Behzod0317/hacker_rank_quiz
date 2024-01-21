# if __name__ == '__main__':
#     n = int(input("Enter the number of elements in the tuple: "))
#     integer_list = map(int, input("Enter space-separated integers: ").split())

#     # Creating a tuple from the input
#     my_tuple = tuple(integer_list)

#     # Calculating and printing the hash value
#     result = hash(my_tuple)
#     print(result)
if __name__ == '__main__':
    n = int(input("Enter the number of elements in the tuple: "))
    integer_list = map(int, input("Enter space-separated integers: ").split())

    # Creating a tuple from the input
    my_tuple = tuple(integer_list)

    # Calculating and printing the hash value
    result = hash(my_tuple)
    print(result)
