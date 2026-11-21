import re 

text = '9242680284929687280U5962YJ0H5G0895057Y828778620876480760782468075280HG0'

pattern = r'\D' #upper case D harfi lower case D yani d harfinin tersidir sayı hariç her şeyi bulmamızı sağlar.

results = re.findall(pattern,text)  

if results:
    print('harf bulundu')

else:
    print('harf bulunamadi')

print(results)
