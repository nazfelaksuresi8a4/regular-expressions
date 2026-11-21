import re 

text = 'Bu cümlede kac tane bosluk var'

pattern = r'\bc\w+'     #\w, "c" harfinden sonra gelen kelime karakterlerini (harf, rakam veya alt çizgi _) yakalamaya yarar + ise gruplar (bitişe kadar gitmesini sağlar.)

results = re.findall(pattern,text)

print(results)
