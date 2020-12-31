while True:
    try:
        nama = input("masukan nama: ")
        uts = input("masukan nilai UTS: ")
        uas = input("masukan nilai UAS: ")
        tugas = input("masukan nilai TUGAS: ")
        akhir = (float(tugas)*.2)+(float(uts)*.4)+(float(uas)*.4)
        keterangan = ("TIDAK LULUS", "LULUS")[akhir > 60.0]
        break
    except ValueError:
        print("harap masukan angka saat memasukan nilai!")
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
