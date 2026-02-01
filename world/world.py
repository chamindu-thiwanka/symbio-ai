from typing import List

class World:

    def __init__(self):
        self.time = 0
        self.agents: List = []
        

    def add_agent(self, agent):
        self.agents.append(agent)

    def step(self):
        self.time += 1
        print(f'\n---SymbioAI World Time: {self.time} ...')

        for agent in self.agents:
            agent.act(self)
