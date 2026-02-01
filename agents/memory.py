class Memory: 
    def __init__(self):
        self.short_term = []
        self.long_term = []

    def remember(self, event:str, important = False):
        self.short_term.append(event)
        if important:
            self.long_term.append(event)
            if important:
                self.long_term.append(event)

    
    def summarize(self):
        return ' | '.join(self.long_term[-5:])