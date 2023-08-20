class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:

        def invert(value):
            return 0 if value == 1 else 1

        
        for i in range(len(image)):
            for j in range(math.ceil(len(image[i])/2)):
                mirrorIndex = len(image[i])-j-1

                image[i][j], image[i][mirrorIndex] = invert(image[i][mirrorIndex]), invert(image[i][j])

    
               

        return image
        

        