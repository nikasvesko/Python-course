#a string is a sequence of characters
#positions of letters start at zero

fruit="banana"
letter= fruit[1]
print(letter)
#bit ce a

x=3
w=fruit[x-1]
print(w)

fruit="banana"
print(len(fruit))
#length function

fruit="banana"
index=0
while index < len(fruit):
  letter=fruit[index]
  print(index, letter)
  index= index+1
#izaci ce od 0-5 i slova pripadajuca pored

fruit="banana"
for letter in fruit:
  print(letter)
#ispisat ce banana, slovo po slovo, kraći code

word="banana"
count=0
for letter in word:
  if letter== "a" :
    count=count+1
print(count)

#onaj zad dolje npr. koristi n u banana, a ne letter




