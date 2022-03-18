from cmath import log


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


def main():
  x = int_or_die("Enter number x: ")
  y = int_or_die("Enter number y: ")

  x_pow_y = x ** y
  print("X**y =", x_pow_y)

  log2_x = log(x, 2)
  print("log2(x) =", log2_x.real)


if __name__ == "__main__":
  main()
