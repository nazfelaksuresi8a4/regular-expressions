#regex ile örnek uygulamalar 

#1- isim kontrolü

import re

pattern = r'^[a-zA-Z]+' #büyük ve küçük harfler a dan z ye olmak üzere var ise hepsini grupla

while True:
    name = str(input('isminiz nedir: '))

    if re.fullmatch(pattern,name):      #fullmatch metodu girdinin pattern ile tam uyumlu olup olmaıgını kontrol eder.
        print(f'Teşekkürler. İsminiz, {name}')
        break

    else:
        print('isim sadece sözel karakter içerebilir!')


