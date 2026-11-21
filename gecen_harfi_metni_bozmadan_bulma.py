import re 

text = 'Merhaba herkese'

result = re.findall(r'a*',text)    #* işareti bir harfin 1 veya sonsuz kez geçip geçmediğine bakar eğer koşul sağlandı ise result içine harfleri dizer (harfler dizilirken koşuluın desteklenmediği eyerler '' olarak işaretlenir ve metin sırası bozulmaz bir nevi maskeleme gibidir)

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
