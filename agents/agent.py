from agents.dialogue import Message
import subprocess

class Agent:
    def __init__(self, name, traits):
        self.name = name 
        self.traits = traits
        self.memory = []
 

    def think(self, world):
        others = [a.name for a in world.agents if a !=self]

        promot = prompt = f"""
You are {self.name}, an AI agent in a simulation.
Traits: {self.traits}
Other agents present: {others}
Rules:
- Do NOT take actions
- Only think
- Be brief (1–2 sentences)

What are your thoughts?
"""
        response = self._call_llm(promot)
        print(f'{self.name} thinks -> {response}')


    def speak(self, world):
        others = [a.name for a in world.agents if a != self]

        prompt = f"""
You are {self.name}.
Traits: {self.traits}
Other agents: {others}

Speak ONE short sentence to one agent.
Be natural.
"""
        response = self._call_llm(prompt)
        return Message(self.name, response)


    def receive(self, message):
        self.memory.append({
            'from': message.sender,
            'content': message.content
        })

        print(f'{self.name} heard -> {message.sender}: {message.content}')


    
    def update_personality(self):
        delta = 0.0

        for m in self.memory[-5:]:
            text = m['content'].lower()
            if 'thank' in text or 'nice' in text:
                delta += 0.01
            if 'ignore' in text or 'annoy' in text:
                delta -=0.01

        self.traits['kindness'] = round(
            min(1.0, max(0.0, self.traits.get('kindness', 0.5) +delta)),
            3
        )


    def _call_llm(self, prompt):
        try:
            result = subprocess.run(
                ['ollama', 'run', 'qwen3:1.7b'],
                input = prompt, 
                text = True,
                encoding = 'utf-8',
                capture_output = True,
                check = True
            )

            return result.stdout.strip()

        except Exception as e:
            return f'(LLM error: {e})'

