import re 

text = '''Merhaba arkadaşlar
Merhaba diyorum'''

pattern = r'^Merhaba'  #baştaki işaret metnin başındakini kontrol etmemizi sağlar.

result = re.findall(pattern,text,re.MULTILINE)    #multiline demek her bir satır için bu işlemi tekrarla demektir.

if result:
    print('eşleşme var')

else:
    print('eşleşme yok')

print(result)
