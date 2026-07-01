import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        if not s:
            return true
        s = s.lower()
        s = s.translate(str.maketrans("","", string.punctuation))
        s= "".join(s.split())
        is_palindrome = s == s[::-1]
        return is_palindrome
