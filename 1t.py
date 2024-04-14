#Napisati rekurzivnu funkciju koja provjerava koliko zadati broj ima parnih cifara.
def count_even_digits(num):

  if num%10 == 0:
    return 0

  if num < 10:
    if num % 2 == 0:
      return 1
    else:
      return 0
  elif num % 10 % 2 == 0:
    return 1 + count_even_digits(num//10)
  else:
    return 0 + count_even_digits(num//10)

print(count_even_digits(24689))