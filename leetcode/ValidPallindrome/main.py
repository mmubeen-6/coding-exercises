import re

def valid_pallindrome(s : str) -> bool:
    s = s.replace(" ", "").lower()
    s = re.sub(r'[^a-zA-Z0-9]', '', s)
    
    l, r = 0, len(s)-1
    while (l < r):
        if s[l] != s[r]:
            return False
        
        l += 1
        r -= 1       
    
    return True


if __name__ == '__main__':
    print(valid_pallindrome("A man, a plan, a canal: Panama") == True)
    print(valid_pallindrome("race a car") == False)
    print(valid_pallindrome(" ") == True)