#find the count occurences of each character in the string

def get_count(s1):
    s2=s1.replace(" ", "").lower()
    count_dict={}

    # for char in s2:
    #     if char in count_dict:
    #         count_dict[char] += 1
    #     else:
    #         count_dict[char] =count_dict.get(char,0)+1

    for char in s2:
        count_dict[char]=count_dict.get(char,0)+1
    
    return count_dict







a="listessn"
print(get_count(a))