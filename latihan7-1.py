def jumlah_huruf_kata1(kata1):
    hasil = {}

    for huruf in kata1:
        if huruf in hasil:
            hasil[huruf] += 1
        else:
            hasil[huruf] = 1
    return hasil

def jumlah_huruf_kata2(kata2):
    hasil = {}

    for huruf in kata2:
        if huruf in hasil:
            hasil[huruf] += 1
        else:
            hasil[huruf] = 1
    return hasil

def cek_anagram(kata1, kata2):
    if len(kata1) != len(kata2):
        print("Bukan Anagram")
    else:
        huruf_kata1 = jumlah_huruf_kata1(kata1)
        huruf_kata2 = jumlah_huruf_kata2(kata2)

        if huruf_kata1 == huruf_kata2:
            print("Anagram")
        else:
            print("Bukan Anagram")

# PROGRAM UTAMA
kata1 = input("Kata pertama: ")
kata2 = input("Kata kedua: ")
cek_anagram(kata1, kata2)