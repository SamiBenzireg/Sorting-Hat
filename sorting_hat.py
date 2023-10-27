gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0

 # Question 1
print('Q1) Do you like Dawn or Dusk?')

print('  1) Dawn')
print('  2) Dusk')

answer = int(input('Enter answer (1-2): '))

if answer == 1:
  gryffindor +=1
  ravenclaw +=1
elif answer == 2:
  hufflepuff +=1
  slytherin +=1
else:
  print("Wrong input.")

# Question 2
print("q2) When im dead, i want people to remember me as:")

print("1) the good")
print("2) the Great")
print("3) the Wise")
print("4) the Bold")

answer = int(input("Enter answer (1-4): "))

if answer == 1:
  hufflepuff +=2
elif answer == 2:
  slytherin += 2
elif answer == 3:
  ravenclaw += 2
elif answer == 4:
  gryffindor  += 2
else:
  print("Wrong input.")

# Question 3

print("q3) which kind of instrument most pleases your ear? ")

print("1) The violin")
print("2) The trumpet")
print("3) The piano")
print("4) The drum")

answer = int(input("Enter answer (1-4)"))

if answer == 1:
  slytherin +=4
elif answer == 2:
  hufflepuff += 4
elif answer == 3:
  ravenclaw += 4
elif answer == 4:
  gryffindor += 4
else:
  print("Wrong input.")

print("gryffindor: ", gryffindor)
print("ravenclaw: ", ravenclaw)
print("Hufflepuff: ", hufflepuff)
print("Slytherin: ", slytherin)

most_points = max(gryffindor, ravenclaw, hufflepuff, slytherin)

if gryffindor == most_points:
  print("🦁 Gryffindor")
if ravenclaw == most_points:
  print("🦅 Ravenclaw")
if hufflepuff == most_points:
  print("🦡 Hufflepuff")
if slytherin == most_points:
  print("🐍 Slytherin")





