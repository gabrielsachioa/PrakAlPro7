def hapus_kelebihan_spasi(kalimat):
    kalimat = kalimat.lower()
    kalimat = " ".join(kalimat.split())
    print(kalimat)

# PROGRAM UTAMA
# kalimat = input("Kalimat: ")
hapus_kelebihan_spasi("saya tidak  suka memancing ikan ")