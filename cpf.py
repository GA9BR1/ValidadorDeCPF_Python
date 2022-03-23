cpf = str(input('Digite um número de CPF xxx.xxx.xxx-xx: '))
dig1 = []
dig2 = []
modt = 0
while len(cpf) != 14:
    print('Número de CPF inválido, verifique a digitação xxx.xxx.xxx-xx')
    cpf = str(input('Digite um número de CPF: '))
if len(cpf) == 14:
    cpfnum = cpf.split('.')
    cpfnum = ''.join(cpfnum)
    cpfnum = cpfnum.split('-')
    cpfnum = ''.join(cpfnum)
    # Verificação de dígito 1
    for num, multi in zip(cpfnum, range(10, 1, -1)):
        num = int(num)
        dig1.append(num * multi)
    somadig1 = sum(dig1)
    mod1 = 11 - (somadig1 % 11)
    # Verificação de dígito 2
    for num, multi in zip(cpfnum, range(11, 1, -1)):
        num = int(num)
        if multi > 2:
            dig2.append(num * multi)
        if multi == 2:
            if mod1 > 9:
                modt = 0
            elif mod1 <= 9:
                modt = mod1
            dig2.append(modt * multi)
    somadig2 = sum(dig2)
    mod2 = 11 - (somadig2 % 11)
    if mod1 > 9 and cpfnum[-2] == '0' or mod1 <= 9 and cpfnum[-2] == str(mod1):
        if mod2 > 9 and cpfnum[-1] == '0' or mod2 <= 9 and cpfnum[-1] == str(mod2):
            print('CPF válido')
        else:
            print('CPF inválido')
    else:
        print('CPF inválido')





