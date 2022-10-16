class Person:
    def __init__(self, name, hp) -> None:
        self.name = name
        self.hp = hp
        self.level = 1
    
    def make_kick(self, enemy):
        enemy.hp -= 20
        if enemy.hp < 0:
            enemy.hp = 0
        self.hp += 10
        print(self.name, "бьет", enemy.name)
        print('%s = %d' % (enemy.name, enemy.hp))


        
class Player(Person):
    def __init__(self, name = 'Igrok', hp = 100) -> None:
        Person.__init__(self, name, hp)
        
    #def up_level(self):
    #    self.level += 1

        
class Monster(Person):
    def __init__(self, name = 'Monster', hp = 75) -> None:
        Person.__init__(self, name, hp)
        #self.my_treasure = None
    #def follow(self, hero):
     #   self.my_hero = hero.id


class Battle:
    def __init__(self, plr, mnstr) -> None:
        self.plr = plr
        self.mnstr = mnstr
        self.result = "Сражения не было"
    def battle(self):
        while self.plr.hp > 0 and self.mnstr.hp > 0:
            n = randint(1, 2)
            if n == 1:
                self.plr.make_kick(self.mnstr)
            else:
                self.mnstr.make_kick(self.plr)
        if self.plr.hp > self.mnstr.hp:
            self.result = self.plr.name + " ПОБЕДИЛ"
        elif self.mnstr.hp > self.plr.hp:
            self.result = self.mnstr.name + " ПОБЕДИЛ"
    def who_win(self):
        print(self.result)
        
        