# Mo
# 1/7/25
# Example of a class
class Weapon:
    def __init__(self, name, damage, durability):
        self.name = name
        self.damage = damage
        self.durability = durability
    def attack(self, target):
        if self.durability > 0:
            self.durability -= 10
            print("Attacked", target, "for", self.damage,"damage.")
        else:
            print("Weapon is too damaged to use!")
    def repair(self):
        self.durability = 100
        print("Weapon repaired")
my_weapon = Weapon("Sword", 25, 100)#instanse of object
my_weapon.attack("Enemy")
print("Durability after attack:", my_weapon.durability)#print out contents of variable
my_weapon.repair()
