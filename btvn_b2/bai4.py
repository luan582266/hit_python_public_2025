n = int(input("nhập số xu: "))

mua = n // 28
tongbia = mua 
vobia = mua 

while vobia >= 3: 
    doi = vobia // 3
    tongbia += doi
    vobia = doi + (vobia % 3) 
    
print("Số bia mua được là: ", tongbia)