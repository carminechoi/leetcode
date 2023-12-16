class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N == 1:
            return ""

        for i in range(N//2):
            if  palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                return palindrome

        return palindrome[:-1] + "b"

