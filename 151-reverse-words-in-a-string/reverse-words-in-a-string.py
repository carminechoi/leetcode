class Solution:
    def reverseWords(self, s: str) -> str:
        words = s.split(" ")
        print(words)
        reversed = ""
        for i, word in enumerate(words[::-1]):
            if word != "":
                reversed += word + " "
        
        return reversed[0: len(reversed)-1]