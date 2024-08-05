entrada = input('Digite um número:')

entrada = int(entrada)



def duplicar_n(entrada):
    duplicado = entrada * 2
    return duplicado

def triplicar_n(entrada):
    return entrada * 3

def quadruplicar_n(entrada):
    return entrada * 4

duplicar_n(entrada)

triplicar_n(entrada)

quadruplicar_n(entrada)
print(f'O número inicial é {entrada}')
print(f'O número duplicado é {duplicar_n(entrada)}')
print(f'O número triplicado é {triplicar_n(entrada)}')
print(f'O número quadruplicado é {quadruplicar_n(entrada)}')
