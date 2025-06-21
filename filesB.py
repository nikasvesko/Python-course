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
#counts lines
#reading the whole file
fhand= open("mbox-short.txt")
inp= fhand.read()
print(len(inp)) #says how many characters
print(inp[:20])
#first 20 characters

#searching through files
fhand= open("mbox-short.txt")
for line in fhand:
  if line.startswith("From:"):
    print(line)

#what are blank lines-> newlines, print statement adds newline to each line

#how to fix it
fhand=open("mbox-short.txt")
for line in fhand:
  line=line.rstrip() #this is fix, newline is considered white space
  if line.startswith("from:"):
    print(line)

#skipping with continue
fhand= open ("mbox-short.txt")
for line in fhand:
  line=line.rstrip() 
  if not line.startswith("from:"):
    continue #skip a line
    print(line)

fhand= open ("mbox-short.txt")
for line in fhand:
  line=line.rstrip() 
  if not "@uct.ac.za" in line: #selection criteria
    continue
  print(line)
  
#prompt for file name is fname

#if you dont put quit its going to blow up, we have to put it so there wont be any traceback






