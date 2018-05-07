

class Time:
    
    def tick(self, directory):

        for key, agents in directory.agents.items():
            for agent in agents:
                agent.step()
                directory.move(agent, agent.old_x, agent.old_y)
        
