BATTLE

define main
main should have player 1 also known as spongebob
call spongebob as TBC.Character
give him the name spongebob
give him 10 health
50 hit chance
5 max damage
2 armor

make patrick get a TBC Character and define his stats as patarick, 20, 30, 5, 0
print spongebobs stats
print patricks stats

call TBC.fight with the parameters spongebob and patrick

use the if__main__ to allow this code to be easily reused later




TBC
Import random
make a class called charater with the object parameter

define __init__ with the Name of the character and its number stats
make self get each of the stats

@property
define name with parameters self
return self.name

@name.setter
define name with parameters self and value
    self.name = value
    
@property
define hitpoints with parameter self
return self.hitPoints

@hitpoints.setter
define hitpoints with parameters self, value
if type(value) == int:
if value >= 0:
self.__hitPoints = value
else
print Hitpoints must be positive
else
print Hitpoints must be a number

Do the exact same for hitchance but use hitchance instead of hitpoints

Do the exact same for maxDamage but use maxDamage instead of hitchance

Do the exact same for armor but use armor instead of maxDamage

define printstats
print each character stat

define hit with the parameters self and enemy
if random.randint(1,100) < self.hitChance:
print self.name hits enemy.name...
damage gets random.randint(1, self.maxDamage)
print for damage points of damage
damage -= enemy.armor
if damage < 0:
damage gets 0
if enemy.armor > 0:
print but enemy.name's armor absorbs enemy.armor points
enemy.hitPoints -= damage
else:
print self.name misses enemy.name
        
print enemy.name hits self.name

define fight with parameters player1 and player2
        
keepGoing gets True
while keepGoing:
nextRound gets input Press enter for next round. 
player1.hitplayer2
player2.hitplayer1
            
print player1.name has player1.hitPointsHP left
print player2.name has player2.hitPointsHP left
                
if player1.hitPoints <= 0:
print player1.name loses the game... 
keepGoing get False
elif player2.hitPoints <= 0:
print player2.name loses the game... 
keepGoing gets False

define main
player1 gets Character("Chicken", 20, 40, 3, 2)
player2 gets Character("Darth Vader", 40, 70, 8, 0)
Character.fight(player1, player2)
    
    
    
if __name__ == "__main__":
    main()





























