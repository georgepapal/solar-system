import math

# Important values
G = 6.674e-11


sun = {
    'x': 0,
    'y': 0,
    'mass': 1.989e30,
    'radius': 20,
    'color': (255, 230, 0)
}

mercury = {
    'x': 5.791e10,
    'y': 0,
    'mass': 3.3011e23,
    'radius': 5,
    'color': (102, 194, 255)
}

venus = {
    'x': 108.2e9,
    'y': 0,
    'mass': 4.8675e24,
    'radius': 8,
    'color': (77, 15, 22)
}

earth = {
    'x': 1.5193e11,
    'y': 0,
    'mass': 5.974e24,
    'radius': 10,
    'color': (0, 100, 255)
}

mars = {
    'x': 247.93e9,
    'y': 0,
    'mass': 6.4171e23,
    'radius': 6,
    'color': (255, 0, 0)
}

jupiter = {
    'x': 768.59e9,
    'y': 0,
    'mass': 1.898e27,
    'radius': 16,
    'color': (201, 144, 57)
}

# Calculating velocity of mercury -----------------------------------------------------------------
distance_sun_mercury = mercury['x']
velocity_mercury = math.sqrt(G * sun['mass'] / distance_sun_mercury)

# Calculating velocity of venus ------------------------------------------------------------------
distance_sun_venus = venus['x']
velocity_venus = math.sqrt(G * sun['mass'] / distance_sun_venus)

# Calculating velocity of earth ------------------------------------------------------------------
distance_sun_earth = earth['x']
velocity_earth = math.sqrt(G * sun['mass'] / distance_sun_earth)

# Calculating velocity of mars -------------------------------------------------------------------
distance_sun_mars = mars['x']
velocity_mars = math.sqrt(G * sun['mass'] / distance_sun_mars)

# Calculating velocity of jupiter
distance_sun_jupiter = jupiter['x']
velocity_jupiter = math.sqrt(G * sun['mass'] / distance_sun_jupiter)

print(velocity_mercury)
print(velocity_venus)
print(velocity_earth)
print(velocity_mars)
print(velocity_jupiter)
