import random

magic_number = random.randint(1, 10)
print(magic_number)
guess = ""

while  guess != magic_number:
  guess = int(input("guess a number between 1 and 10: "))
  if guess == magic_number:
    print("You win!")
  else:
    print("Incorrect.")
