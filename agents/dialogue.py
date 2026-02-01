class Message:
    def __init__(self, sender, content):
        self.sender = sender
        self.content = content

    def __repr__(self):
        return f'{self.sender}: {self.content}'