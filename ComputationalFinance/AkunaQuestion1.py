def initial(low,high):
  counter = 0;
  for x in range(low,high+1):
    if recursion(x) is True:
      counter += 1;
  return counter;

def recursion(targetnumber):
  flag = True;
  currentnumber = targetnumber
  while currentnumber  != 1:
    if currentnumber % 3 == 0:
      currentnumber = currentnumber/3
    elif currentnumber % 5 == 0:
      currentnumber = currentnumber/5
    else:
      return False;
  return flag;

print(initial(1,15))
