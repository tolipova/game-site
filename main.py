print("\n Start o'yin boshlandi!")

while True:
    user_name=input("User_name kiriting: ")
    parol=input("Parolni kiriting: ")
    if user_name  == 'root'or 'admin':
     print("\n Garajga kirdingiz, Hush kelibsiz!!!")
     break
    else: 
      print("Xato user_name kirittingiz")
      continue
admin=['damas','nexia','lacetti']    
root=['malibu','captiva','epica']
if user_name == 'admin':
    print("Quyidagi mashinalardan birini tanlang :",admin)
    a=input( )
elif  user_name == 'root':
    print("Quyidagi mashinalardan birini tanlang :",root)
    b=input() 
else:
   print("Xatolik bor!")
print("Siz tanlagan mashina:",a or b)
