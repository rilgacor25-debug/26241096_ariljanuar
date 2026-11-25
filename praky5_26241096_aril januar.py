# nama: aril januar
# Nim: 26241096
# kelas: 1 C PTI
# Mata Kuliah: Pemrograman Dasar
# Tugas: Operator Komparasi dan Boolean

nama = input("Nama mahasiswa : ")
nim = input("NIM lengkap    : ")

digit_a = int(input("Digit A        : "))
digit_b = int(input("Digit B        : "))

print("\n===== DATA MAHASISWA =====")
print("Nama mahasiswa :", nama)
print("NIM lengkap    :", nim)
print("Digit A        :", digit_a)
print("Digit B        :", digit_b)

print("\n===== HASIL PERBANDINGAN =====")

print("A > B  :", digit_a > digit_b)
print("A < B  :", digit_a < digit_b)
print("A == B :", digit_a == digit_b)
print("A != B :", digit_a != digit_b)
print("A >= B :", digit_a >= digit_b)
print("A <= B :", digit_a <= digit_b)
