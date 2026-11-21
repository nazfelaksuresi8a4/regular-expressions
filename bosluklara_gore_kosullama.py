import re 

text = 'Bu cümlede kac tane bosluk var'

pattern = r'\s'    #boşlukları bulur
pattern_2 = r'\s[a-d]'  #boşluklardan sonra a ile d arası harf varsa desteklenir.

results = re.findall(pattern_2,text)

print(results)

