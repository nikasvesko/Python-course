xfile=open("mbox.txt")
for cheese in xfile:
  print(cheese)

fhand=open("mbox.txt")
count=0
for line in fhand:
  count= count+1
print("Line Count:", count)

$python open.py
#Line Count: 132045
