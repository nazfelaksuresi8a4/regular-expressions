import re 

text = 'Merhaba herkese'

result = re.findall(r'a?',text)    #? işareti bir harfin metinde 0 kez veya 1 kez geçip geçmediğini kontrol eder eğer 1 den fazla ise koşul sağlanmaz
if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
