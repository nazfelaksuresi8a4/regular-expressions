import re 

text = 'Merhaba herkese Merhaba'

pattern_1 = r'(Merhaba)+'#merhaba sözcüğü 1 veya daha fazla kez geçtiyse tek tek listeyle döner 
pattern_2 = r'(Merhaba)*'#merhaba sözcüğü 0 veya daha fazla kez geçtiyse tek tek listeyle döner 
pattern_3 = r'(Merhaba)?'#merhaba sözcüğü 0 veya 1 kez geçtiyse tek tek listeyle döner 

results = re.findall(pattern_1,text)    

if results:
    print('eşleşme var')

else:
    print('eşleşme yok')

print(results)

