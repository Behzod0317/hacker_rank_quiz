if __name__ == '__main__':
    # Reading the number of students' records
    n = int(input("Enter the number of students: "))
    
    # Creating a dictionary to store name:[marks]
    student_records = {}

    # Reading the names and marks for each student
    for _ in range(n):
        input_data = input("Enter student name and marks separated by space: ").split()
        name = input_data[0]
        marks = list(map(float, input_data[1:]))
        student_records[name] = marks

    # Reading the name of the student to query
    query_name = input("Enter the name of the student to query: ")

    # Calculating the average marks for the specified student
    average_marks = sum(student_records[query_name]) / len(student_records[query_name])

    # Printing the result with 2 decimal places
    print("{:.2f}".format(average_marks))
