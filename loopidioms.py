#smart loops
#looping through a set

print("before")
for thing in [9,41,12,3,74,15]:
  print(thing)
print("after")

#what is the largest number
largest_so_far =-1
print("before",largest_so_far)
for the_num in [9,41,12,3,74,15]:
  if the_num > largest_so_far:
    largest_so_far=the_num
  print(largest_so_far, the_num)
print("after", largest_so_far)

#samo mijenja po redu kako ide

    
