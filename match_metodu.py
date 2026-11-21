import re 

text = 'Bu cumlede kac tane bosluk var'

letter = 'Bu'

output = re.match(letter,text)  #match metodu sadece en baştaki ile bizim desenimizi karşılaştırır.

print(output)
