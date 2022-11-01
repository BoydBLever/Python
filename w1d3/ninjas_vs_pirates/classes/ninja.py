class Ninja:
    
    def __init__( self , name ):
        self.name = name
        self.strength = 50
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")

    def attack( self , pirate ):
        pirate.health -= self.strength#-10 in damage
        if pirate.health <= 0:
            print("Black beard is dead.")
        return self
    
    def heal( self, pirate):
        pirate.health += self.strength
        print("Coding Ninja: I possess the ultimate power!\n I taketh away your life, and I can giveth your life back.")
        if pirate.health > 0:
            print("Black beard says: Thank you for saving my life.")
        return self

    def heal_thyself(self):
        self.health += 30
        print("You can strike me down, but I only grow stronger.")
        print(f"My health is: {self.health}.")
        return self