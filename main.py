Número = float(input("Digite um número:"))
if Número < 1 or Número > 2:
    print('Grau Inválido')
elif Número ==1:
    print('Equação do primeiro grau')  
    p1 = float(input('Digite o valor de a:'))
    if p1 ==0:
        print('Valor Inválido.')
    else:
        p2 = float(input('Digite o valor de b:'))
        x = -p2 / -p1 
        print(f"o valor da raiz é {x:.2f}")   
else:
    print('Equação do segundo grau.')
    q1 = float(input('digite o valor de a:'))
    if q1 ==0:
        print('valor Inválido!')
    else:
        q2 = float(input('digite o valor de b:'))
        q3 = float(input('digite o valor de c:'))
        x = q2 ** 2 - 4 * q1 * q3   
        if x < 0:
            print('A Equação não possui raízes reais')
        elif x==0:
            y = -q2 / (2 *q1)
            print(f'A Equação possui apenas uma raiz real{y:.2f}')
        else:
            if x >0:
             t = (-q2 - x **0.5)/(2 * q1)
             a = (-q2 + x **0.5)/(2 * q1) 
            print(f'`A Equação possui duas raízes reais{t:.2f} e {a:.2f} ')