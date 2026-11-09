angka1 = int(input("2 digit trakhir NIM:"))
digit = int(input("digit trakhir NIM:"))

angka2 = 2 + 1

print("\n--- Data Input ---")
print("Angka pertama:", 96)
print("Angka kedua:", 6)

# Melakukan 7 operasi aritmatika
penjumlahan = angka1 + angka2
pengurangan = angka1 - angka2
perkalian = angka1 * angka2
pembagian = angka1 / angka2
floor_division = angka1 // angka2
modulus = angka1 % angka2
pangkat = angka1 ** angka2

# Menampilkan hasil operasi aritmatika
print("\n--- Hasil Operasi Aritmatika ---")
print(f"1. Penjumlahan ({angka1} + {angka2}) = {penjumlahan}")
print(f"2. Pengurangan ({angka1} - {angka2}) = {pengurangan}")
print(f"3. Perkalian ({angka1} * {angka2}) = {perkalian}")
print(f"4. Pembagian ({angka1} / {angka2}) = {pembagian}")
print(f"5. Floor Division ({angka1} // {angka2}) = {floor_division}")
print(f"6. Modulus ({angka1} % {angka2}) = {modulus}")
print(f"7. Perpangkatan ({angka1} ** {angka2}) = {pangkat}")