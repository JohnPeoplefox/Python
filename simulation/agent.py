

class Agent:

    ID = 0
    
    def __init__(self, x, y, space):

        self.id = Agent.ID
        Agent.ID +=1
        
        self.space = space
        
        self.x = x
        self.y = y
        
        self.old_x = x
        self.old_y = y
        
        
    def __eq__(self, other):
        return self.id == other.id
        
        
    def step(self):
        
        self.old_x = self.x
        self.old_y = self.y
