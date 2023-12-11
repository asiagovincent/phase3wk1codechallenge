def exactly_two_positive(a, b, c):
    # Count the number of positive numbers
    positive_count = 0

    # Check each number and update positive_count
    if a > 0:
        positive_count += 1
    if b > 0:
        positive_count += 1
    if c > 0:
        positive_count += 1

    # Return True if exactly two of the three numbers are positive
    return positive_count == 2

# Examples:
print(exactly_two_positive(2, 4, -3))   
print(exactly_two_positive(-4, 6, 8))   
print(exactly_two_positive(4, -6, 9))   
print(exactly_two_positive(-4, 6, 0))   
print(exactly_two_positive(4, 6, 10))   
print(exactly_two_positive(-14, -3, -4)) 
