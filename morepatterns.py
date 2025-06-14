#summing in a loop
zork=0
print("before", zork)
for thing in [9,41, 12, 3, 74, 15] :
  zork=zork+ thing
  print(zork, thing)
print("after", zork)

#finding average in a loop

count= 0
sum = 0
print("before", count, sum)
for value in [19, 41, 12, 3, 74, 15] :
  count= count +1
  sum= sum+ value
  print(count, sum, value)
print("after", count, sum, sum/count)

#filtering in a loop
print("before")
for value in [19,41,12,3,74,15]:
  if value > 20:
    print("large number", value)
print("after")

#search using a Boolean variable
#if we just want to know is value was found
found= False
print("before", found)
for value in [19,41,12,3,74,15]:
  if value =3:
    found= True
  print(found, value)
print("after", found)

#how to find the smallest value
smallest_so_far = -1
print("before", smallest_so_far)
for the_num in [19,41,12,3,74,15]:
  if the_num < smallest_so_far:
    smallest_so_far = the_num
  print(smallest_so_far, the_num)
print("after", smallest_so_far)

#another way, with none
smallest = None
print("before")
for value in [19,41,12,3,74,15]:
  if smallest is None :
    smallest = value
  elif value < smallest:
    smallest= value
  print(smallest, value)
print("after", smallest)
 #we can do largest as well 

#the is and is not operators

#similar to ==, but stronger
#is not is also logical operator
#is on Booleans and none types




