def mutate_string(string, position, character):
    s_list = list(string)
    
    
    s_list[position] = character
    
    # Join the list back into a string
    modified_string = ''.join(s_list)
    
    return modified_string


if __name__ == '__main__':
    string = input('Enter a string: ')
    position= input(int('Enter a position where you want to change: ').split())
    character = input('Enter a character which you want to change: ').split()
    s_new = mutate_string(string, int(position), character)
    print(s_new)