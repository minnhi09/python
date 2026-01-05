print("Welcome to tip calculator")
#nhap so tien bill
bill = float(input("What was the total bill ? $"))
#nhap so % tien muon tip dua theo bill
percen_tip = int(input("What percentage would you like to give ? 10, 12 or 15 ?"))
#nhap so nguoi muon tra tien tip 
people = int(input("How many people to split the bill ?"))


tien_tip = bill * (percen_tip / 100)
tong_bill = bill + tien_tip
tien_bill_1_nguoi = tong_bill / people

print(f"Tong tien bill la: ${tong_bill} ")
print(f"So tien 1 nguoi phai tra la: ${tien_bill_1_nguoi}")