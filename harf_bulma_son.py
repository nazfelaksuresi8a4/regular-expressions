import re 

text = 'Merhaba herkese'

result = re.findall(r'M.*a',text)    # '.' herhangi bir karakteri temsil eder ve başına yıldız geldiği zaman şunu sorar "M den sonra 1 veya sonsuz tane harf varsa ve bu zincirin sonunda a harfi ile bitiyorsa koşulu destekle

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

result = re.findall(r'M.+a',text)    # yukarıdakinin aynısının 1 veya sonsuz tane geçen versiyonu

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)

result = re.findall(r'M.?a',text)    #yukarıdakinin aynısının 0 veya 1 tane geçebilen ve daha fazla geçerse desteklenmeyen versiyonu

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
