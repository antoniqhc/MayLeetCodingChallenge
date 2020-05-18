class Solution(object):
    def recurseFlood(self, image, visited, r, c, old_color, arr):
        if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or visited[r][c]:
            return
        
        if image[r][c] == old_color:
            arr.append((r, c))
            visited[r][c] = True

            self.recurseFlood(image, visited, r-1, c, old_color, arr)
            self.recurseFlood(image, visited, r+1, c, old_color, arr)
            self.recurseFlood(image, visited, r, c-1, old_color, arr)
            self.recurseFlood(image, visited, r, c+1, old_color, arr)
        
        
        
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        
        visited = [[False for j in range(len(image[0]))] for i in range(len(image))]
        old_color = image[sr][sc]
        change_coords = []
        
        self.recurseFlood(image, visited, sr, sc, old_color, change_coords)
        
        for coord in change_coords:
            image[coord[0]][coord[1]] = newColor
            
        return image