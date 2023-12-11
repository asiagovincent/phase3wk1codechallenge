def solve(s):
    vowels = "aeiou"
    consonant_substrings = [s]
    
    # Split the string into consonant substrings
    for vowel in vowels:
        consonant_substrings = "".join(consonant_substrings).split(vowel)

    # Calculate the value of each consonant substring
    values = [sum(ord(char) - ord('a') + 1 for char in substring) for substring in consonant_substrings]

    # Return the maximum value
    return max(values)

# Examples:
print(solve("zodiacs"))   
print(solve("strength"))  
