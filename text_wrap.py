import textwrap

def wrap(string, max_width):
    wrapped_text = textwrap.fill(string, max_width)
    return wrapped_text
    

if __name__ == '__main__':
    string = input('Enter a string: ')
    max_width =  int(input('Number : '))
    result = wrap(string, max_width)
    print(result)