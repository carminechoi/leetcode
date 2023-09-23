class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        if len(ransomNote) > len(magazine): 
            return False
        
        letters = collections.Counter(magazine)
        
        for letter in ransomNote:    
            if letters[letter] <= 0:
                return False
            letters[letter] -= 1
        
        return True