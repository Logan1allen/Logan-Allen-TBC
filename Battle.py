import TBC

def main():
    spongebob = TBC.Character()
    spongebob.name = "Sponge"
    spongebob.hitPoints = 10
    spongebob.hitChance = 50
    spongebob.maxDamage = 5
    spongebob.armor = 2

    patrick = TBC.Character("Patrick", 20, 30, 5, 0)
    spongebob.printStats()
    patrick.printStats()
    

    TBC.Character.fight(spongebob, patrick)

if __name__ == "__main__":
    main()