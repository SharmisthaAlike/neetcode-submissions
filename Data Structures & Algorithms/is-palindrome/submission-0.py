class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean =''
        for ch in s:
            if ch.isalnum():
                clean+=ch.lower()

        return clean==clean[::-1]