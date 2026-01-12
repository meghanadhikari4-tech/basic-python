friends=['meghan','megha','megg','regg','egg']
friends[1]='lila'
print(friends[1])
print(friends)
print(friends[0])
print(friends[1:3])
friends.append('gigi')
print(friends)
friends.insert(2,'rihana')
print(friends)
#removes the last element
friends.pop()
print(friends)
#to check if name is there
print(friends.index('megg'))
game=['football','baseball','cricket','baseball','baseball']
print(game.count('baseball'))