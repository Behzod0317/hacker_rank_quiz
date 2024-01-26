def print_door_mat(n, m):
    pattern = [('.|.' * (2 * i + 1)).center(m, '-') for i in range(n // 2)]
    welcome_line = 'WELCOME'.center(m, '-')
    door_mat = '\n'.join(pattern + [welcome_line] + pattern[::-1])
    print(door_mat)

if __name__ == "__main__":
    n, m = map(int, input('Enter  amount of rows and columns: ').split())
    print_door_mat(n, m)