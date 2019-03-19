

class Item:
    name: str
    desc: str

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def onTake(self):
        print(f"Picked up {name}")

    def onDrop(self):
        print(f"Dropped {name}")
