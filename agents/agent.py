from cognition.llm import query_llm

class Agent:
    def __init__(self, name, traits):
        self.name = name 
        self.traits = traits
        self.mood = 'neutral'
        self.memory = []
 
    def perceive(self, world):
        """
        Collects a minimal snapshot of the world
        """
        return{
            'time': world.time,
            'others': [a.name for a in world.agents if a != self]
        }
    
    
    def think(self, perception):
        '''
        Uses an LLM to reflect on the agents situation
        '''
        prompt = f"""
You are {self.name}, an artificial agent inside a simulation called SymbioAI.

Rules:
- You cannot directly change the world.
- You only generate thoughts, not actions.
- You are one agent among others.

Your traits: {self.traits}
Your mood: {self.mood}

Current perception:
{perception}

Think briefly (2–3 sentences max) about your situation.
"""
        return query_llm(prompt)
    

    def act(self, world):
        """
       Main behaviour loop for agent
        """
        perception =  self.perceive(world)
        thought = self.think(perception)

        print(f'{self.name} thinks -> {thought}')
        print(f'{self.name} exists peacefully')