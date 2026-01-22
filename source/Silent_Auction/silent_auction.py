#khởi tạo dictionary rỗng, lưu khách đấu giá
khach = {}
tieptuc_daugia =  True

def Tim_So_Tien_Lon_Nhat(object_khach):
    tien_max = 0
    winner = ""

    for khach in object_khach:
        sotien_daugia = object_khach[khach]
        if sotien_daugia > tien_max:
            tien_max = sotien_daugia
            winner = khach
    print(f"Người chiến thắng là {winner} với số tiền đấu giá là {tien_max}.")

while tieptuc_daugia:
    ten = input("Nhập vào tên của bạn: ")
    gia = int(input("Nhập vào số tiền bạn muốn đấu giá ($): "))

    khach[ten] = gia

    should_continue = input("Có còn khách nào muốn đấu giá nữa không? y/n ").lower()
    if should_continue == "n":
        tieptuc_daugia = False
        Tim_So_Tien_Lon_Nhat(khach)
    elif should_continue == "y":
        print("\n"*100)
    else:
        choose = input("Mời chọn \"y\" để tiếp tục đấu giá hoặc ấn phím bất kì để kết thúc phiên đấu giá: ").lower()
        if choose == "y":
            print("\n"*100)
        else:
            tieptuc_daugia = False
            Tim_So_Tien_Lon_Nhat(khach)




        
            
