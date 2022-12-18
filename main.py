ozurlu=int(input("Özürlü Devamsızlık Giriniz :  "))
ozursuz=int(input("Özürsüz Devamsızlık Giriniz :  "))
toplam=ozurlu+ozursuz

if toplam>30:
  print ("Kaldınız :(")
else:
  if ozursuz>10:
    print ("Kaldınız :(")
  else:
    print("Geçtiniz :)")
  
           