def addmultiplenumbers(numbers):
   return sum(numbers)
def multiplymultiplenumbers(numbers):
    result = 1
    for num in numbers:
        result = result * num
    return result
def isitaninteger(num):
    return isinstance(num, int)
def isiteven(num):
    return isitaninteger(num) and num % 2 == 0
def main():
  print("Hello learners!")
  print("Suma:", addmultiplenumbers([1, 2, 3, 4]))
  print("Multiplicación:", multiplymultiplenumbers([1, 2, 3, 4]))
  print("¿Es entero 5?:", isitaninteger(5))
  print("¿Es par 4?:", isiteven(4))

if __name__=="__main__":
  main()