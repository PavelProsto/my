from random import randint


class Person:
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp
        self.level = 1
    
    def make_kick(self, enemy):
        enemy.health -= 20
        if enemy.health < 0:
            enemy.health = 0
        self.health += 10
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.health))


        
class Player(Person):
    def __init__(self, name, hp) -> None:
        Person.__init__(self, name, hp = 100)
        
    #def up_level(self):
    #    self.level += 1

        
class Monster(Person):
    def __init__(self, name, hp) -> None:
        Person.__init__(self, name, hp = 75)
        #self.my_treasure = None
    #def follow(self, hero):
     #   self.my_hero = hero.id


class Battle:
    def __init__(self, plr, mnstr) -> None:
        self.plr = plr
        self.mnstr = mnstr
        self.result = "Сражения не было"
    def battle(self):
        while self.plr.health > 0 and self.mnstr.health > 0:
            n = randint(1, 2)
            if n == 1:
                self.plr.make_kick(self.mnstr)
            else:
                self.mnstr.make_kick(self.plr)
        if self.plr.health > self.mnstr.health:
            self.result = self.plr.name + " ПОБЕДИЛ"
        elif self.mnstr.health > self.plr.health:
            self.result = self.mnstr.name + " ПОБЕДИЛ"
    def who_win(self):
        print(self.result)
        
        
player_name = input('Введите имя игрока')
player1 = Player(player_name)
monster1 = Monster('Abrvalk')
b = Battle(player1, monster1)
b.battle()
b.who_win()




#first = Soldier('Mr. First', 140)
#second = Soldier()
#second.set_name('Mr. Second')





#h1 = Hero(1)
#h2 = Hero(2)
#army1 = []
#army2 = []
#for i in range(20):
#    n = randint(1, 2)
#    if n == 1:
#        army1.append(Soldier(n))
#    else:
#        army2.append(Soldier(n))
#print(len(army1), len(army2))
#if len(army1) > len(army2):
#    h1.up_level()
#elif len(army1) < len(army2):
#    h2.up_level()
#army1[0].follow(h1)
#print(army1[0].id, h1.id, h1.level, h2.id, h2.level)
#
#
#class Soldier:
#    def __init__(self, name='Noname', health = 100) -> None:
#        
        
    
    






