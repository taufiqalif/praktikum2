nama = input("masukan nama: ")
uts = input("masukan nila UTS: ")
uas = input("masukan nilai UAS: ")
tugas = input("masukan nilai TUGAS: ")
akhir = (int(tugas)*.2)+(int(uts)*.4)+(int(uas)*.4)
keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]

if akhir > 80:
    huruf = "A"
elif akhir > 70:
    huruf = "B"
elif akhir > 50:
    huruf = "C"
elif akhir > 40:
    huruf = "D"
else:
    huruf = "COBA LAGI"

print("Nama: ", nama)
print("nilai UTS:", uts)
print("nilai UAS: ", uas)
print("nilai tugas: ", tugas)
print("nilai akhir: ", akhir)
print("Nilai huruf: ", huruf)
print("keterangan: ", keterangan)
