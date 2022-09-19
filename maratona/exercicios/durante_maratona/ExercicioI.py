"""
Frodo was a little hobbit (small, hairy-footed people) who lived quietly in the Shire, taking his various breakfasts filled with many
succulent foods that a good hobbit diet provides. One day his Uncle Bilbo hands him his famous golden ring, and Gandalf, a very "cool"
mage, tells Frodo that this ring was not normal and should be thrown on the Mountain of Doom, so that a great evil would be avoided.
For this journey, an entourage was formed, composed of dwarves, elves, humans, hobbits and magicians. Frodo wants to know the amount
of each race that will go with him for the journey. Given a list of people who enlisted, report back to Frodo from the entourage.

Input
The first line of the entry is composed of an integer N(0 < N <= 10), indicating the number of people who enlisted.
Each of the next N Next lines are composed of a string (without spaces and of alphanumeric characters only) and a capital character,
indicating, respectively, the name and the type of the race of the respective being. This character may be:
● A - For dwarves; ● E - For elves; ● H - For humans; ● M - For magicians; ● X - For hobbits (X, because every hobbit is a mystery to the world).
Output A report should be presented with Frodo's entourage, indicating in each line how many beings of each species will be on the journey,
following the order: hobbits, humans, elves, dwarves and magicians (in Portuguese).

Input Sample:
9
Frodo X
Gandalf M
Pippin X
Sam X
Aragorn H
Legolas E
Gimli A
Boromir H
Merry X

.....

Output Sample:
4 Hobbit(s)
2 Humano(s)
1 Elfo(s)
1 Anao(oes)
1 Mago(s)
"""

linhas = int(input())

# vars
dwarves = 0
elves = 0
humans = 0
magicians = 0
hobbits = 0
animal = []

# code
for num in range(0,linhas):
    linha = input()
    animal = linha.split(' ', 1)
    if(animal[1] == 'A'): #dwarves
      dwarves = dwarves + 1
    elif( animal[1] == "E"): #elves
      elves = elves + 1
    elif( animal[1] == 'H'): #humans
      humans = humans + 1
    elif( animal[1] == 'M'): #magicians
      magicians = magicians + 1
    elif( animal[1] == 'X'): #hobbits
      hobbits = hobbits + 1

# saida

print( str(hobbits) + ' Hobbit(s)')
print( str(humans) + ' Humano(s)')
print( str(elves) + ' Elfo(s)')
print( str(dwarves) + ' Anao(oes)')
print( str(magicians) + ' Mago(s)')