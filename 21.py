import itertools

# Part 1
print 'Part 1'

# Add (0, 0, 0) to armor and rings so the combinations include choosing "nothing"
store = {
  'weapons': [(8, 4, 0), (10, 5, 0), (25, 6, 0), (40, 7, 0), (74, 8, 0)],
  'armor': [(13, 0, 1), (31, 0, 2), (53, 0, 3), (75, 0, 4), (102, 0, 5), (0, 0, 0)],
  'rings': [(25, 1, 0), (50, 2, 0), (100, 3, 0), (20, 0, 1), (40, 0, 2), (80, 0, 3), (0, 0, 0), (0, 0, 0)]
}

boss = {
  'Hit Points': 109,
  'Damage': 8,
  'Armor': 2
}

def playGame(player, boss):
  bossPoints = boss['Hit Points']
  playerPoints = player['Hit Points']
  while True:
    playerAttack = player['Damage'] - boss['Armor'] if player['Damage'] - boss['Armor'] > 0 else 1
    bossPoints -= playerAttack
    if bossPoints <= 0:
      return True

    bossAttack = boss['Damage'] - player['Armor'] if boss['Damage'] - player['Armor'] > 0 else 1
    playerPoints -= bossAttack
    if playerPoints <= 0:
      return False

combinations = {
  'weapons': store['weapons'],
  'armor': store['armor'],
  'rings': list(itertools.combinations(store['rings'], 2))
}

products = itertools.product(range(len(combinations['weapons'])), range(len(combinations['armor'])), range(len(combinations['rings'])));

playerCombos = []

for product in products:
  items = {
    'weapon': combinations['weapons'][product[0]],
    'armor': combinations['armor'][product[1]],
    'ring1': combinations['rings'][product[2]][0],
    'ring2': combinations['rings'][product[2]][1]
  }

  cost = items['weapon'][0] + items['armor'][0] + items['ring1'][0] + items['ring2'][0]
  damage = items['weapon'][1] + items['armor'][1] + items['ring1'][1] + items['ring2'][1]
  armor = items['weapon'][2] + items['armor'][2] + items['ring1'][2] + items['ring2'][2]

  playerCombos.append((cost, damage, armor))

playerCombos = sorted(playerCombos, key=lambda combo: combo[0])

for combo in playerCombos:
  player = {
    'Hit Points': 100,
    'Damage': combo[1],
    'Armor': combo[2]
  }
  playerWins = playGame(player, boss)

  if playerWins:
    print combo[0]
    break

# Part 2
print '\nPart 2'

playerCombos = sorted(playerCombos, key=lambda combo: combo[0], reverse=True)

for combo in playerCombos:
  player = {
    'Hit Points': 100,
    'Damage': combo[1],
    'Armor': combo[2]
  }
  playerLoses = not playGame(player, boss)

  if playerLoses:
    print combo[0]
    break
