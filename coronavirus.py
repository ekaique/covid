print('Bem-vindo(a) ao Hospital Referencia \n CENTRAL DE TRIAGEM')
nmpaciente = input('Insira seu nome? ')
idadepaciente = int(input('Qual a sua idade?'))
infopaciente = input('Tem bronquite? ou asma?').upper()


if infopaciente != 'SIM' and infopaciente != 'NAO':
    print('Digite somente sim ou não')
    exit()  

if idadepaciente >=60 or idadepaciente < 15 :
    print('Olá, \n{} Você está na fila preferencial'.format(nmpaciente.title()))
elif infopaciente == 'SIM':
    print('Olá, \n{} Você está na fila prioritaria devido ao Grupo de risco')
else:
    print('Olá, \n{} Você está na fila comum'.format(nmpaciente.title()))
 
