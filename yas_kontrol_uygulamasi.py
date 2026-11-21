#regex ile örnek uygulamalar 

#1- isim kontrolü

import re

pattern = r'[1-9]+' #sayı önemsiz ise \d+ kullanıulabilir \d sadece sayı alır + gruplar ancak burada 1 ve 9 arası tüm sayıları bul ve grupla dedik

while True:
    name = str(input('isminiz nedir: '))

    if re.fullmatch(pattern,name):      #fullmatch metodu girdinin pattern ile tam uyumlu olup olmaıgını kontrol eder.
        print(f'Teşekkürler. yaşınız, {name}')
        break

    else:
        print('yaşınızı doğru girdiğinizden emin olun yaşınız negatif veya 0 olamaz!')


