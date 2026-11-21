#sub metodu belirtilen desene göre desen her desteklendiğinde split gibi eş parçalara bölmek yerine bizim belirttiğimiz karakteri o bosluk yerine koyar aşşağıdaki örnekte bosluklar için bunu yapması istenmiştir. count pozisyonel argümanı ise baştan sona kaç tane koyacağını verir 5 bosluk var ise 2 tane count dersek baştan 2 tanesi değiştirilip sondan 3 tanesi aynen kalır.

import re 

text = 'Bu cumlede kac tane bosluk var'

pattern = r'\s'     #\w, "c" harfinden sonra gelen kelime karakterlerini (harf, rakam veya alt çizgi _) yakalamaya yarar + ise gruplar (bitişe kadar gitmesini sağlar.)

results = re.sub(pattern,'-',text,count=2) #split her pattern desteklendikten sonra ifadeyi böler maxsplit paramtertesi bölme sayısını verir 1. desteklemeden sonra böler 2. desteklemeden sonra böler ve 3. desteklemeye gelince bölme yapmadan hepsini birden döner

print(results)
