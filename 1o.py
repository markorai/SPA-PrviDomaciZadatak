#Napisati rekurzivnu funkciju koja provjerava koliko zadati broj ima neparvnih cifara
def check_odd_digits(num):
  if num < 10:
    if num % 2 == 0:
      return 0
    else:
      return 1

  if num % 2 != 0:
    return 1 + check_odd_digits(num//10)
  else:
    return 0 + check_odd_digits(num//10)

check_odd_digits(101)