import re 

text = 'Merhaba herkese'

pattern = r'Merhaba|arkadaşlar'    #Merhaba veya arkadaşlar sözcüğü metinde geçiyorsa geçeni döner ikisi  geçtiyse ikisinde döner hiç biri geçmezse hiç birini dönmez tek bir tanesi geçse bile koşul desteklenir ve tek birisini döner klasik or kapısı mantığı ile çalışışr.

results = re.findall(pattern,text)

if results:
    print('eşleşme var')

else:
    print('eşleşme yok')

print(results)
