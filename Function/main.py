#function

def add(n1, n2):
    result = n1 + n2
    print (n1, " + ",n2, " = ",result)

def substitute(n1, n2):
  result = n1 - n2
  print (n1, " - ",n2, " = ",result)

def multiply(n1, n2):
  result = n1 * n2
  print (n1, " x ",n2, " = ",result)

def divide(n1, n2):
  result = n1 / n2
  print (n1, " / ",n2, " = ",result)

print("kalkulator sederhana")
print("====================")
print("mode kalkulator")
print("1. tambah")
print("2. kurang")
print("3. kali")
print("4. bagi")

mode = input("pilih 1/2/3/4: ")
number1 = int(input("masukkan angka pertama: "))
number2 = int(input("masukkan angka kedua: "))

if mode == "1":
  add(number1, number2)
elif mode == "2":
  substitute(number1, number2)
elif mode == "3":
  multiply(number1, number2)
elif mode == "4":
  divide(number1, number2)
else:
  ("mode yang anda masukkan salah")