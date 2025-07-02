min_lenght = 5

username = input('Ingrese su nombre de usuario. ')

isValid = False
hasDigit = False
hasUpper = False


    
for carac in username:
    if carac.isdigit():
        hasDigit = True
    if carac.isupper():
        hasUpper = True
    if carac.isalnum():
        isValid = True
        
if len(username) >= min_lenght:
    isValid = True
else:
    print ('Debe contener al menos 5 caracteres.')
    

if not hasDigit:
    isValid = False
    print('El nombre de usuario debe contener un digito.')
    
if not hasUpper:
    isValid = False
    print('El nombre de usuario debe contener una mayuscula.')

    
if isValid:
    print('El nombre de usuario es adecuado. ')
