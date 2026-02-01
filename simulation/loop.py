def run_simulation(world, steps =11):
    for _ in range(steps):
        world.step()
        