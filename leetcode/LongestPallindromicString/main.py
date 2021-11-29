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


def longest_pallindromic_string(s : str) -> str:
    longest_pallendrome = ""
        
    for i in range(len(s), 1, -1):
        for j in range(0, len(s) - i + 1):
            test_string = s[j:j+i]
            if len(test_string) > len(longest_pallendrome) and valid_pallindrome(test_string): 
                longest_pallendrome = test_string
                
    if longest_pallendrome == "" and len(s) > 0:
        longest_pallendrome = s[0]
    
    return longest_pallendrome


if __name__ == '__main__':
    print(longest_pallindromic_string("babad") == "bab")
    print(longest_pallindromic_string("cbbd") == "bb")
    print(longest_pallindromic_string("a") == "a")
    print(longest_pallindromic_string("ac") == "a")
