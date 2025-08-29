# Importing packages

import math

import pygame

import calc_forces

# Setting

pygame.init()
screen = pygame.display.set_mode((1000, 1000))
clock = pygame.time.Clock()
font = pygame.font.SysFont("Arial", 16)

# Constants
G = 6.674e-11
scale = 80 / 1.496e11  # scale meters to pixels


# Creating planets

class Planet:
    def __init__(self, x, y, vx, vy, mass, radius, color, sun=False, planet_name=""):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.mass = mass
        self.radius = radius
        self.color = color
        self.sun = sun
        self.planet_name = planet_name
        self.orbit = []
        self.distance_traveled = 0
        self.last_position = (x, y)

    def update(self, fx, fy, difftime):
        ax = fx / self.mass
        ay = fy / self.mass
        self.vx += ax * difftime
        self.vy += ay * difftime
        new_x = self.x + self.vx * difftime
        new_y = self.y + self.vy * difftime

        # calculate distance traveled
        dx = new_x - self.x
        dy = new_y - self.y
        self.distance_traveled += math.sqrt(dx ** 2 + dy ** 2)

        self.x = new_x
        self.y = new_y

        if len(self.orbit) > 1000:
            self.orbit.pop(0)
        self.orbit.append((self.x, self.y))

    def draw(self, screen, offset_x, offset_y, scale, font):
        if len(self.orbit) > 1:
            scaled_points = [
                (int(x * scale + offset_x), int(y * scale + offset_y))
                for x, y in self.orbit
            ]
            pygame.draw.lines(screen, (255, 255, 255), False, scaled_points, 1)

        px = int(self.x * scale + offset_x)
        py = int(self.y * scale + offset_y)
        pygame.draw.circle(screen, self.color, (px, py), self.radius)

        # Draw the name
        if self.planet_name:
            name_text = font.render(self.planet_name, True, (255, 255, 255))
            screen.blit(name_text, (px + 10, py))

        # Draw the distance in miles
        km = self.distance_traveled / 1000
        distance_text = font.render(f"{km:,.0f} km", True, (255, 255, 255))
        screen.blit(distance_text, (px + 10, py + 20))


# The planets

sun = Planet(
    calc_forces.sun['x'],
    calc_forces.sun['y'],
    0,
    0,
    calc_forces.sun['mass'],
    calc_forces.sun['radius'],
    calc_forces.sun['color'],
    sun=True,
planet_name="Sun")

mercury = Planet(calc_forces.mercury['x'],
                 calc_forces.mercury['y'],
                 0,
                 calc_forces.velocity_mercury,
                 calc_forces.mercury['mass'],
                 calc_forces.mercury['radius'],
                 calc_forces.mercury['color'],
                 False,
                 "Mercury")

venus = Planet(calc_forces.venus['x'],
               calc_forces.venus['y'],
               0,
               calc_forces.velocity_venus,
               calc_forces.venus['mass'],
               calc_forces.venus['radius'],
               calc_forces.venus['color'],
               False,
               "Venus")


earth = Planet(calc_forces.earth['x'],
               calc_forces.earth['y'],
               0,
               calc_forces.velocity_earth,
               calc_forces.earth['mass'],
               calc_forces.earth['radius'],
               calc_forces.earth['color'],
               planet_name="Earth")

mars = Planet(calc_forces.mars['x'],
              calc_forces.mars['y'],
              0,
              calc_forces.velocity_mars,
              calc_forces.mars['mass'],
              calc_forces.mars['radius'],
              calc_forces.mars['color'],
              False,
              "Mars")

jupiter = Planet(calc_forces.jupiter['x'],
                 calc_forces.jupiter['y'],
                 0,
                 calc_forces.velocity_jupiter,
                 calc_forces.jupiter['mass'],
                 calc_forces.jupiter['radius'],
                 calc_forces.jupiter['color'],
                 False,
                 "Jupiter")


bodies = [sun, mercury, earth, venus, mars, jupiter]
# Running the game

def calculating_forces(sun, planet):
    dx_sun_planet = sun.x - planet.x
    dy_sun_planet = sun.y - planet.y
    distance_sun_planet = math.sqrt(dx_sun_planet ** 2 + dy_sun_planet ** 2)
    force = G * sun.mass * planet.mass / distance_sun_planet ** 2
    fx = force * dx_sun_planet / distance_sun_planet
    fy = force * dy_sun_planet / distance_sun_planet
    planet.update(fx, fy, time)

def calculating_distance_earth_jupiter(earth, jupiter):
    dx_earth_jupiter = earth.x - jupiter.x
    dy_earth_jupiter = earth.y - jupiter.y
    distance_earth_jupiter = math.sqrt(dx_earth_jupiter ** 2 + dy_earth_jupiter ** 2)
    return distance_earth_jupiter

def draw_line_between_planets(planet1, planet2):
    planet1_px = int(planet1.x * scale) + 500
    planet1_py = int(planet1.y * scale) + 500

    planet2_px = int(planet2.x * scale) + 500
    planet2_py = int(planet2.y * scale) + 500

    pygame.draw.line(screen, (255, 255, 255), (planet1_px, planet1_py), (planet2_px, planet2_py), 1)

running = True
while running:
    time = 60*60*24 # Time for program set to 1 hour
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # For update
    # Mercury
    calculating_forces(sun, mercury)

    # Venus
    calculating_forces(sun, venus)

    # Earth
    calculating_forces(sun, earth)

    # Mars
    calculating_forces(sun, mars)

    # Jupiter
    calculating_forces(sun, jupiter)

    # distance_earth_jupiter = []
    # distance_earth_jupiter.append(calculating_distance_earth_jupiter(earth, jupiter))
    # distance_earth_jupiter.sort()
    # min_distance_earth_jupiter = distance_earth_jupiter[-1]
    # print(f"Best distance between Earth and Jupiter: {min_distance_earth_jupiter} m")
    #

    # draw_line_between_planets(earth, jupiter)
    for body in bodies:
        body.draw(screen, 500, 500, scale, font)


    pygame.display.flip()
    clock.tick(60)

pygame.quit()
