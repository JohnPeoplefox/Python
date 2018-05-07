
from random import randint
from agent import Agent

class MyAgent(Agent):
    
    def __init__(self, x, y, space):

        super().__init__(x, y, space)

        self.step()

        self.red = randint(1, 255)
        self.green = randint(1, 255)
        self.blue = randint(1, 255)        

        
    def step(self):
        
        super().step()
        
        self.x, self.y = self.space.set_point(
                self.x + randint(-1, 1),
                self.y + randint(-1, 1))

       
    
