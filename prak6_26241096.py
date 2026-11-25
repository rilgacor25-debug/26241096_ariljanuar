# Tugas Mahasiswa - Pertemuan 6
# Operator Logika NOT, AND, OR, dan XOR
# NIM: 26241096

# Input dua digit terakhir NIM
a = int(input("Digit A: "))
b = int(input("Digit B: "))

# Membuat dua kondisi Boolean
kondisi1 = a >= 5
kondisi2 = b >= 5

# Menampilkan nilai kondisi
print("Kondisi 1:", kondisi1)
print("Kondisi 2:", kondisi2)

# Menampilkan hasil operasi logika
print("NOT:", not kondisi1)
print("AND:", kondisi1 and kondisi2)
print("OR :", kondisi1 or kondisi2)
print("XOR:", kondisi1 ^ kondisi2)
