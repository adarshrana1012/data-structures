t=input("enter the text:")
v=[]
v.append(t)
h=t
undo=[]
redo=[]
undoh=[]
redoh=[]
print("press 1 for make changes")
print("press 2 for undo")
print("press 3 for redo")
print("press 4 for save document")
print("press 5 for undo history")
print("print 6 for redo history")
print("print 7 for all version")
print("print 8 for original version")
print("print 9 for exit")
ch=int(input("enter choice:"))

f=True
while(f):
  if(ch==1):
    undo.append(t)
    undoh.append(t)
    t=input("enter the changes=")
    v.append(t)
    redo.clear()
    print(t)
  elif(ch==2):
    if(len(undo)>0):
     redo.append(t)
     redoh.append(t)
     t=undo[-1]
     v.append(t)
     undo.pop()
     print(t)
    else :
      print("nothing to undo")
  elif(ch==3):
    if(len(redo)>0):
     undo.append(t)
     undoh.append(t)
     t=redo[-1]
     v.append(t)
     redo.pop()
     print(t)
    else:
     print("nothing to redo")
  elif (ch==4):
      undo.clear()
      redo.clear()
  elif(ch==5):
     print(undoh)
  elif(ch==6):
     print(redoh)
  elif(ch==7):
    print(v)
  elif(ch==8):
    print(h)
  else:
    break
  ch=int(input("enter choice"))
  
print(t)