class Solution:
    def countValidWords(self, sentence: str) -> int:
        wordCount = 0
        words = sentence.split()

        for word in words:
            valid = True
            hasHyphen = False
            for i, letter in enumerate(word):
                if letter.isdigit():
                    valid = False
                    break
                if letter in ("!",".",",") and i != len(word)-1:
                    valid = False 
                    break
                if (letter == "-" and (i == len(word)-1 or i == 0)) or (letter == "-" and (not word[i-1].isalpha() or not word[i+1].isalpha())):
                    valid = False 
                    break
                if letter == "-":
                    if hasHyphen:
                        valid = False 
                        break
                    hasHyphen = True
            if valid:
                wordCount += 1
        
        return wordCount
