#Password Generator Project
import random

def generate_password():
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  nr_letters = random.randint(8, 10)
  nr_symbols = random.randint(2, 4)
  nr_numbers = random.randint(2, 4)

  password_list = []

  letters_list = [random.choice(letters) for char in range(nr_letters)]
  # for char in range(nr_letters):
  #   password_list.append(random.choice(letters))

  symbols_list = [random.choice(symbols) for char in range(nr_symbols)]
  # for char in range(nr_symbols):
  #   password_list += random.choice(symbols)

  numbers_list = [random.choice(numbers) for char in range(nr_numbers)]
  # for char in range(nr_numbers):
  #   password_list += random.choice(numbers)
  password_list.extend(letters_list)
  password_list.extend(symbols_list)
  password_list.extend(numbers_list)

  random.shuffle(password_list)

  password = "".join(password_list) # This does the same function as the 3 lines below
  # password = ""
  # for char in password_list:
  #   password += char

  print(f"Your password is: {password}")
  return password


# generate_password()