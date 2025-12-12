#reverse the string 

def reverse_string(s1):
    lst=[]
    s1=s1.split()
    print(s1)
    for i in s1:
        i=i.split()
        for j in i:
            lst.append(j[::-1])
            
    return ' '.join(lst)


print(reverse_string('hello world'))