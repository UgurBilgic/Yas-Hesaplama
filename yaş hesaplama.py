isim = input("Adınız: ")    #kullanıcıdan ismi istenir

doğum_yılı = int(input("Doğum yılınız: "))    #kullanıcıdan doğum yılı istenir

yaş = 2023 - doğum_yılı      #kullanıcının yaşı hesaplanır

mesaj = isim + " adlı kişinin yaşı " + str(yaş)  #kullanıcıya adı ve yaşı söylenir

print(mesaj)   #mesaj ekrana gösterilir

input("Çıkmak için ENTER'a basınız")