

class Item:

    def __init__(self, name, desc):
        self.name = name
        self.desc = desc

    def onTake(self):
        print(f"\n~~~ Picked up {self.name}")

    def onDrop(self):
        print(f"\n~~~ Dropped {self.name}")
