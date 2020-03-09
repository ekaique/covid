#Identificando o nivel de acesso:
iduser = input('Bem vindo(a)!\n Para administrador digite "A"\n Para usuario comum "U"\n Para visitante digite "G"\n Deseja logar como? ').upper()

#Condição para entrada correta dos dados - nivel de acesso (print desconhecido).
if iduser != 'A' and iduser != 'U' and iduser != 'G' :
    print('Olá, desconhecido')
    exit()

#Idenficando o genero (sem polemicas, inserção de "outros" além de masculino e feminino rsrs).

idgenero = input('Para masculino digite "M"\n Para femenino digite "F"\n Para não informar digite "O"\nQual genero você se identifica? ').upper()

#Condição para entrada correta dos dados - genero
if idgenero != 'M' and idgenero != 'F' and idgenero != 'O':
    print('Em uma proxima vez Digite somente M, F ou O por gentileza.')

#Print o administrador(a)
if iduser == 'A':
    if idgenero == 'M':
        print('Olá, administrador')
    elif idgenero == 'F':
        print('Olá, administradora')
    else:
        idinfo = input('Insira seu nome: ').title()
        print('Olá, {},\n Você tem privilegio administrativos'.format(idinfo).title())

#Print usuario comum
elif iduser == 'U':
    if idgenero == 'M':
        print('Olá, usuario')
    elif idgenero == 'F':
        print('Olá, usuaria')
    else:
        idinfo = input('Insira seu nome: ').title()
        print('Olá, {},\n Você tem privilegio de usuario comum'.format(idinfo).title())
#Print visitante
else:
    if idgenero == 'M':
        print('Olá, visitante')
    elif idgenero == 'F':
        print('Olá, visitante')
    else:
        idinfo = input('Insira seu nome:').title()
        print('Olá, {},\n Você tem privilegio de visitante'.format(idinfo).title())
