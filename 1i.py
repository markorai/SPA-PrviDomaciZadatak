#Napisati rekurzivnu funkciju koja vraća proizvod cifara zadatog broja n.
def multiplication_of_digits(num):
  if num == 0:
    return 1
  else:
    return num%10 * multiplication_of_digits(num//10)

print(multiplication_of_digits(1234))