class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        N = len(palindrome)
        if N == 1:
            return ""
        replaced = False

        for i in range(N//2):
            if not replaced and palindrome[i] != 'a':
                palindrome = palindrome[:i] + 'a' + palindrome[i+1:]
                replaced = True
                break

        if not replaced:
            return palindrome[:-1] + "b"

        return palindrome