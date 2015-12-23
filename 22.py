# effects take place before start of players turn. so boss can die before player buys spell.

import random

spells = [
  {'name': 'Magic Missile', 'cost': 53, 'damage': 4, 'armor': 0, 'heals': 0, 'mana': 0, 'turns': 1},
  {'name': 'Drain', 'cost': 73, 'damage': 2, 'armor': 0, 'heals': 2, 'mana': 0, 'turns': 1},
  {'name': 'Shield', 'cost': 113, 'damage': 0, 'armor': 7, 'heals': 0, 'mana': 0, 'turns': 6},
  {'name': 'Poison', 'cost': 173, 'damage': 3, 'armor': 0, 'heals': 0, 'mana': 0, 'turns': 6},
  {'name': 'Recharge', 'cost': 229, 'damage': 0, 'armor': 0, 'heals': 0, 'mana': 101, 'turns': 5}
]

def isActive(activeSpells, spell):
  for activeSpell in activeSpells:
    if spell['name'] == activeSpell['name'] and activeSpell['turns'] > 1:
      return True
  return False

def getValidSpell(activeSpells, mana, spells):
  counter = 0
  while True:
    isValid = True
    spell = random.choice(spells)

    if mana - spell['cost'] < 0 or isActive(activeSpells, spell):
      isValid = False
    if isValid:
      return dict(spell)
    if counter > 100:
      return None
    counter += 1

def playGame(boss, player, spells, hard):
  activeSpells = []
  manaSpent = 0
  gameTranscript = ''

  gameTranscript += '\n' + str(player) + '\n'
  gameTranscript += str(boss) + '\n'

  while True:

    if hard:
      player['hp'] -= 1
      if player['hp'] < 1:
        gameTranscript += 'Player loses\n'
        return (None, gameTranscript)

    armor = 0
    newSpell = getValidSpell(activeSpells, player['mana'], spells)
    if newSpell != None:
      activeSpells.append(newSpell)
      manaSpent += newSpell['cost']
      player['mana'] -= newSpell['cost']
      gameTranscript += 'Player casts {}\n'.format(newSpell['name'])

    for spell in activeSpells:
      if spell['turns'] > 0:
        armor += spell['armor']
        player['hp'] += spell['heals']
        player['mana'] += spell['mana']
        boss['hp'] -= spell['damage']

        spell['turns'] -= 1
        gameTranscript += '{}: turns left = {}\n'.format(spell['name'], spell['turns'])

    if boss['hp'] < 1:
      gameTranscript += 'Player wins\n'
      return (manaSpent, gameTranscript)

    playerDamage = boss['damage'] - armor if boss['damage'] - armor > 1 else 1
    player['hp'] -= playerDamage

    gameTranscript += '\n' + str(player) + '\n'
    gameTranscript += str(boss) + '\n'

    if player['hp'] < 1:
      gameTranscript += 'Player loses\n'
      return (None, gameTranscript)

      gameTranscript += '\n\n\n'

# Part 1
print 'Part 1'

manas = []
simTimes = 10000


for i in range(simTimes):
  boss = {
    'hp': 55,
    'damage': 8
  }

  player = {
    'hp': 50,
    'mana': 500
  }

  result = playGame(boss, player, spells, False)
  mana = result[0]
  if mana != None:
    manas.append(mana)

print min(manas)

# Part 2
print '\nPart 2'

manas = []
simTimes = 10000
for i in range(simTimes):
  boss = {
    'hp': 55,
    'damage': 8
  }

  player = {
    'hp': 50,
    'mana': 500
  }

  result = playGame(boss, player, spells, True)
  mana = result[0]
  if mana != None:
    manas.append(mana)
  # if mana == 953:
  #   print result[1]
  #   print '\n\n\n\n\n\n'

print min(manas)



