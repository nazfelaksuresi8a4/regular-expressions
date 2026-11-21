import re 

text = 'Merhaba dünya'

result = re.findall(r'[a-m]',text)    #[harf_1-harf_2] şeklinde yazılan komut iki harf arasında baş ve son harfler dahil olmak üzere metinde geçiyor ise harfleri sırası ile liste olarak döner. 

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
