print("tabel perkalian")
print("===============")

number = int(input("mau perkalian"))
loop = int(input("mau berapa banyak?"))

for x in range(1,loop+1):
    result = x * number
    print(f"{x} x {number} = {result}")