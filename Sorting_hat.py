#The Sorting Hat is a magical talking hat at Hogwarts School of Witchcraft and Wizardry. 
#The hat decides which of the four "Houses" each first-year student goes to:
#🦁 Gryffindor
#🦅 Ravenclaw
#🦡 Hufflepuff
#🐍 Slytherin


Gryffindor = 0
Ravenclaw = 0
Hufflepuff = 0
Slytherin = 0

print("*****************")
print("***Sorting Hat***")
print("*****************")

print("Q1) Do you like Dawn or Dusk?") 
print("1) Dawn")
print("2) Dusk")

answer_1 = int(input("Enter number (1-2):")) 

if answer_1 == 1:
  Gryffindor =+ 1
  Ravenclaw =+ 1
elif answer_1 == 2:
  Hufflepuff =+ 1
  Slytherin =+ 1
else:
  print("Wrong input") 

print("Q2) When I’m dead, I want people to remember me as:")
print("1) The Good")
print("2) The Great")
print("3) The Wise")
print("4) The Bold")

answer_2 = int(input("Enter number (1-4):"))

if answer_2 == 1:
  Hufflepuff =+ 2 
elif answer_2 == 2:
  Slytherin =+ 2 
elif answer_2 == 3:
  Ravenclaw +2
elif answer_2 == 4:
  Gryffindor =+ 2
else:
  print("Wrong input")

print("Q3) Which kind of instrument most pleases your ear?")
print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer_3 = int(input("Enter number (1-4):"))

if answer_3 == 1:
  Slytherin += 4
elif answer_3 == 2:
  Hufflepuff += 4
elif answer_3 == 3:
  Ravenclaw +=4
elif answer_3 == 4:
  Gryffindor += 4
else:
  print('Wrong input.')

print('Gryffindor',Gryffindor)
print('Slytherin',Slytherin)
print('Hufflepuff',Hufflepuff)
print('Ravenclaw',Ravenclaw)

most_points = max(Gryffindor,Hufflepuff,Ravenclaw,Slytherin)

if most_points == Gryffindor:
  print('🦁 Gryffindor')
elif most_points == Slytherin:
  print('🐍 Slytherin')
elif most_points == Hufflepuff:
  print('🦡 Hufflepuff')
else:
  print('🦅 Ravenclaw')
