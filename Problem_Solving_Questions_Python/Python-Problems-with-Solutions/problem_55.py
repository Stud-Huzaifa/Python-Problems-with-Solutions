'''Write a program to print third, fifth and seventh element from a list using enumerate
function'''

l = [10, 20, 30, 40, 50, 60, 70, 80, 90]
for i,item in  enumerate(l):
  if i == 2 or  i == 5 or i == 6:
      print(item)
