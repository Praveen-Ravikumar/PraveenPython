# program to check if a vowel is present in a string

def vowel(s):
    count=0
    for char in s:
        if 'a'==char or 'e'==char or 'i'==char or 'o'==char or 'u'==char:
            count=count+1
            
    return count

rev=vowel("helloworld")
print(rev)
