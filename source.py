print("user details")
a=input("enter name:")
b=int(input("enter phone:"))
source=int(input("enter the source:"))
destination=int(input("enter the destination"))
if source<0 or destination<0:
   print("give valid number")
   exit()
elif source==0 or destination==0:
  print("source and destination are not valid")
  exit()
else:
  dis=abs(destination-source)
  print("1.car\n 2.bike\n 3.bus\n")
  select=input()
  if select=="1.car":
    x=dis*4
    print(x)
  elif select=="2.bike":
    x=dis*3
    print(x)
  elif select=="3.bus":
    x=dis*4
    print(x)
  else:
    print("invalid")
  print(a,'\n',b,'\n',source,'\n',des,'\n',dis,'\n',x)
