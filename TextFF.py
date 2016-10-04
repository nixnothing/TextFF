from random import randint as rand
import sys

class Potion(object):
    def __init__(self, amount=2):
        self.name = "Potion"
        self.ammount = amount

    def effect(self, user):
        #gains 10 hp
        user.hp += 10
        if user.hp > user.maxhp:
            user.hp = user.maxhp


class SuperPotion(object):
    def __init__(self, amount=1):
        self.name = "Super Potion"
        self.ammount = amount

    def effect(self, user):
        #gains 20 hp
        user.hp += 20
        if user.hp > user.maxhp:
            user.hp = user.maxhp


def dprint(s):
    print s


def itemcount(lst, tpe):
    return len([item for item in lst if isinstance(item, tpe)])


class Fighter:
    def __init__(self, name, hp, mp, att, defense, spd, acc, intel, run, itemlist={}):
        self.maxhp = 100
        self.maxmp = 50
        self.name = name
        self.hp = hp
        self.mp = mp
        self.att = att
        self.defense = defense
        self.intel = intel
        self.spd = spd
        self.acc = acc
        self.run = run
        self.reset = True
        self.mobroll = rand(1, 10)
        self.itemlist = [Potion(), Potion(), SuperPotion()]

    def playername(self):
        print "\n" + self.name

    def health(self):
        if self.hp > 0:
            str_hp = "="*(self.hp/10)
            print "[" + str_hp + " "*(10-len(str_hp)) + "]" + " " + "HP: " + str(self.hp) + "/" + str(self.maxhp) + "  MP: " + str(self.mp) + "/" + str(self.maxmp)
        else:
            print "[" + " DEAD! " + "] \n"
            print self.name + "has been defeated!"
            raw_input()
            sys.exit()

    def fight(self, opponent):
        #roll 1-20, 19,20 crit, crit dmg val x2
        print("\nUsing attack value: " + str(self.att) + "\n")
        hitluck = rand(1, 10)
        if self.acc >= opponent.spd or hitluck > 6:
            crit = rand(1, 20)
            dprint("Using crit value (1-20): " + str(crit) + "\n")
            if crit > 18:
                print self.name + " has struck a critical blow! \n"
                print self.name, "has dealt", self.att*2, "damage to", opponent.name
                opponent.hp -= self.att*2
            else:
                print self.name, "has dealt", self.att, "damage to", opponent.name
                opponent.hp -= self.att
        else:
            print self.name + " missed!"

    def skill(self):

        if self.mp > 0:
            while True:
                print "\nWhat ability would you like to use?:"
                print "[Slash]\n[Mega-Slash]\n[Magic Missiles]\n[Exit]"
                skillaction = raw_input(":")
                if skillaction.lower() == "exit":
                    self.reset = True
                    break
                else:
                    print "\nYou have not entered a valid option!"
        else:
            print "\nYou are all out of mana!"
            self.reset = True


    def slash(self):
        pass

    def megaslash(self):
        pass

    def magicmissiles(self):
        pass

    def useitem(self, it):
        theitem = None
        for i in self.itemlist:
            if isinstance(i, it):
                theitem = i
                break
        theitem.effect(self)
        del self.itemlist[self.itemlist.index(theitem)]

    def item(self):
        if len(self.itemlist) > 0:
            potion_num = itemcount(self.itemlist, Potion)
            superpotion_num = itemcount(self.itemlist, SuperPotion)
            print "\nWhich item would you like to use?: "

            while True:
                if potion_num > 0:
                    print "[" + "potion" + "  x" + str(potion_num) + "]"
                if superpotion_num > 0:
                    print "[" + "super potion" + "  x" + str(superpotion_num) + "]"
                print "[Exit]"
                itemaction = raw_input(":")
                if itemaction.lower() == "potion":
                    self.useitem(Potion)
                    print "\n" + self.name + " gained 10 health!"
                    break
                elif itemaction.lower() == "super potion":
                    self.useitem(SuperPotion)
                    print "\n" + self.name + " gained 20 health!"
                    break
                elif itemaction.lower() == "exit":
                    self.reset = True
                    break
                else:
                    print "You have not entered a valid option!"

        else:
            print "\nYou have no items!\n"
            self.reset = True

    def escape(self):
        if self.mobroll > 8:
            print self.name + " cannot run from this battle! \n"
            self.reset = True
        else:
            runcheck = rand(0, 100)
            if runcheck >= 75:
                print self.name + " has successfully fled from battle!"
                raw_input()
                sys.exit()
            else:
                print self.name + " has failed to flee from battle! \n"

    def autoturn(self):
        print "\n" + self.name + "'s Turn! \n" + "=========================="
        autoroll = rand(7, 10)
        if autoroll >= 7 and autoroll < 9:
            badguy.fight(goodguy)
        #elif autoroll >= 4 and autoroll < 7:
            #print "hey"
            #  skill
        #elif autoroll >= 7 and autoroll < 10:
            #pass
            #  magic
        if autoroll == 10:
            badguy.escape()

goodguy = Fighter("Thunder", rand(20, 100), rand(0, 50), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10))

badguy = Fighter("Dark-Death Evilman", rand(20, 100), rand(0, 50), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10), rand(0, 10))


def heroturn():
    #Hero Turn
    #while goodguy.Run == "no":
    #If run is successful, the encounter ends.
    goodguy.reset = True
    while goodguy.reset:
    #resets menu in case of incorrect input and "cant escape"
        goodguy.reset = False
        healthstat()
        print "\n" + goodguy.name + "'s turn!\n========================"
        action = raw_input("What do you want to do?: \n(Fight, Skill, Item, Run)\n:")
        if action.lower() == "fight":
            goodguy.fight(badguy)
            healthstat()
        elif action.lower() == "skill":
            goodguy.skill()
        elif action.lower() == "item":
            goodguy.item()
        elif action.lower() == "run":
            goodguy.escape()
        else:
            print "Incorrect input, Try Again.\n"
            goodguy.reset = True


def healthstat():
    goodguy.playername()
    goodguy.health()
    badguy.playername()
    badguy.health()

#Que enemy
print "Wild " + badguy.name + " Appeared!" + "\n" + "================================="

while True:
    heroturn()
    badguy.autoturn()