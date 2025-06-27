#regular expressions
#"wild" card
#very old programming language
# ^ npr. matches beginning of a line
re.search() # to see if string matches a regular expression

hand=open('mbox-short.txt')
for line in hand:
  line=line.rstrip()
  if line.find('From:') >=0:
    print(line)

import re  
hand=open('mbox-short.txt')
for line in hand:
  line=line.rstrip()
  if re.search('From:', line :
    print(line)
#fine tunning

#mozemo koristiti re.search umjesto startswith 
#re.search('^From:', line)
#beggining of line, ne moramo pisati startswith

#dot matches any character
#a line that starts with X itself
#kako biti jasniji sto zelis da matcha sto ne
X-blabla: CMU
X-haha: ne
X-napravis razmak: Ne


