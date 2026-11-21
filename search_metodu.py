import re 

text = 'Bu cümlede kac tane bosluk var'

pattern = r'\s'    #boşlukları bulur
pattern_2 = r'\s[a-d]'  #boşluklardan sonra a ile d arası harf varsa desteklenir.

results = re.search(pattern_2,text)

start_index = results.start()   #bulunan ifadelerin baslangic indeksini verir.
start_and_stop_index = results.span() #bulunan ifadelerin baslangic ve bitis indekslerini verir

print(start_index)
print(start_and_stop_index)
