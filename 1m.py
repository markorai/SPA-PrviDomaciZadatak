#Napisati rekurzivnu funkciju koja vraća poslednje veliko slovo zadatog stringa.

def last_capital_letter(str1):
  if str1[-1] == str1[-1].upper() and str1[-1] != " ":
    return str1[-1]
  else:
    return last_capital_letter(str1[:-1])


print(last_capital_letter("oVo je nEki string"))