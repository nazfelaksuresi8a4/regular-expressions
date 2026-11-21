import re 

text = '''Merhaba arkadaşlar
          Merhaba diyorum'''

pattern = r'\AMerhaba'    #\A kacis karakteri burada metnin başlangıcına bakar eğer başlangıcında belirttiğimiz harf zinciri var ise koşul desteklenir ve liste içinde desteklenenleri döner. Sadece ilk satıra bakar aşşağılara inmez varsa vardır yoksa yoktur.

result = re.findall(pattern,text)

if result:
    print('eşleşme var')

else:
    print('eşleşme yok')

print(result)
