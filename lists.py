# random
import random

my_randoms = list()
for i in range(10):
    my_randoms.append(random.randrange(1, 6))
print(my_randoms)

# Generate a list of numbers 1..10
numbers_1_to_10 = list(range(1, 11))

# Iterate from 1 to 10
for number in numbers_1_to_10:
    # Iterate your random number list here
    message = f'{number} is contained in the random list' if number in my_randoms else f'{number} is not contained in the random list'

    print(message)

# planets
planet_list = ["Mercury", "Mars"]
planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
planet_list.append("Pluto")
print(planet_list)

rocky_planets = planet_list[0:4]
print(rocky_planets)

del planet_list[-1]
print(planet_list)