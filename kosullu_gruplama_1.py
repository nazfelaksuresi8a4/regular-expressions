import re 

text = 'Merhaba benim yasim 50'

pattern = r'[a-zA-Z0-9]+'    #a dan z ye küçük karakterler ve a dan z ye büyük karakterler varsa ve 0 dan 9 a kadar sayılar varsa desen desteklenir. + işareti ile gruplama sağlanır ve ardışık olanları gruplanır.

results = re.findall(pattern,text)

print(results)
