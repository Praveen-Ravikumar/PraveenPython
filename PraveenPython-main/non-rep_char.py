# find the first non-repeating character in the string

def non_repeating_char(s1):
    s1 = s1.replace(" ","").lower()
    char_count = {}

    for char in s1:
        char_count[char]= char_count.get(char,0)+1
    
    for char in s1:
        if char_count[char] == 1:
            return char
    return None

a=input("enter the string:")
print(non_repeating_char(a))
