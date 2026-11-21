import re 

text = 'merhaba'

pattern = r'[^a]'       #bu kullanımda ^ karakteri [] içinde olduğu zaman tersine döner ve bulduğu eşleşmeleri siler

results = re.findall(pattern,text)

print(results)

pattern = r'[^a]+'       #bu kullanımda ise ^ karakteri [] içinde olduğu zaman tersine döner ancak + işareti nedeniyle art arda gelen eşleşmelerde gruplama yapılır

results = re.findall(pattern,text)

print(results)

pattern = r'[a-n]+'       #bu kullanımda ise klasik gruplama ve harf aralıgı vardır
results = re.findall(pattern,text)

print(results)
