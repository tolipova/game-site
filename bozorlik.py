bozorliklar=[]

while True :
    xarid=input("Xarid qilmoqchi bulgan ruyxatni kiriting:")
    if xarid.lower() == 'exit' :
            break
    bozorliklar.append(xarid)
mahsulot_narxi={}

while len(bozorliklar) > 0 :
        xarid_nomi=bozorliklar.pop(0)
        narx = float(input(f"{xarid_nomi}ni narxini kiriting: "))
        mahsulot_narxi[xarid_nomi] = narx
print("\n Xarid qilingan mahsulot narxlari: ")    
for xarid,narx in mahsulot_narxi.items():
     print(f"{xarid}:{narx}")

