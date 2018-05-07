

class Space:
    
    def __init__(self, width, height, toroidal=False):
        
        self.width = width
        self.height = height
        self.toroidal = toroidal
        
        self.space = [[0]*self.width]*self.height
        
        
    def get_point(self, x, y):        
        return self.space[x][y]
        
    
    def set_point(self, x, y):
        
        if x < 0:
            x = 0
        elif x > self.width - 1:
            x = self.width - 1
            
        if y < 0:
            y = 0
        elif y > self.height - 1:
            y = self.height - 1
            
        return x, y
