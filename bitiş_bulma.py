import re 

text = 'Merhaba dünya'

result = re.findall(r'dünya$',text)    # '$' işareti kelimenin metnin sonunda olup olmadıgını kontrol eder metin bu kelime ile bitiyor ise liste olarak döner 

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
