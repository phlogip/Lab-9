def encoder(password):
  new_pass = ''
  for number in password:
    if int(number) >= 7:
      new_pass += str((int(number)-7))
    else:
      new_pass += str((int(number)+3))
  return new_pass
  
def Decode(input):
  new_pass = ''
  for i in range(len(input)):
    if input[i] <= 2:
      new_pass += input[i] + 7
    else:
      new_pass += input[i] - 3
  return [new_pass, input]

def menu():
  print("Menu\n
        -------------\n
        1. Encode\n
        2. Decode\n
        3. Quit")

def main():
  while True:
    menu()
    option = input("Please enter an option: )
    if option == 1:
      pw = str(input("Please enter your password to encode: ))
      encoded_pw = encoder(pw)
      print("Your password has been encoded and stored!")
    if option == 2:
      decoded_pw = Decode(encoded_pw)
      print(f"The encoded password is {decoded_pw[0]}, and the original password is {decoded_pw[1]}.")
    if option == 3:
      break

      
