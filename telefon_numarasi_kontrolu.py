import re 

telefon_numarasi = '535-1111111'

pattern = r'\d{3,4}-\d{7}' # '-' tan önce 3 veya 4 haneli olarak bölünebilecek bir numara ve slashtan sonra 7 haneli olmak zorunda olan bir numara var ise desen desteklenir.

results = re.findall(pattern,telefon_numarasi)

if results:
    print('telefon numarasi doğru')

else:
    print('telefon numaraniz yanlis')

print(results)

