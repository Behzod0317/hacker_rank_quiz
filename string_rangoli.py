def print_rangoli(size):
    import string
    lines = []
    alphabet = string.ascii_lowercase
    for i in range(size):
        row = '-'.join(alphabet[size-1:i:-1]+alphabet[i:size])
        lines.append((row.center(size*4-3,'-')))
    # your code goes here
    print('\n'.join(lines[:0:-1] + lines))

if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)