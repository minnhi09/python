alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
# text = input("Nhap vao chuoi van ban: ")
# chon = input("Chon \"E\" de ma hoa, nhap \"D\" de giai ma van ban: \n").lower()
# shift_number = int(input("Nhap vao so Shift: "))
should_continue = True

def caesar(textdef, sf_number, chon):
    kq = ""

    if chon == "d":
        sf_number *= -1
    
    for letter in textdef:
        if letter not in alphabet:
            kq += letter
        else:
            vt_current = alphabet.index(letter)
            dinhchuan_sfmunber = sf_number % len(alphabet)
            vt_new = vt_current + dinhchuan_sfmunber
            kq += alphabet[vt_new]
    print(f"Ket qua: {kq}")


while should_continue:
    direction = input("Nhap \"E\" de ma hoa, nhap \"D\" de giai ma van ban: \n")
    text = input("Nhap vao chuoi van ban: ")
    shift_number = int(input("Nhap vao so Shift: "))

    caesar(text, shift_number, direction)

    restart = input("Do you want to go again? y/n ").lower()

    if restart == "n":
        should_continue = False
        print("Goodbye")
