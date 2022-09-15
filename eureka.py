mass = float(input('Podaj masę w Kg: '))
volume = float(input('Podaj objętość w m3: '))


def density(mass: float, volume: float):
    dens = mass / volume
    return dens


print(density(mass, volume))