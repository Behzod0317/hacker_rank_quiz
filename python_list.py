# planets = ['Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus']
# planets[3] = 'Malacandra'
# planets.append('Pluto')

#print(planets[:-2])

# for planet in planets:
#     print(planet, end=' ')

# print(" ")

planets = ['Mercury', 'Venus', 'Earth', 'Mars', 'Jupiter', 'Saturn', 'Uranus', 'Neptune']
planet_to_initial = {planet: planet[-1] for planet in planets}
print(planet_to_initial,end=' ')
print()