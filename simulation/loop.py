def run_simulation(world, steps =3):
    for _ in range(steps):
        world.step()

        for agent in world.agents:
            agent.think(world)

        for agent in world.agents:
            message = agent.speak(world)
            world.broadcast(agent, message)

        for agent in world.agents:
            agent.update_personality()
            print(f'{agent.name} -> {agent.traits}')

        for agent in world.agents:
            print(f'{agent.name} exists peacefully !')
        