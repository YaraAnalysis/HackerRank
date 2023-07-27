#Day 06 - Operators, Strings, and Loops

# Enter your code here. Read input from STDIN. Print output to STDOUT

t = int(input())
temp = []

for i in range(t):
  s = str(input())
  temp.append(s)

for i in range(len(temp)):
  print(temp[i][0::2] + ' ' + temp[i][1::2])
