'''
https://www.codewars.com/kata/5656b6906de340bd1b0000ac
Take 2 strings s1 and s2 including only letters from a to z. Return a new sorted string, the longest possible, containing distinct letters - each taken only once - coming from s1 or s2.

Examples:
a = "xyaabbbccccdefww"
b = "xxxxyyyyabklmopq"
longest(a, b) -> "abcdefklmopqwxy"

a = "abcdefghijklmnopqrstuvwxyz"
longest(a, a) -> "abcdefghijklmnopqrstuvwxyz"

'''

def longest(a1, a2):
    list_a1 = list()
    set_all = set()
    list_a2 = list() 
       
    for i in a1.lower():
        if ord(i) >= 97 and ord(i)<= 122:
            list_a1.append(i)
            set_all.add(i)
            
    for i in a2.lower():
        if ord(i) >= 97 and ord(i)<= 122:
            list_a2.append(i)
            set_all.add(i)
            
    list_all = list(set_all)
    list_all.sort()
    return ''.join(list_all)
    
print(longest("aretheyhere", "yestheyarehere"))

