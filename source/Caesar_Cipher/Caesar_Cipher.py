alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

lua_chon = input("Lua chon (E)ncrypt hoac (D)ecrypt: \n")
text = input("Nhap vao van ban:\n")
shift = int(input("Nhap so buoc dich: "))

def encrypt(text, shift):
    kq = ""
    for letter in text:
        vitri_goc = alphabet.index(letter)
        vitri_moi = (vitri_goc + shift) % len(alphabet) # 21 < 26 => vtri moi = 21
                                                        # 34 > 26 => vtri moi = 8 (= 1 vong alphabet va quay lai dau bang 'i') 
        chucai_moi = alphabet[vitri_moi]
        kq += chucai_moi
    print(f"Doan van ban da duoc ma hoa: {kq}")

def decrypt(text, shift):
    kq = ""
    for chucai in text:
        vitri_hientai = alphabet.index(chucai)
        vitri_cu = (vitri_hientai - shift) % len(alphabet)
        chucai_goc = alphabet[vitri_cu]
        kq += chucai_goc
    print(f"Doan van ban duoc giai ma: {kq}")

if lua_chon == "E":
    encrypt(text, shift)
else:
    decrypt(text, shift)
