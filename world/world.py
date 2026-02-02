from typing import List

class World:

    def __init__(self):
        self.agents = []
        self.time = 0
        

    def add_agent(self, agent):
        self.agents.append(agent)

    def broadcast(self, sender, message):
        for agent in self.agents:
            if agent != sender:
                agent.receive(message)

    def step(self):
        self.time += 1
        print(f'\n---SymbioAI World Time: {self.time} ...')

       
