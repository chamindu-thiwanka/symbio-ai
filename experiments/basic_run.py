from world.world import World
from agents.agent import Agent
from simulation.loop import run_simulation

world = World()

yash = Agent('Yashu', {'kindness':0.8})
cham = Agent('Chami', {'kindness':0.3})

world.add_agent(yash)
world.add_agent(cham)

run_simulation(world, steps = 3)