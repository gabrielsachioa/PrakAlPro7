def ukuran_kata(kalimat):
    kalimat = kalimat.lower()
    kata = kalimat.split(" ")
    
    terpendek = len(kata[0])
    terpanjang = len(kata[0])

    for i in range(len(kata)):
        if len(kata[i]) < terpendek:
            terpendek = len(kata[i])
            kata_terpendek = kata[i]
        elif len(kata[i]) > terpanjang:
            terpanjang = len(kata[i])
            kata_terpanjang = kata[i]
       
    print(f"terpendek: {kata_terpendek} ")
    print(f"terpanjang: {kata_terpanjang}")

# PROGRAM UTAMA
kalimat = input("Kalimat: ")
ukuran_kata(kalimat)
# ukuran_kata("red snakes and a black frog in the pool")