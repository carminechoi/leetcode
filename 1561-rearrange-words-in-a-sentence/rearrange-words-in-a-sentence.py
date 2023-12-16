class Solution:
    def arrangeWords(self, text: str) -> str:
        words = text.split(" ")
        words.sort(key=lambda word: len(word))
        
        result = " ".join(words)
        result = result.capitalize()

        return result