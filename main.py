#Ryan Mijares
def Decode(input):
  new_pass = ''
  for number in input:
    if int(number) <= 2:
      new_pass += str((int(number) + 7))
    else:
      new_pass += str((int(number) - 3))
  return [new_pass, input]

def encoder(password):
  new_pass = ''
  for number in password:
    if int(number)+3 >= 7:
      new_pass += str((int(number) - 7))
    else:
      new_pass += str((int(number) + 3))
  return new_pass

def menu():
  print("Menu")
  print("-------------")
  print("1. Encode")
  print("2. Decode")
  print("3. Quit")

def main():
  while True:
    menu()
    option = int(input("Please enter an option: "))
    if option == 1:
      u_input = input("Please enter your password to encode: ")
      encoder(u_input)
      print("Your password has been encoded and stored!")
    elif option == 2:
      value = Decode(u_input)
      print(f"The encoded password is {value[0]}, and the original password is {value[1]}")
    elif option == 3:
      break

if __name__ == "__main__":
  main()
