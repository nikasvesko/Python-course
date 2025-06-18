#reading files
#file processing
#a file can be bunch of lines

#to read a file
open()function

handle=open(filename, mode)
#mode is optional and it should be r 

fhand= open("mbox.txt")
print(fhand)

#when files are missing we get a traceback

stuff= "hello\nWorld!" #backslash n means new line
stuff
#it wil display "hello\nWorld!"
print(stuff)
#it will display Hello in one line, and World! in other
stuff= "X\nY"
#X u jednom redu, Y u drugom
len(stuff)
#its 3
#a text file has newlines at the end of each line

