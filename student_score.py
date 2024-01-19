if __name__ == '__main__':
    n = int(input())
    
    students = []

    # Reading input for each student and populating the 'students' list
    for _ in range(n):
        name = input()
        score = float(input())
        students.append([name, score])

    # Finding the second lowest grade
    unique_scores = sorted(set(score for name, score in students))
    second_lowest_score = unique_scores[1]

    # Sorting names alphabetically for students with the second lowest grade
    names_second_lowest = sorted([name for name, score in students if score == second_lowest_score])

    # Printing names of students with the second lowest grade
    for name in names_second_lowest:
        print(name)
