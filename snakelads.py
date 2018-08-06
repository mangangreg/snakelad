import random
import time
import math

grid = [[None]*10]*10

# Set of empty squares, exluding 1 and 100
empty = set(range(2,100))

# Assign snakes
snakes = []
for x in range(7):
	a = random.choice(list(empty))

	row = math.floor(a/10)

	b = random.choice(list(empty.difference(grid[row])))

	empty.remove(a)
	empty.remove(b)
	
	snake = [a,b]
	snake.sort()
	snakes.append(snake)

print("Snakes:",snakes)

snake_heads = [x[1] for x in snakes]

ladders = []
for x in range(7):
	a = random.choice(list(empty))

	row = math.floor(a/10)

	b = random.choice(list(empty.difference(grid[row])))

	empty.remove(a)
	empty.remove(b)
	
	lad = [a,b]
	lad.sort()
	ladders.append(lad)

print("Ladders:",ladders)

ladder_tails = [x[0] for x in ladders]

# Game portion

position = 1
print('Starting at 1!')

count = 0

while position <100:
	count += 1
	
	# Roll the die
	die = random.randint(1,6)
	print("---")
	print("You rolled a %d." % die)	
	
	# Map out the old position and the 'move' position
	old = position
	move = position + die
	
	# If you go past 100, bounce back
	if move >100:
		
		move = 100 - move + 100

		print("Woah there! We're going to have to take you down a peg or two")
		print("You bounced from %d to %d and back to %d" % (old,100,move))
		

		pass

	# If you land on a snake head, fall down!
	if move in snake_heads:
		position = snakes[snake_heads.index(move)][0]
		print("Oh no, snake! Move from %s to %d and then drop down to %d." % (old,move,position))
	
	# If you land on a ladder tail, climb that sucker!
	elif move in ladder_tails:
		position = ladders[ladder_tails.index(move)][1]
		print("Yay ladder! Move from %d to %d and then climb to %d." % (old,move,position))

	# Else just do a normal move
	else:
		position = move
		print("Standard move, jump from %d to %d." % (old, position))



	#time.sleep(0.75)




print("---")
print('You win!')
print('[I mean you always win...]')
print('But you won it in %d moves!' % count)













# Assign ladders