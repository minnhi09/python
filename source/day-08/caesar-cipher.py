# Xây dựng Caesar Cirpher : phương pháp mã hóa văn bản

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\nnhập 'encode' để mã hóa văn bản hoặc 'decode' để giải mã: ")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))