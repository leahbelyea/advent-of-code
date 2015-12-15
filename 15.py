import itertools
import re

with open('input/15.txt', 'r') as f:
  input = [x.strip('\n') for x in f.readlines()]

# Organize ingredients
ingredients = []

for item in input:
  item = re.split(' ', item)

  ingredient = {}
  ingredient['name'] = item[0].replace(':', '')
  ingredient[item[1]] = int(item[2].replace(',', ''))
  ingredient[item[3]] = int(item[4].replace(',', ''))
  ingredient[item[5]] = int(item[6].replace(',', ''))
  ingredient[item[7]] = int(item[8].replace(',', ''))
  ingredient[item[9]] = int(item[10].replace(',', ''))
  ingredients.append(ingredient)

# Part 1
print 'Part 1'

quantities = range(0, 101)
qualities = ['capacity', 'durability', 'flavor', 'texture']

scores = []

for recipe in itertools.product(quantities, repeat=len(qualities)):
  if sum(recipe) != 100: continue

  capacity = 0
  durability = 0
  flavor = 0
  texture = 0

  for ingredient in ingredients:
    quantity = recipe[ingredients.index(ingredient)]
    capacity += ingredient['capacity'] * quantity
    durability += ingredient['durability'] * quantity
    flavor += ingredient['flavor'] * quantity
    texture += ingredient['texture'] * quantity

  capacity = capacity if capacity > 0 else 0
  durability = durability if durability > 0 else 0
  flavor = flavor if flavor > 0 else 0
  texture = texture if texture > 0 else 0

  scores.append(capacity * durability * flavor * texture)

print max(scores)

# Part 2
print '\nPart 2'

quantities = range(0, 101)
qualities = ['capacity', 'durability', 'flavor', 'texture']

scores = []

for recipe in itertools.product(quantities, repeat=len(qualities)):
  if sum(recipe) != 100: continue

  capacity = 0
  durability = 0
  flavor = 0
  texture = 0
  calories = 0

  for ingredient in ingredients:
    quantity = recipe[ingredients.index(ingredient)]
    capacity += ingredient['capacity'] * quantity
    durability += ingredient['durability'] * quantity
    flavor += ingredient['flavor'] * quantity
    texture += ingredient['texture'] * quantity
    calories += ingredient['calories'] * quantity

  if calories != 500: continue

  capacity = capacity if capacity > 0 else 0
  durability = durability if durability > 0 else 0
  flavor = flavor if flavor > 0 else 0
  texture = texture if texture > 0 else 0

  scores.append(capacity * durability * flavor * texture)

print max(scores)
