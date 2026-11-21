import re 

text = 'Merhaba dünya 052516'

result = re.findall(r'\d',text)    # '\d' metinde sayı olup olmadıını kontrole eder sayı var ise nerede olduğu önemsiz olmak üzere hepsini listeye depolar ve döner.

if result:
    print('eşleşme var ')

else:
    print('eşleşme yok')

print(result)
