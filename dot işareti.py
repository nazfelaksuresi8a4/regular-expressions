import re 

text = 'Merhaba dünya'

result = re.findall('M.....a',text)    # '.' işareti iki harf arasına koyulduğunda metinde geen herhangi bir kelimenin bitiş ve başlangı harfini temsil eder arasındaki nokta sayısı kadar harf varsa kelimeyi döner.

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
