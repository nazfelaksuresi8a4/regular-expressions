import re 

text = '''Merhaba arkadaşlar
Merhaba diyorum'''

pattern = r'arkadaşlar\Z'  #metnin sonunun bununla bitip bitmediğni kontrol etmemizi sağlar.

result = re.findall(pattern,text)

if result:
    print('eşleşme var')

else:
    print('eşleşme yok')

print(result)
