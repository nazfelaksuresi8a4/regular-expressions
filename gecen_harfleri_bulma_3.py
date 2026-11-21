import re 

text = 'Merhaba herkesea'

result = re.findall(r'a+',text)    # '+' işareti bir harfin 1 veya sonsuz kez geçip geçmediğini kontrol eder eğer koşul sağlandıysa sadece harfleri listeye koyup verir. 

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
