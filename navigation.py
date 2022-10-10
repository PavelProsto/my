from sys import exit
from random import randint
from textwrap import dedent

class Scene(object):

    def enter(self):
        print("Эта сцена еще не настроена.")
        print("Создайте подкласс и реализуйте функцию enter().")
        exit(1)


class Engine(object):

    def __init__(self, scene_map):
        self.scene_map = scene_map

    def play(self):
        current_scene = self.scene_map.opening_scene()
        last_scene = self.scene_map.next_scene('finished')

        while current_scene != last_scene:
            next_scene_name = current_scene.enter()
            current_scene = self.scene_map.next_scene(next_scene_name)

        # не забудьте вывести последнюю сцену
        current_scene.enter()


class Death(Scene):

    quips = [
        "Ваше путешествие заверешено.",
        "Подземелия и драконы, говорили они... Бдет весело, говорили они...",
        "Вы были чрезмерно самонадеяны.",
        "Монстры глумятся над вашим трупом.",
        "Свет! Я вижу свет!"
    ]

    def enter(self):
        print(Death.quips[randint(0, len(self.quips)-1)])
        exit(1)


class Entrance_of_the_dungeon(Scene):

    def enter(self):
        print(dedent("""
            Перед вами мрачный и манящий вход в подземелье.
            Бла бла бла 
            возможные действия зайти .
            """))

        action = input("> ")

        if action == "зайти":
            print(dedent("""
                Вы проскальзываете в портал входа на встречу приключениям.
                """))
            return 'lader'

       # elif action == "подождать":
       #     print(dedent("""
       #         Внезапно вам на встречу выскакиевает монстр, начинается битва!
       #         """))
       #     return 'battle'

        else:
            print("Выберите один из предложенных вариантов")
            return 'entrance'

class LaserWeaponArmory(Scene):

    def enter(self):
        print(dedent("""
            Ты вбегаешь в оружейную лабораторию и начинаешь обыскивать 
            комнату, спрятались ли тут другие готоны.  Стоит мертвая тишина. 
            Ты бежишь в дальний угол комнаты и находишь нейтронную бомбу в 
            защитном контейнере. На лицевой стороне контейнера расположена 
            панель с кнопками и тебе надо ввести правильный код, чтобы 
            достать бомбу. Если ты 10 раз введешь неправильный код, контейнер 
            заблокируется и ты не сможешь достать бомбу. Учти, что код 
            состоит из 3 цифр.
            """))

        code = f"{randint(1,9)}{randint(1,9)}{randint(1,9)}"
        guess = input("[keypad]> ")
        guesses = 0

        while guess != code and guesses < 10:
            print("ВЖЖЖИИИК!")
            guesses += 1
            guess = input("[keypad]> ")

        if guess == code:
            print(dedent("""
                Контейнер открывается со щелчком и выпускает сизый газ. 
                Ты вытаскиваешь нейтронную бомбу и бежишь в топливный отсек, 
                чтобы установить бомбу в нужном месте, активировать ее и 
                успеть смотаться с корабля.
                """))
            return 'the_bridge'
        else:
            print(dedent("""
                Ты слышишь, как замок жужжит последний раз, а затем 
                чувствуешь запах гари - замок расплавился. Ты остаешься 
                в оружейной лавке, пока наконец готоны не взрывают 
                корабль выстрелом со своего судна и ты не умираешь.
                """))
            return 'death'



class TheBridge(Scene):

    def enter(self):
        print(dedent("""
            Ты вбегаешь в топливный отсек с нейтронной бомбой и видишь 
            пятерых готонов, безуспешно пытающихся управлять кораблем. 
            Один уродливее другого и все в клоунских костюмах, как и готон, 
            убитый тобой. Они не достают оружие, так как видят бомбу в твоих 
            руках и не хотят, чтобы ты взорвал ее. Преимущество явно на твоей 
            стороне.
            """))

        action = input("> ")

        if action == "бросить бомбу":
            print(dedent("""
                Ты в панике активируешь бомбу и бросаешь ее в толпу готонов, 
                а затем прыгаешь к двери шлюза.  Сразу после этого 
                один из готонов стреляет тебе в спину. Умирая, 
                ты видишь, как другие готоны тщетно пытаются деактивировать 
                бомбу. Ты осознаешь, что готоны тоже погибнут. 
                Свет меркнет перед глазами.
                """))
            return 'death'

        elif action == "установить бомбу":
            print(dedent("""
                Ты указываешь бластером на бомбу в своих руках. 
                Готоны поднимают лапы вверх и в страхе потеют. 
                Ты осторожно, не отворачиваясь, подходишь к двери и 
                аккуратно устанавливаешь бомбу, держа готонов на мушке. 
                Ты запрыгиваешь в шлюз и закрываешь ее ударом по кнопке, 
                а затем бластером расплавляешь замок, чтобы готоны не смогли 
                открыть дверь. Теперь тебе нужно залезть в спасательную капсулу 
                и удрать с корабля к чертям собачьим.
                """))

            return 'escape_pod'
        else:
            print("ТАК НЕЛЬЗЯ ПОСТУПИТЬ!")
            return "the_bridge"


class EscapePod(Scene):

    def enter(self):
        print(dedent("""
            Ты мчишься по отсеку со спасательными капсулами. Некоторые из них 
            могут быть повреждены и взорвутся во время полета. Всего капсул 
            пять и у тебя нет времени, чтобы осматривать каждую из них 
            на отсутствие повреждений. 
            Задумавшись на секунду, ты решаешь сесть в капсулу под 
            номером...
            Капсулу под каким номером ты выбираешь?"
            """))

        good_pod = randint(1,5)
        guess = input("[pod #]> ")


        if int(guess) != good_pod:
            print(dedent("""
                Ты запрыгиваешь в капсулу номер {guess} и нажимаешь кнопку 
                отстыковки. Капсула вылетает в космическое пространство, а затем 
                взрывается с яркой вспышкой, разбрасывая осколки. 
                Ты умираешь.
                """))
            return 'death'
        else:
            print(dedent("""
                Ты запрыгиваешь в капсулу номер {guess} и нажимаешь кнопку
                отстыковки. Капсула вылетает в космическое пространство, а затем 
                отправляется к планете неподалеку. Ты смотришь в иллюминатор и 
                видишь, как ваш корабль взрывается. Его осколки повреждают 
                топливный отсек корабля готонов и тот тоже разлетается в клочья. 
                Победа за вами!"
                """))

            return 'finished'

class Exit_of_the_dungeon(Scene):

    def enter(self):
        print("Вы выбрались из подземелья! Так держать!")
        return 'finished'


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
        
        
class Map(object):

    scenes = {
        'entrance': Entrance_of_the_dungeon(),
        'laser_weapon_armory': LaserWeaponArmory(),
        'the_bridge': TheBridge(),
        'escape_pod': EscapePod(),
        'death': Death(),
        'finished': Exit_of_the_dungeon(),
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene

    def next_scene(self, scene_name):
        val = Map.scenes.get(scene_name)
        return val

    def opening_scene(self):
        return self.next_scene(self.start_scene)

a_map = Map('central_corridor')
a_game = Engine(a_map)
a_game.play()