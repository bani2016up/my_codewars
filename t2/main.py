'''
https://www.codewars.com/kata/545cedaa9943f7fe7b000048 
A pangram is a sentence that contains every single letter of the alphabet at least once. For example, the sentence "The quick brown fox jumps over the lazy dog" is a pangram, because it uses the letters A-Z at least once (case is irrelevant).

Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and punctuation.
'''

def is_pangram(s):
    

    
    list_s = list(s.lower())
    list_s.sort()
    set_s = set()
    for i in list_s:
        if ord(i) >= 97 and ord(i)<= 122:
            set_s.add(i)
    if set_s == {'u', 'g', 'm', 'i', 'q', 'b', 'y', 'c', 'l', 'w', 'v', 'f', 'j', 'z', 'n', 'h', 's', 'a', 'p', 'k', 'o', 'e', 'r', 'x', 't', 'd'}:
        return True
    else:
        return False        

print(is_pangram('The quick, brown fox jumps over the lazy dog!'))