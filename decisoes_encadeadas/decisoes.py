nome=input('Digite o Nome do paciente  : ')
idade=int(input('Digite a idade do paciente  : '))
doenca_infectocontagiosa=input('Suspeita de doença infectocontagiosa  ?') .upper()
if idade >=65 :
    print('O paciente ' + nome + ' Possui atendimento prioritario .')
elif doenca_infectocontagiosa =='Sim':
    print('O paciente '+ nome + 'deve se direcionado para a sala de espera reservada')
else:
    print('O paciente '+ nome + ' não possui atendimento prioritario e pode aguardar na sala comum !')

