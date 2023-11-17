print("score range checker")
print("===================")

score = int(input("masukkan nilai anda: "))

if score >= 85 and score <= 100:
    print("kamu mendapatkan A")
elif score >= 70 and score <= 84:
    print("kamu mendapatkan B")
elif score >= 60 and score <= 69:
    print("kamu mendapatkan C")
else:
    print("kamu mendapatkan D")