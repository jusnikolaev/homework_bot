import datetime
from ephem import *

PLANETS = {
    'mercury': Mercury,
    'venus': Venus,
    'mars': Mars,
    'jupiter': Jupiter,
    'saturn': Saturn,
    'uranus': Uranus,
    'neptune': Neptune
}


# Функция вычисления созвездия
def planet_constellation(planet):
    date = datetime.datetime.now()
    curr_date = date.strftime('%Y/%m/%d')
    if planet not in PLANETS:
        return "Sry...I dont know"
    else:
        planet_constll = PLANETS[planet]
        return constellation(planet_constll(str(curr_date)))


# Функция вычисления положения планеты
def planet_position(planet):
    date = datetime.datetime.now()
    curr_date = date.strftime('%Y/%m/%d')
    if planet in PLANETS:
        planet_ctor = PLANETS[planet]
        planet_pos = planet_ctor()
        planet_pos.compute(curr_date)
        return planet_pos
    else:
        return None


