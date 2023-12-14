"""
Nama Program    : guessGame.py
Deskripsi       : Program game sederhana menebak angka
Nama Pembuat    : Zulvikar Kharisma Nur M.
NIM             : 4.33.23.2.26
Tanggal         : 17/11/23
"""

def guess_number():

    secret_number = 9  # angka yang perlu di tebak
    guess_count = 0
    guess_limit = 3  # limit melakukan guessing

    while guess_count < guess_limit:
        user = int(input("guess: "))

        if user == secret_number:
            print("Anda berhasil")
            break
        else:
            print("Anda kurang beruntung")
            guess_count += 1
            print("Sisa kesempatan:", guess_limit - guess_count)
    else:
        print("Kesempatan anda habis")
