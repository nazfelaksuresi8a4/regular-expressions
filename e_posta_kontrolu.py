#regex ile örnek uygulamalar 

#1- isim kontrolü

import re

def is_valid_email(email):
    #örnek olarak ahmet.mustafa17@gmail.com.tr
    
    pattern = r'^[a-zA-Z0-9._]+@[a-zA-Z.-]+\.[a-zA-Z]{2,}$' #açıklama: ^başlangıç oldugunu belirtir büyük ve küçük harfleri 0 dan 9 a kadar rakamları ve . _ özel karakterlerini destekler [] ile aynı grupta oldukları belirtilir ve + ile bunların gruplanması söylenir sonunda @ olmak zorundadır. @ işaretinden sonra isebüyük küçük harf ve .- özel karakterlini destekler ve onlarıda grupladıktan sonra en sonundaki .tr ekini desteklemek için . yı meta olarak algılamasın diye \. şeklinde koyarız ve düz string nokta olarak algıladıktan sonra tekrar [a-zA-Z]{2,} deriz ve bu da şu demektir ki büyük ve küçük harfler desteklendiği gibi 2 veya daha fazla barınmak zorundadır şeklinddir ve sondaki dolar işaretide buranın bitiş oldugunu belirtir

    return re.fullmatch(pattern,email)


while True:
    your_email = str(input('e-posta adresiniz: '))

    if is_valid_email(your_email):
        print(f'Teşekkürler. e-posta adresiniz: {your_email}')
        break

    else:
        print('E-posta adresinizi doğru girdiğinizden emin olun!!')
