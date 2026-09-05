class Hero:
    def __init__(self, name, hp=100):
        self.name = name
        self.hp = hp
    
    def take_damage(self, damage=10):
        self.hp -= damage
    
arthur = Hero("Arthur", 100)
morgana = Hero("Morgana", 100)

arthur.take_damage(10)

print(f"Arthur = {arthur.hp}")
print(f"Morgana = {morgana.hp}")