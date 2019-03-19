# Implement a class to hold room information. This should have name and
# description attributes.

class room:
    name: str
    description: str

    def __init__(self, name, desc):
        self.name = name
        self.description = desc