reaction = int(input('Ingrese su tiempo de reacción en milisegundos '))

if reaction < 200:
    print('Categoría: Rápido')
elif 200 <= reaction <= 500:
    print('Categoría: Normal')
else:
    print('Categoría: Lento')
