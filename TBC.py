"""
Turn Based Combat Code

"""
import random

class Character(object):
    
    def __init__(self, name = "Character", hitPoints = 20, hitChance = 70, maxDamage = 5, armor = 1):
        super().__init__()
        self.name = name
        self.hitPoints = hitPoints
        self.hitChance = hitChance
        self.maxDamage = maxDamage
        self.armor = armor
        
    @property
    def name(self):
        return self.__name
        
    @name.setter
    def name(self, value):
        self.__name = value
            
    @property
    def hitPoints(self):
        return self.__hitPoints
        
    @hitPoints.setter
    def hitPoints(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitPoints = value
            else:
                print("Hitpoints must be positive")
        else:
            print("Hitpoints must be a number")

    @property
    def hitChance(self):
        return self.__hitChance
        
    @hitChance.setter
    def hitChance(self, value):
        if type(value) == int:
            if value >= 0:
                self.__hitChance = value
            else:
                print("HitChance must be positive")
        else:
            print("HitChance must be a number")

    @property
    def maxDamage(self):
        return self.__maxDamage
        
    @maxDamage.setter
    def maxDamage(self, value):
        if type(value) == int:
            if value >= 0:
                self.__maxDamage = value
            else:
                print("Max Damage must be positive")
        else:
            print("Max Damage must be a number")
            
    @property
    def armor(self):
        return self.__armor
        
    @armor.setter
    def armor(self, value):
        if type(value) == int:
            if value >= 0:
                self.__armor = value
            else:
                print("Armor must be positive")
        else:
            print("Armor must be a number")
                
            
    def printStats(self):
        print(f"Name: {self.name}")
        print(f"Hit Points: {self.hitPoints}")
        print(f"Hit Chance: {self.hitChance}")
        print(f"Max Damage: {self.maxDamage}")
        print(f"Armor: {self.armor}")
        print()
                    
    
    
    
    
    def hit(self, enemy):
        if random.randint(1,100) < self.hitChance:
            print(f"{self.name} hits {enemy.name}... ")
            damage = random.randint(1, self.maxDamage)
            print(f"for {damage} points of damage")
            damage -= enemy.armor
            if damage < 0:
                damage = 0
            if enemy.armor > 0:
                print(f" but {enemy.name}'s armor absorbs {enemy.armor} points")
            enemy.hitPoints -= damage
        else:
            print(f"{self.name} misses {enemy.name}")
        
        print(f"{enemy.name} hits {self.name}")
        
        
    def testInt(self, value, min = 0, max = 100, default = 0):
        out = default

        if type(value) == int:
            if value >= min:
                if value <= max:
                    out = value 
                else:
                    print("Too large")
            else:
                print("Too small")
        else:
            print("Must be an int")

        return out
        
      
    def fight(player1, player2):
        
        keepGoing = True
        while keepGoing:
            nextRound = input("Press enter for next round. ")
            player1.hit(player2)
            player2.hit(player1)
            
            print(f"{player1.name} has {player1.hitPoints}HP left")
            print(f"{player2.name} has {player2.hitPoints}HP left")
                
            if player1.hitPoints <= 0:
                print (f"{player1.name} loses the game... ")
                keepGoing = False
            elif player2.hitPoints <= 0:
                print(f"{player2.name} loses the game... ")
                keepGoing = False

 
def main():
    player1 = Character("Chicken", 20, 40, 3, 2)
    player2 = Character("Darth Vader", 40, 70, 8, 0)
    Character.fight(player1, player2)
    
    
    
if __name__ == "__main__":
    main()