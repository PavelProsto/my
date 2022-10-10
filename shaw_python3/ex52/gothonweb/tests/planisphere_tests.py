from nose.tools import *
from gothonweb.planisphere import *

def test_room():
    gold = Room("GoldRoom",
                """В этой комнате полно золота, которое можно украсть.
                Здесь есть дверь с выходом на север.""")
    assert_equal(gold.name, "GoldRoom")
    assert_equal(gold.paths, {})

def test_room_paths():
    center = Room("Center", "Тестирование центральной комнаты.")
    north = Room("North", "Тестирование северной комнаты.")
    south = Room("South", "Тестирование южной комнаты.")
   
    center.add_paths({'north': north, 'south': south})
    assert_equal(center.go('north'), north)
    assert_equal(center.go('south'), south)

def test_map():
    start = Room("Start", "Вы можете идти на запад и провалиться в яму.")
    west = Room("Trees", "Здесь есть деревья и вы можете отправиться на восток.")
    down = Room("Dungeon", "Здесь темно и вы можете подняться вверх.")

    start.add_paths({'west': west, 'down': down})
    west.add_paths({'east': start})
    down.add_paths({'up': start})

    assert_equal(start.go('west'), west)
    assert_equal(start.go('west').go('east'), start)
    assert_equal(start.go('down').go('up'), start)

def test_gothon_game_map():
    start_room = load_room(START)
    assert_equal(start_room.go('shoot!'), generic_death)
    assert_equal(start_room.go('dodge!'), generic_death)

    room = start_room.go('tell a joke')
    assert_equal(room, laser_weapon_armory)