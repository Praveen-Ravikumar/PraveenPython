def longest_palindrome_substring(s):
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]

    if not s or len(s) == 1:
        return s

    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (center at i)
        palindrome1 = expand_around_center(i, i)
        # Even-length palindrome (center between i and i+1)
        palindrome2 = expand_around_center(i, i + 1)

        # Update the longest palindrome found
        if len(palindrome1) > len(longest):
            longest = palindrome1
        if len(palindrome2) > len(longest):
            longest = palindrome2

    return longest

# Example usage
input_string = "babad"
result = longest_palindrome_substring(input_string)
print(f"The longest palindromic substring is: '{result}'")
