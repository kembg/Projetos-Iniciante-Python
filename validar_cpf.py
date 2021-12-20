cpf = '494.090.788'
cpf = cpf.split('.')
cpf = ''.join(cpf)
x = 10
soma = 0
y = 11

for i in range(0, len(cpf)):
    num = int(cpf[i])
    soma += num * x
    x -= 1
dig1 = 11 - (soma % 11)

if dig1 > 9:
    dig1 = '0'
else:
    dig1 = str(dig1)
cpf = cpf+dig1

for i in range(0, len(cpf)):
    num = int(cpf[i])
    soma += num * y
    y -= 1
dig2 = 11 - (soma % 11)
cpf = cpf + str(dig2)

print(f'{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9::]}')
