import random
import copy

class Player:
  def __init__(self, hp, mana):
    self.hp = hp
    self.mana = mana
    self.armor = 0
    self.manaSpent = 0

  def __str__(self):
    return 'hp: {}, mana: {}'.format(self.hp, self.mana)

class Boss:
  def __init__(self, hp, damage):
    self.hp = hp
    self.damage = damage

  def __str__(self):
    return 'hp: {}'.format(self.hp)

class Spell:
  def __init__(self, name, cost, damage, armor, heals, mana, turns):
    self.name = name
    self.cost = cost
    self.damage = damage
    self.armor = armor
    self.heals = heals
    self.mana = mana
    self.turns = turns

  def __str__(self):
    return 'name: {}, cost: {}, damage: {}, armor: {}, heals: {}, mana: {}, turns: {}'.format(self.name, self.cost, self.damage, self.armor, self.heals, self.mana, self.turns)

class Game:
  def __init__(self, spells, player, boss, hard = False):
    self.spells = spells
    self.player = player
    self.boss = boss
    self.executedSpells = []
    self.transcript = ''
    self.hard = hard

  def play(self, verbose = False):
    self.transcript += '\nStart Game\n'
    self.transcript += self.getStats()

    while True:
      self.doPlayerTurn()
      if self.gameOver():
        self.transcript += '\n\nGame Over\n\n'
        break
      self.doBossTurn()
      if self.gameOver():
        self.transcript += '\n\nGame Over\n\n'
        break

    if verbose:
      print self.transcript

  def doPlayerTurn(self):
    self.transcript += '\n\n--- Player Turn ---\n'

    # Hard mode
    if self.hard:
      self.player.hp -= 1

    # Check game over
    if self.gameOver(): return

    # Reset armor
    self.player.armor = 0

    # Apply effects
    self.applyEffects()

    # Check game over
    if self.gameOver(): return

    # Pick spell
    spell = self.getValidSpell()

    # Execute spell and add to executedSpells
    if spell is not None:
      self.transcript += 'Player executes {}\n'.format(spell.name)
      if spell.turns == 1:
        self.executeSpell(spell)
      self.executedSpells.append(spell)
      self.player.manaSpent += spell.cost
      self.player.mana -= spell.cost

    self.transcript += self.getStats()

  def doBossTurn(self):
    self.transcript += '\n\n--- Boss Turn ---\n'

    # Reset armor
    self.player.armor = 0

    # Apply effects
    self.applyEffects()

    # Check game over
    if self.gameOver(): return

    # Attack
    playerDamage = boss.damage - self.player.armor if boss.damage - self.player.armor > 1 else 1
    player.hp -= playerDamage
    self.transcript += 'Boss attacks for {} - {} = {} damage\n'.format(self.boss.damage, self.player.armor, playerDamage)

    self.transcript += self.getStats()

  def applyEffects(self):
    self.transcript += ':: Applying effects\n'
    for spell in self.executedSpells:
      if spell.turns > 0:
        self.executeSpell(spell)
        self.transcript += 'Effect {} executed. {} turns remaining.\n'.format(spell.name, spell.turns)
    self.transcript += ':: End effects\n'

  def executeSpell(self, spell):
    self.player.armor += spell.armor
    self.player.hp += spell.heals
    self.player.mana += spell.mana
    self.boss.hp -= spell.damage

    spell.turns -= 1

  def gameOver(self):
    if self.player.hp < 1:
      return True
    elif self.boss.hp < 1:
      return True
    return False

  def getStats(self):
    return 'player - {}\nboss - {}\n'.format(player, boss)

  def getValidSpell(self):
    counter = 0
    while True:
      isValid = True
      spell = random.choice(self.spells)

      if self.player.mana - spell.cost < 0 or self.isActive(spell):
        isValid = False
      if isValid:
        return copy.deepcopy(spell)
      if counter > 100:
        return None
      counter += 1

  def isActive(self, spell):
    for activeSpell in self.executedSpells:
      if spell.name == activeSpell.name and activeSpell.turns > 0:
        return True
    return False

  def getManaSpent(self):
    return self.player.manaSpent

  def playerWon(self):
    if player.hp > boss.hp:
      return True
    return False

spells = [
  Spell('Magic Missile', 53, 4, 0, 0, 0, 1),
  Spell('Drain', 73, 2, 0, 2, 0, 1),
  Spell('Shield', 113, 0, 7, 0, 0, 6),
  Spell('Poison', 173, 3, 0, 0, 0, 6),
  Spell('Recharge', 229, 0, 0, 0, 101, 5)
]

# Part 1
print 'Part 1'

manas = []
for i in range(10000):
  player = Player(50, 500)
  boss = Boss(55, 8)
  game = Game(spells, player, boss)
  game.play()
  if game.playerWon(): manas.append(game.getManaSpent())

print min(manas)

# Part 2
print '\nPart 2'

manas = []
for i in range(10000):
  player = Player(50, 500)
  boss = Boss(55, 8)
  game = Game(spells, player, boss, True)
  game.play()
  if game.playerWon(): manas.append(game.getManaSpent())

print min(manas)
