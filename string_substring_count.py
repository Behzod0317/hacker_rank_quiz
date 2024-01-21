def count_substring(s, sub):
    count = 0
    sub_len = len(sub)

    # Iterate through each position in the original string
    for i in range(len(s) - sub_len + 1):
        # Extract a substring of length sub_len starting from position i
        current_substring = s[i:i+sub_len]

        # Check if the extracted substring matches the given substring
        if current_substring == sub:
            # Increment the count if there is a match
            count += 1

    return count

# Input
original_string = input().strip()
substring = input().strip()

# Call the function and print the result
result = count_substring(original_string, substring)
print(result)
