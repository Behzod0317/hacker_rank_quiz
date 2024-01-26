def print_formatted(number):
    width = len(bin(number)[2:])
    
    for i in range(1, number + 1):
        decimal_format = str(i).rjust(width)
        octal_format = oct(i)[2:].rjust(width)
        hexadecimal_format = hex(i)[2:].upper().rjust(width)
        binary_format = bin(i)[2:].rjust(width)
        
        print(f"{decimal_format} {octal_format} {hexadecimal_format} {binary_format}")

if __name__ == "__main__":
    n = int(input())
    print_formatted(n)
