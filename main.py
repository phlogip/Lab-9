def encoder(password):
  list = []
  for number in password:
    if int(number)+3 >= 7:
      list.append(int(number)-7)
    else:
      list.append(int(number)+3)
  return list
