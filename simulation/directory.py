

class Directory:
    
    def __init__(self, width, height):
        self.agents = dict()        
                
    def add(self, agent):
        self.agents[agent.id] = agent
        
    def remove(self, agent):
        self.agents[agent.id].remove(agent)
        
    def move(self, agent):
        self.agents[agent.id].remove(agent)
        self.add(agent)
        
        
