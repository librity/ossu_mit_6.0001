def float_or_die(message):
  number_str = input(message)

  try:
    number_f = float(number_str)
  except:
    print("Error parsing float:", number_str)
    quit()

  return number_f


def int_or_die(message):
  number_str = input(message)

  try:
    number_i = int(number_str)
  except:
    print("Error parsing int:", number_str)
    quit()

  return number_i
