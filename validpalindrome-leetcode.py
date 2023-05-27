class Solution:
    def isPalindrome(self, s: str) -> bool:
        string = ""
        s = s.lower()
        for char in s:
            if char.isalnum():
                string+=char
        return string==string[::-1]
