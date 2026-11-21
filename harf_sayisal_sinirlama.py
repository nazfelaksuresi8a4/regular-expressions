import re 

text = 'Merhaba herkese'

result = re.findall(r'M.{2}a',text)    # M den sonra herhangi 2 harf olabilir ancak sonrasında a ile bitmek zorunda koşuludur. 

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

result = re.findall(r'\d{2}',text)    # metindeki sayılar 2 şerli olarak bölünüp verilir veya 2 şerli grup olanları döner

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

result = re.findall(r'\d{1,2}',text)    # metinde ardışık olmayan sayılar veya ardışık ikili sayılar varsa döner 

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

result = re.findall(r'\d{1,}',text)    # metinde tek kalan sayıları döner birden fazla art arda gelmiş sayıları kendi gruplarıyla beraber döner

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

# {alt_sinir,üst_sinir}
