#matching and extracting data
re.findall()
import re
x='My 2 fave numbers are 2 and 22'
y=re.findall('[0-9]+', x)
print(y)
#0-9 one or more digits
#it will print 0, 2 and 22
y=re.findall('[AEIOU]+',x)
print(y)
# it will print 1 list with no items innit

#greedy matching
#chooses largest overlap

#non-greedy matching
#if we add ? nece bit greedy, preferira kratki string

# \S+@\S+ 
#fine tuning extraxtion, at least one non whitespace character

#we wanna match from the beginning ... ^From (\S+@\S+)
#stavimo zagradu jer ne zelimo cijeli taj dio s from pa da omeđimo


