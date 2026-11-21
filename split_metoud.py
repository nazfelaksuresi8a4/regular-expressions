import re 

text = 'Bu cumlede kac tane bosluk var'

pattern = r'\s'     #\w, "c" harfinden sonra gelen kelime karakterlerini (harf, rakam veya alt çizgi _) yakalamaya yarar + ise gruplar (bitişe kadar gitmesini sağlar.)

results = re.split(pattern,text,maxsplit=2) #split her pattern desteklendikten sonra ifadeyi böler maxsplit paramtertesi bölme sayısını verir 1. desteklemeden sonra böler 2. desteklemeden sonra böler ve 3. desteklemeye gelince bölme yapmadan hepsini birden döner

print(results)
