import re 

text = 'Merhaba herkese'

result = re.findall(r'Me+r',text)    #Me+r dediğimiz zaman M ile başlayıp e 1 veya sonsuz kez geçtiyse ve sonunda r var ise koşulu destekle demektir koşul desteklendiyse liste olarak sadece desteklenen bölüm dönülür.

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
