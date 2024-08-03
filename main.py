# Function to convert a number in a specified base to a number in base 10
def convert_to_decimal(number, base):
  decimal_value = 0
  power = 0
  while number != 0:
      remainder = number % 10
      decimal_value += remainder * (base ** power)
      number //= 10
      power += 1
  return decimal_value

# Function to convert decimal number into the new final base 
def convert_from_decimal(decimal_number, new_base):
  new_base_number = 0
  power = 0
  while decimal_number != 0:
      remainder = decimal_number % new_base
      new_base_number += remainder * (10 ** power)
      decimal_number //= new_base
      power += 1
  return new_base_number

continue_program = True

# While loop to keep asking user for number, original base, and new base for the number and executing the program until they choose to stop
while continue_program:
  original_number = int(input("Enter the original number: "))
  original_base = int(input("Enter the original base: "))
  new_base = int(input("Enter the new base: "))

  decimal_number = convert_to_decimal(original_number, original_base)
  result = convert_from_decimal(decimal_number, new_base)

  print(f"The number {original_number} in base {original_base} is equivalent to {result} in base {new_base}")

  choice = input("Do you want to continue? (yes/no): ")
  if choice.lower() == "no":
      continue_program = False