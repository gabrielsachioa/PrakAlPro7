# CARA KE 1
def frekuensi_kata(kalimat, kata):
    kalimat = kalimat.lower()
    kata = kata.lower()

    kalimat = ["".join(i for i in kalimat if i.isalpha()) for kalimat in kalimat.split()]

    frek_kata = kalimat.count(kata)
    print(frek_kata)


# PROGRAM UTAMA
kalimat = input("Kalimat: ")
kata = input("Kata: ")
frekuensi_kata(kalimat, kata)
# frekuensi_kata("Saya mau makan. Makan itu wajib. Mau siang atau malam saya wajib makan", "makan")
