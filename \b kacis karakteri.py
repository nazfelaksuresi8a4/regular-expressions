import re 

text = '''Merhaba arkadaşlar'''

pattern = r'\bark'    #\b kacis karakteri metnin içinde herhangi bir kelimenin bu harfle başlayıp başlamadıgın veya bitip bitmediğini kontrol eder başlangıcınınmı bitişinimi kontrole deceğini kacis karakterini koyduğunuz alan belirler.

result = re.findall(pattern,text)

if result:  #ark ile baslayan kelime varsa burası calısır
    print('eşleşme var')

else:
    print('eşleşme yok')

print(result)

pattern = r'ark\b'    #\b kacis karakteri metnin içinde herhangi bir kelimenin bu harfle başlayıp başlamadıgın veya bitip bitmediğini kontrol eder başlangıcınınmı bitişinimi kontrole deceğini kacis karakterini koyduğunuz alan belirler.

result = re.findall(pattern,text)

if result:  #ark ile biten kelime varsa burası calısır
    print('eşleşme var')

else:
    print('eşleşme yok')

print(result)
