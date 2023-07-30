#Day 8 - solution 2 - Phone a Friend

n = int(input())

phone_book = {}

for i in range(n):
  contact = input().split()
  phone_book[contact[0]] = contact[1]

#print(phone_book)

for i in range(n):
  try:
    name = str(input())
    if name in phone_book:
      print(name + '=' + phone_book[name])
    else:
      print('Not found')
  except:
    break