import json, time, random, datetime
from dateutil.relativedelta import relativedelta 

while True:
    print('=' * 30)
    print('{:^30}'.format('CAIXA ELETRÔNICO'))
    print('=' * 30)
    print('Selecione uma das funções:')
    print('....................\n[ 1 ] CRIAR CONTA\n....................\n[ 2 ] EXCLUIR CONTA\n....................\n[ 3 ] CONSULTA DO SALDO\n....................\n[ 4 ] FAZER SAQUE\n....................\n[ 5 ] DEPÓSITO\n....................\n[ 6 ] TRANSFERÊNCIA\n....................')
    
    opçao = int(input('Digite o número correspondente a função desejada: '))
 
    if opçao == 1:                                              #CRIAR CONTA
        contaNova = {}
        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()
        
        bancoDados = json.loads(stringBancoDados)
        gerandoNumeroConta = random.randint(1000, 9999)

        for c in range(len(bancoDados)):
            if gerandoNumeroConta != bancoDados[c]["Num da conta"]:
                time.sleep(1) 
        print('\033[33mGerando número da sua conta.\033[m')
        time.sleep(1)
        print(f'\033[35mSeu número de conta é {gerandoNumeroConta}.\033[m')   
        
        enter = input('Informe os dados que forem pedidos para criação da conta. TECLE ENTER PRA CONTINUAR')
        
        contaNova ['Num da conta'] = int(input('Digite aqui número de conta que foi informado a você: '))
        
        while True: 
            if contaNova ['Num da conta'] == gerandoNumeroConta:
                break
            else:
                print('O número de conta que você digitou, não foi informado!\nPor favor o informe novamente: ')
                contaNova ['Num da conta'] = int(input('Digite o número de conta que foi informado a você: '))
        contaNova ['nome'] = str(input('Digite seu nome completo: '))
        contaNova ['idade'] = int(input('Digite sua idade: '))
        contaNova ['CPF'] = str(input('Informe seu CPF de 5 dígitos: '))
        while True:
            if len(contaNova ['CPF']) == 5:
                break
            else:
                print('\033[31mQuantidade de dígitos inválidas!\033[m\nPor favor digite o CPF novamente de 5 DÍGITOS:')
                contaNova ['CPF'] = str(input('DIgite seu CPF de 5 dígitos: '))
        
        contaNova ['senha'] = str(input('Informe sua senha de 4 dígitos: '))
        while True:
            if len(contaNova ['senha']) == 4:
                while True:
                    if contaNova ['senha'] == contaNova ['CPF'][0:4]:
                        print('\033[31mSua senha não pode ser o seu CPF! DIgite uma outra senha:\033[m')
                        contaNova ['senha'] = str(input('DIgite sua senha de 4 dígitos: '))
                    else: 
                        break
                
                while True:
                    if contaNova ['senha'] == contaNova['CPF'][1:5]:
                        print('\033[31mSua senha não pode ser o seu CPF! Digite outra senha:\033[m')
                        contaNova ['senha'] = str(input('Digite sua senha de 4 dígitos: '))
                    else:
                        break
                break
            else:
                print('\033[31mQuantidade de dígitos inválidas!\033[m\nPor favor digite a senha novamente de 4 DÍGITOS:')
                contaNova ['senha'] = str(input('Digite sua senha: '))
        

        contaNova ['saldo'] = int(0)
        contaNova ['email'] = str(input('Digite aqui o seu EMAIL: '))
        contaNova ['bloqueio'] = int(0)
        contaNova ['ativandoChequeEspecial'] = str(0)
        contaNova ['valorChequeEspecial'] = float(0)

        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()

        if len(stringBancoDados) == 0:
            texto = json.dumps([contaNova]) 
            arq = open("banco-dados.txt", 'w')
            arq.write(texto)
            arq.close()  
            
        if len(stringBancoDados) >= 1:
            bancoDados = json.loads(stringBancoDados)
            string = json.dumps(bancoDados + [contaNova])
            arq = open("banco-dados.txt", 'w')
            arq.write(string)
            arq.close()
        time.sleep(1)
        print('Aguarde ....')
        time.sleep(2)
        print('\033[32mSua conta foi salva com sucesso!\033[m')
        
    if opçao == 2:                                                      #EXCLUIR CONTA
        numDaConta = int(input('Digite o número da sua conta para exclusão: '))

        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()
        bancoDados = json.loads(stringBancoDados)
        contador = 0
        
        for c in range(len(bancoDados)):
            if numDaConta == bancoDados[c]['Num da conta']:
                time.sleep(1)
                confirmandoConta = 'SIM'
                break
            else:
                confirmandoConta = 'NAO'
            contador += 1

        nomeUso = bancoDados[contador]["nome"]

        while True:
            if bancoDados [contador]['bloqueio'] == 0:
                if confirmandoConta == 'SIM':
                    time.sleep(1)
                    confirmandoUsuario = str(input(f"\033[32mSeja Bem Vindo(a) {nomeUso}!\033[m\nTECLE ENTER PARA CONTINUAR!"))

                    time.sleep(1)
                    confirmandoCpfExclusao = str(input('Digite seu CPF para fazermos a exclusão da sua conta: '))
                    
                    if confirmandoCpfExclusao == bancoDados[contador]['CPF']:
                        time.sleep(1)
                        print('\033[33mAguarde...\033[m')
                        time.sleep(1)
                        print('\033[32mCPF CONFIRMADO!\033[m')
                        print('Processo de exclusão iniciado!\n\033[33mAguarde....\033[m')
                        time.sleep(3)
                        
                        bancoDados.pop(contador)
                        arq = open("banco-dados.txt", 'w')
                        salvandoBancoDados = json.dumps(bancoDados)
                        arq.write(salvandoBancoDados)
                        arq.close()

                        print('\033[32mSua conta foi excluída com sucesso!\033[m')
                        break
                    
                    if confirmandoCpfExclusao != bancoDados[contador]['CPF']:
                        time.sleep(1)
                        print('\033[31mCPF INVÁLIDO!\033[m')    
                        break
                
                if confirmandoConta == 'NAO':   
                    time.sleep(1)
                    print('Seu número de conta não foi encontrado!')    
                    break
            else:
                print('\033[31mVocê não pode acessar a sua conta! Ela está BLOQUEADA.\033[m')
                break

    if opçao ==  3:                                        #CONSULTA AO SALDO
        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close() 

        bancoDados = json.loads(stringBancoDados)
        numDaConta = int(input('Qual o número da sua conta: '))

        contador = 0
        for c in range(len(bancoDados)):          
            if numDaConta == bancoDados[c]['Num da conta']:
                contaConfirmada = 'SIM'
                break
            if numDaConta != bancoDados[c]['Num da conta']:
                contaConfirmada = 'NAO'
            contador += 1
            
        while True:
            if contaConfirmada == 'SIM':
                time.sleep(1)
                
                if bancoDados [contador]['bloqueio'] == 0:
                    saldo = bancoDados[contador]['saldo']
                    nomeUsuario = bancoDados[contador]['nome']

                    time.sleep(1)
                    print('\033[32mNúmero de conta confirmado!\033[m')
                    time.sleep(1)
                    confirmandoUsuario = input(f'\033[32mSeja Bem Vindo {nomeUsuario}!\033[m\nTECLE ENTER PARA CONTINUAR!')

                    time.sleep(1)
                    print('\033[33mAguarde ...\033[m')
                    time.sleep(1)
                    confirmandoSenha = str(input('Informe sua senha: '))
                    cont = 0
                    while True:
                        if confirmandoSenha == bancoDados[contador]['senha']:
                            print('\033[32mSenha CONFIRMADA!\033[m')
                            time.sleep(2)
                            print(f'Seu saldo é de R${saldo}.')
                            break

                        if confirmandoSenha != bancoDados[contador]['senha']:
                            print('\033[31mSENHA INVÀLIDA!\033[m')
                            cont += 1
                            print('Digite a senha novamente')
                            confirmandoSenha = str(input('Informe sua senha: '))
                            if cont == 3: 
                                print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                print('Você digitou a senha errada mais de três vezes!\nSua conta foi bloqueada por questões de segurança.')
                                dataBloqueio = datetime.datetime.now()
                                data_str = dataBloqueio.__str__()
                                bancoDados [contador]['bloqueio'] = data_str
                            
                                arq = open("banco-dados.txt", 'w')
                                salvandoBancoDados = json.dumps(bancoDados)
                                arq.write(salvandoBancoDados)
                                arq.close()
                                break
                else:
                    time.sleep(1)
                    print('\033[31mVocê não pode acessar a sua conta! Ela está BLOQUEADA.\033[m')
                    break

            if contaConfirmada == 'NAO':
                time.sleep(1)
                print('\033[31mNúmero de conta informado é INVÁLIDO!\033[m') 
            break
            
    if opçao == 4:                                           #FAZER SAQUE
        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()

        numDaConta = int(input('Qual é o número da sua conta? '))
        bancoDados = json.loads(stringBancoDados)
        contador = 0

        for c in range(len(bancoDados)):
            if numDaConta == bancoDados[c]['Num da conta']:
                contaConfirmada = 'SIM'                                                                                                    
                break
            else:
                contaConfirmada = 'NAO'    
            contador += 1

        while True:
            if contaConfirmada == 'SIM':
                time.sleep(1)
                print('\033[32mNÚMERO DE CONTA CONFIRMADO\033[m')
                
                if bancoDados [contador]['bloqueio'] == 0:
                    if bancoDados [contador]['ativandoChequeEspecial'] == '0':    
                        time.sleep(1)
                        print('''\033[33mCédulas disponíveis de:\nR$ 100\nR$ 50\nR$ 20\nR$ 10\nR$ 5\nO VALOR DO SAQUE PRECISA TERMINAR EM 0 OU 5!\033[m ''')
                        time.sleep(1)
                        valorDoSaque = int(input('Digite aqui o valor do saque desejado: R$'))
                        verificandoSaque = valorDoSaque % 5

                        if valorDoSaque <= bancoDados[contador]['saldo']:
                            time.sleep(1)
                            confirmandoSenha = str(input('Digite a sua senha? '))      
                            
                            while True:
                                cont = 0
                                if confirmandoSenha == bancoDados [contador]['senha']:    
                                    while True: 
                                        if verificandoSaque == 0:      
                                            time.sleep(1)
                                            print('\033[32mSENHA CONFIRMADA...\033[m')
                                            bancoDados[contador]['saldo'] -= valorDoSaque
                                            
                                            arq = open("banco-dados.txt", 'w')
                                            salvandoBancoDados = json.dumps(bancoDados)
                                            arq.write(salvandoBancoDados)
                                            arq.close()

                                            valorTotal = valorDoSaque
                                            cedula = 100
                                            contadorDeCedula = 0

                                            while True:
                                                if valorTotal >= cedula:
                                                    valorTotal -= cedula
                                                    contadorDeCedula += 1
                                                else:
                                                    if contadorDeCedula > 0:
                                                        print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                        time.sleep(1)
                                                    if cedula == 100:
                                                        cedula = 50   
                                                    elif cedula == 50:
                                                        cedula = 20                
                                                    elif cedula == 20:
                                                        cedula = 10               
                                                    elif cedula == 10:
                                                        cedula = 5
                                                    elif cedula == 5: 
                                                        cedula = 0
                                                    contadorDeCedula = 0
                                                    if valorTotal == 0:
                                                        break
                                            
                                            print(f'O seu saque de R${valorDoSaque}, foi realizado com \033[32mSUCESSO!\033[m')   
                                            break
                                            
                                        if verificandoSaque != 5 or 0:
                                            restoSaque = valorDoSaque % 5
                                            novoValorDoSaque = valorDoSaque - restoSaque + 5
                                            novoValorSaque2 = valorDoSaque - restoSaque                                                                                                                                                                                               
                                            time.sleep(1)   
                                            escolhaDeSaque = int(input(f'\033[33mSeu valor de saldo não pode ser efetuado!\033[m\nEscolha um novo valor de saldo: saldo 1 \033[32mR${novoValorSaque2}\033[m; saldo 2 \033[33mR${novoValorDoSaque}\033[m: ESCOLHA [1 / 2]:'))
                                            time.sleep(1.5)
                                            
                                            if escolhaDeSaque == 1:
                                                print('AGUARDE...')
                                                time.sleep(1)
                                                bancoDados[contador]['saldo'] -= novoValorSaque2
                                                    
                                                arq = open("banco-dados.txt", 'w')
                                                salvandoBancoDados = json.dumps(bancoDados)
                                                arq.write(salvandoBancoDados)
                                                arq.close()

                                                valorTotal = novoValorSaque2
                                                cedula = 100
                                                contadorDeCedula = 0

                                                while True:
                                                    if valorTotal >= cedula:
                                                        valorTotal -= cedula
                                                        contadorDeCedula += 1
                                                    else:
                                                        if contadorDeCedula > 0:
                                                            print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                            time.sleep(1)
                                                        if cedula == 100:
                                                            cedula = 50   
                                                        elif cedula == 50:
                                                            cedula = 20                
                                                        elif cedula == 20:
                                                            cedula = 10               
                                                        elif cedula == 10:
                                                            cedula = 5
                                                        elif cedula == 5: 
                                                            cedula = 0
                                                        contadorDeCedula = 0
                                                        if valorTotal == 0:
                                                            break
                                                print(f'Seu saque de R${novoValorSaque2}, foi realizado com \033[32mSUCESSO\033[m!')
                                                break
                                            
                                            if escolhaDeSaque == 2:
                                                print('AGUARDE...')
                                                time.sleep(1)
                                                bancoDados[contador]['saldo'] -= novoValorDoSaque
                                                    
                                                arq = open("banco-dados.txt", 'w')
                                                salvandoBancoDados = json.dumps(bancoDados)
                                                arq.write(salvandoBancoDados)
                                                arq.close()

                                                valorTotal = novoValorDoSaque
                                                cedula = 100
                                                contadorDeCedula = 0

                                                while True:
                                                    if valorTotal >= cedula:
                                                        valorTotal -= cedula
                                                        contadorDeCedula += 1
                                                    else:
                                                        if contadorDeCedula > 0:
                                                            print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                            time.sleep(1)
                                                        if cedula == 100:
                                                            cedula = 50   
                                                        elif cedula == 50:
                                                            cedula = 20                
                                                        elif cedula == 20:
                                                            cedula = 10               
                                                        elif cedula == 10:
                                                            cedula = 5
                                                        elif cedula == 5:
                                                            cedula = 0
                                                        contadorDeCedula = 0
                                                        if valorTotal == 0:
                                                            break
                                                print(f'Seu saque de R${novoValorDoSaque}, foi realizado com \033[32mSUCESSO\033[m!')
                                                break
                                        break        
                                    break
                                
                                if confirmandoSenha != bancoDados [contador]['senha']:
                                    print('SENHA DIGITADA INVÁLIDA!')
                                    cont+=1
                                    confirmandoSenha = str(input('Informe sua senha novamente: '))
                                    if cont == 3:
                                        print('TENTATIVAS EXPIRADAS!')
                                        print('Você digitou sua senha errada mais de três vezes!Sua conta foi bloqueada por questões de segurança.')
                                        dataBloqueio = datetime.datetime.now()
                                        str_data = dataBloqueio.strftime("%d/%m/%Y, %H:%M")
                                        bancoDados [contador]['bloqueio'] = str_data

                                        arq = open('banco-dados.txt', 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        break
                                break
                        
                        if valorDoSaque > bancoDados [contador]['saldo']:
                            print('\033[31mSeu saldo é inválido!\033[m')
                            time.sleep(1.5)
                            confirmando_cheque_especial = str(input('Você deseja ativar o cheque especial de R$100.00? DIGITE [S/N]: ')).upper()
                            time.sleep(1.5)

                            if confirmando_cheque_especial == 'S':
                                    time.sleep(1.5)
                                    print('\033[32mO CHEQUE ESPECIAL FOI ATIVADO!\033[m')
                                    time.sleep(1.5)
                                    confirmandoSenha = str(input('Digite sua senha: ')).strip()
                                    cont =  0 
                                    while True:
                                        if confirmandoSenha == bancoDados[contador]['senha']:
                                            time.sleep(1.5)
                                            cheque_especial = 100.0

                                            bancoDados [contador]['saldo'] += cheque_especial
                                            
                                            if valorDoSaque <= bancoDados [contador]['saldo']:
                                                data_ativacao_cheque_especial = datetime.datetime.now()
                                                str_data = data_ativacao_cheque_especial.strftime("%d/%m/%Y, %H:%M")         # SALVANDO DATA DA ATIVAÇÃO CHEQUE ESPECIAL
                                                bancoDados [contador]['ativandoChequeEspecial'] = str_data
                                                print('\033[32mSAQUE APROVADO!\033[m')
  
                                                while True: 
                                                    if verificandoSaque == 0:      
                                                        time.sleep(1)
                                                        print('\033[32mSENHA CONFIRMADA...\033[m')
                                                        
                                                        bancoDados [contador]['saldo'] -= valorDoSaque          
                                                        bancoDados [contador]['saldo'] -= cheque_especial
                                                        bancoDados [contador]['valorChequeEspecial'] = bancoDados [contador]['saldo']
                                                        
                                                        arq = open("banco-dados.txt", 'w')
                                                        salvandoBancoDados = json.dumps(bancoDados)
                                                        arq.write(salvandoBancoDados)
                                                        arq.close()

                                                        valorTotal = valorDoSaque
                                                        cedula = 100
                                                        contadorDeCedula = 0

                                                        while True:
                                                            if valorTotal >= cedula:
                                                                valorTotal -= cedula
                                                                contadorDeCedula += 1
                                                            else:
                                                                if contadorDeCedula > 0:
                                                                    print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                                    time.sleep(1)
                                                                if cedula == 100:
                                                                    cedula = 50   
                                                                elif cedula == 50:
                                                                    cedula = 20                
                                                                elif cedula == 20:
                                                                    cedula = 10               
                                                                elif cedula == 10:
                                                                    cedula = 5
                                                                elif cedula == 5: 
                                                                    cedula = 0
                                                                contadorDeCedula = 0
                                                                if valorTotal == 0:
                                                                    break
                                                        print(f'O seu saque de R${valorDoSaque}, foi realizado com \033[32mSUCESSO!\033[m')   
                                                        break
                                        
                                                    if verificandoSaque != 5 or 0:
                                                        restoSaque = valorDoSaque % 5
                                                        novoValorDoSaque = valorDoSaque - restoSaque + 5
                                                        novoValorSaque2 = valorDoSaque - restoSaque                                                                                                                                                                                               
                                                        time.sleep(1)   
                                                        escolhaDeSaque = int(input(f'Seu valor de saldo não pode ser efetuado!\nEscolha um novo valor de saldo: saldo 1 \033[32mR${novoValorSaque2}\033[m; saldo 2 \033[33mR${novoValorDoSaque}\033[m: ESCOLHA [1 / 2]:'))
                                                        time.sleep(1.5)
                                                        
                                                        if escolhaDeSaque == 1:
                                                            print('AGUARDE...')
                                                            time.sleep(1)
                                                            bancoDados[contador]['saldo'] -= novoValorSaque2
                                                            bancoDados[contador]['saldo'] -= cheque_especial
                                                            bancoDados [contador]['valorChequeEspecial'] = bancoDados [contador]['saldo']
                                                                
                                                            arq = open("banco-dados.txt", 'w')
                                                            salvandoBancoDados = json.dumps(bancoDados)
                                                            arq.write(salvandoBancoDados)
                                                            arq.close()

                                                            valorTotal = novoValorSaque2
                                                            cedula = 100
                                                            contadorDeCedula = 0

                                                            while True:
                                                                if valorTotal >= cedula:
                                                                    valorTotal -= cedula
                                                                    contadorDeCedula += 1
                                                                else:
                                                                    if contadorDeCedula > 0:
                                                                        print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                                        time.sleep(1)
                                                                    if cedula == 100:
                                                                        cedula = 50   
                                                                    elif cedula == 50:
                                                                        cedula = 20                
                                                                    elif cedula == 20:
                                                                        cedula = 10               
                                                                    elif cedula == 10:
                                                                        cedula = 5
                                                                    elif cedula == 5: 
                                                                        cedula = 0
                                                                    contadorDeCedula = 0
                                                                    if valorTotal == 0:
                                                                        break
                                                            print(f'Seu saque de R${novoValorSaque2}, foi realizado com \033[32mSUCESSO\033[m!')
                                                            break
                                                        
                                                        if escolhaDeSaque == 2:
                                                            print('AGUARDE...')
                                                            time.sleep(1)
                                                            bancoDados[contador]['saldo'] -= novoValorDoSaque
                                                            bancoDados[contador]['saldo'] -= cheque_especial
                                                            bancoDados [contador]['valorChequeEspecial'] = bancoDados [contador]['saldo']
                                                                
                                                            arq = open("banco-dados.txt", 'w')
                                                            salvandoBancoDados = json.dumps(bancoDados)
                                                            arq.write(salvandoBancoDados)
                                                            arq.close()

                                                            valorTotal = novoValorDoSaque
                                                            cedula = 100
                                                            contadorDeCedula = 0

                                                            while True:
                                                                if valorTotal >= cedula:
                                                                    valorTotal -= cedula
                                                                    contadorDeCedula += 1
                                                                else:
                                                                    if contadorDeCedula > 0:
                                                                        print(f'O dinheiro irá sair em: {contadorDeCedula} cédulas de R${cedula}. ')
                                                                        time.sleep(1)
                                                                    if cedula == 100:
                                                                        cedula = 50   
                                                                    elif cedula == 50:
                                                                        cedula = 20                
                                                                    elif cedula == 20:
                                                                        cedula = 10               
                                                                    elif cedula == 10:
                                                                        cedula = 5
                                                                    elif cedula == 5:
                                                                        cedula = 0
                                                                    contadorDeCedula = 0
                                                                    if valorTotal == 0:
                                                                        break
                                                            print(f'Seu saque de R${novoValorDoSaque}, foi realizado com \033[32mSUCESSO\033[m!')
                                                            break
                                                    break
                                                break

                                            else:
                                                print('\033[31mSEU SALDO É INSUFICIENTE, MESMO COM O CHEQUE ESPECIAL!\033[m')
                                                time.sleep(1.5)
                                                break
                                            
                                        if confirmandoSenha != bancoDados[contador]['senha']:
                                            print('\033[31mSENHA INVÁLIDA!\033[m')
                                            cont += 1
                                            print('Digite a senha novamente')
                                            confirmandoSenha = str(input('Informe sua senha: '))
                                            if cont == 3: 
                                                print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                                print('Você digitou a senha errada mais de três vezes!\nSua conta foi bloqueada por questões de segurança.')
                                                dataBloqueio = datetime.datetime.now()
                                                str_data = dataBloqueio.strftime("%d/%m/%Y, %H:%M")
                                                bancoDados [contador]['bloqueio'] = str_data
                                            
                                                arq = open("banco-dados.txt", 'w')
                                                salvandoBancoDados = json.dumps(bancoDados)
                                                arq.write(salvandoBancoDados)
                                                arq.close()
                                                break   
                                        
                            if confirmando_cheque_especial == 'N':
                                print('\033[33mO cheque Especial não foi ativado!\033[m \nPor tanto a não é possível realizar o saque.')   
                                break 
                        break
                    
                    if bancoDados [contador]['ativandoChequeEspecial'] != '0':
                        time.sleep(1.5)
                        print('\033[31mVOCÊ NAÕ PODE REALIZAR SAQUES ENQUANTO NÃO QUITAR O VALOR QUE FOI PEGO NO CHEQUE ESPECIAL!\033[m\nO pagamento do cheque especial é realizado na área de deposito.')
                        time.sleep(1)
                        print(f"\033[33mVocê ainda não pagou o valor gasto do cheque especial, para utilizá-lo novamente \nvocê deve pagar o valor usado do cheque especial que foi de RS{bancoDados [contador]['saldo']}\033[m")
                        break

                else:
                    time.sleep(2)
                    print('\033[31mVocê não pode acessar a sua conta, ela está BLOQUEADA.\033[m')
                    break
            
            if contaConfirmada == 'NAO':
                time.sleep(1)
                print('\033[31mO NÚMERO DE CONTA NÃO FOI ENCONTRADO!\033[m')
                break
            break
    
    if opçao == 5:                                                      #DEPÓSITO
        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()

        bancoDados = json.loads(stringBancoDados)
        numDaConta = int(input('Digite o número da sua conta: '))    
        contador = 0
        for c in range(len(bancoDados)):
            if numDaConta == bancoDados[c]['Num da conta']:
                conta = 'sim'
                break
            else:
                conta = 'nao'
            contador += 1

        while True:
            if conta == 'sim':
                if bancoDados [contador]['bloqueio'] == 0:
                    if bancoDados[contador]['ativandoChequeEspecial'] == '0':
                        time.sleep(1)
                        print('\033[32mNÚMERO DE CONTA CONFIRMADO!\033[m')
                        time.sleep(3)
                        confirmandoCpf = str(input('Confirme o seu CPF: '))

                        if confirmandoCpf == bancoDados[contador]['CPF']:
                            time.sleep(1)
                            print('\033[32mSeu CPF Foi VALIDADO!\033[m')
                            time.sleep(1)
                            print('\033[33mAguarde......\033[m')
                            time.sleep(1)
                            valorDoDeposito = int(input('Digite o valor de depósito desejado: '))
                            time.sleep(1)
                            confirmandoSenha = str(input('Digite a sua senha: '))
                            cont = 0
                            
                            while True:
                                if confirmandoSenha == bancoDados[contador]['senha']:  
                                    time.sleep(1)  
                                    print('\033[32mSENHA CONFIRMADA!\033[m')
                                    bancoDados[contador]['saldo'] += valorDoDeposito
                                    arq = open("banco-dados.txt", 'w')
                                    salvandoBancoDados = json.dumps(bancoDados)
                                    arq.write(salvandoBancoDados)
                                    arq.close()
                                    time.sleep(2)
                                    print(f'O depósito de R${valorDoDeposito}, foi realizado com \033[32mSUCESSO!\033[m')
                                    break

                                if confirmandoSenha != bancoDados[contador]['senha']:
                                    print('\033[31mSENHA INVÁLIDA!\033[m')
                                    cont += 1
                                    print('Digite-a novamente ')
                                    time.sleep(2)
                                    confirmandoSenha = str(input('Informe sua senha: '))

                                    if cont == 3:
                                        print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                        time.sleep(1)
                                        print('Você digitou sua senha errada mais de três vezes! Sua coonta foi BLOQUEADA por medidas de segurança.')
                                        dataBloqueio = datetime.datetime.now()
                                        str_data = dataBloqueio.__str__()
                                        bancoDados [contador]['bloqueio'] = str_data

                                        arq = open('banco-dados.txt', 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        break
                                break

                        if confirmandoCpf != bancoDados[contador]['CPF']:
                            time.sleep(2)
                            print('\033[31mO CPF digitado é INVÁLIDO!\033[m')
                            break
                        break
                    
                    if bancoDados[contador]['ativandoChequeEspecial'] != '0':
                        data_atual = datetime.datetime.now()
                        data_cheque_especial = bancoDados[contador]['ativandoChequeEspecial']   
                        data_atual_str = data_atual.strftime("%d/%m/%Y, %H:%M")
                        data_cheque_especial_str = datetime.datetime.strptime(data_cheque_especial, "%d/%m/%Y, %H:%M")
                        
                        comparacao = relativedelta(data_atual, data_cheque_especial_str)
                        analisando_anos = comparacao.years

                        if analisando_anos != 0:
                            dias = comparacao.days
                            quantidade_dias = analisando_anos * 365 + dias

                        if analisando_anos == 0:
                            quantidade_dias = comparacao.days
                        
                        if quantidade_dias > 5:
                            valor_usado_cheque = float(bancoDados[contador]['valorChequeEspecial'])

                            taxa_juros = 0.1
                            
                            valor_juros_sem_formatacao = valor_usado_cheque * (1 + taxa_juros) ** quantidade_dias
                            valor_juros_formatado = "{:.2f}".format(valor_juros_sem_formatacao)
                            bancoDados[contador]['saldo'] = valor_juros_formatado   
                            
                            time.sleep(1.5)
                            print('\033[31mVOCÊ ESTÁ DEVENDO O VALOR DO CHEQUE ESPECIAL!\033[m\n')
                            time.sleep(1)
                            print(f'Você tem saldo \033[31mnegativo de R${valor_juros_formatado}\033[m, já com a aplicação dos juros.')
                            time.sleep(0.5)
                            print('\033[33mAguarde......\033[m')
                            time.sleep(2)
                            
                            valorDoDeposito = float(input('Digite o valor de depósito desejado: '))
                            time.sleep(1)
                            confirmandoSenha = str(input('Digite a sua senha: '))
                            cont = 0
                            
                            while True:
                                if confirmandoSenha == bancoDados[contador]['senha']:  
                                    time.sleep(1)
                                    print('\033[32mSENHA CONFIRMADA!\033[m')
                                    time.sleep(1)
                                    print('\033[33m O valor que será depositado servirá para quitar o valor pego do cheque especial.\033[m')
                                    time.sleep(1.5) 
                                    bancoDados_saldo = float(bancoDados[contador]['saldo'])
                                    bancoDados_saldo += valorDoDeposito
                                    bancoDados [contador]['saldo'] = bancoDados_saldo
                                    
                                    if bancoDados_saldo < 0:
                                        time.sleep(1)
                                        arq = open("banco-dados.txt", 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()

                                        print('\033[32mDEPÓSITO REALIZADO COM SUCESSO!\033[m')
                                        time.sleep(2)
                                        print(f'\033[33mO valor de depósito, não foi o suficiente para quitar o valor utilizado do cheque especial.\033[m\nO valor que você está devendo é de \033[31mR${bancoDados[contador]["saldo"]}.\033[m')
                                        break

                                    if bancoDados_saldo >= 0:
                                        time.sleep(1)
                                        print('\033[32mO valor utilizado do cheque especial foi quitado com SUCESSO!\033[m')                                        
                                        bancoDados[contador]['ativandoChequeEspecial'] = '0'
                                        bancoDados[contador]['valorChequeEspecial'] = 0.0
                                        arq = open("banco-dados.txt", 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        time.sleep(2)
                                        print(f'O depósito de R${valorDoDeposito}, foi realizado com \033[32mSUCESSO!\033[m')
                                        break

                                if confirmandoSenha != bancoDados[contador]['senha']:
                                    print('SENHA INVÁLIDA!')
                                    cont += 1
                                    print('Digite-a novamente ')
                                    time.sleep(2)
                                    confirmandoSenha = str(input('Informe sua senha: '))

                                    if cont == 3:
                                        print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                        time.sleep(1)
                                        print('Você digitou sua senha errada mais de três vezes! Sua coonta foi BLOQUEADA por medidas de segurança.')
                                        dataBloqueio = datetime.datetime.now()
                                        str_data = dataBloqueio.__str__()
                                        bancoDados [contador]['bloqueio'] = str_data

                                        arq = open('banco-dados.txt', 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        break
                        
                        if quantidade_dias <= 5:
                            time.sleep(1)
                            print('\033[33mO juros ainda não foi aplicado no valor que você utilizou do cheque!\033[m ')
                            
                            print('Aguarde......')
                            time.sleep(1)
                            valorDoDeposito = int(input('Digite o valor de depósito desejado: '))
                            time.sleep(1)
                            confirmandoSenha = str(input('Digite a sua senha: '))
                            
                            cont = 0
                            while True:
                                if confirmandoSenha == bancoDados[contador]['senha']:  
                                    time.sleep(1)  
                                    print('\033[32mSENHA CONFIRMADA!\033[m')
                                    bancoDados_saldo = bancoDados[contador]['saldo']
                                    bancoDados_saldo += valorDoDeposito
                                    bancoDados [contador]['saldo'] = bancoDados_saldo
                                    
                                    if bancoDados_saldo >= 0:
                                        time.sleep(1)
                                        print('\033[32mO valor utiizado do CHEQUE ESPECIAL foi QUITADO com SUCESSO!\033[m')
                                        time.sleep(1)
                                        print('\033[33mAguarde....\033[m')
                                        bancoDados [contador]['ativandoChequeEspecial'] = '0'
                                        bancoDados [contador]['valorChequeEspecial'] = 0.0
                                        arq = open("banco-dados.txt", 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        time.sleep(2)
                                        print(f'O depósito de R${valorDoDeposito}, foi realizado com \033[32mSUCESSO!\033[m')
                                        break
                                    
                                    if bancoDados_saldo < 0:
                                        time.sleep(1)
                                        print('\033[32mDEPÓSITO REALIZADO COM SUCESSO!\033[m')
                                        time.sleep(1)
                                        arq = open("banco-dados.txt", 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()

                                        time.sleep(2)
                                        print(f'\033[33mO valor de depósito, não foi o suficiente para quitar o valor utilizado do cheque especial.\033[m\nO valor que você está devendo é de \033[31mR${bancoDados[contador]["saldo"]}.\033[m')
                                        break

                                if confirmandoSenha != bancoDados[contador]['senha']:
                                    print('SENHA INVÁLIDA!')
                                    cont += 1
                                    print('Digite-a novamente ')
                                    time.sleep(2)
                                    confirmandoSenha = str(input('Informe sua senha: '))

                                    if cont == 3:
                                        print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                        time.sleep(1)
                                        print('Você digitou sua senha errada mais de três vezes! Sua coonta foi BLOQUEADA por medidas de segurança.')
                                        dataBloqueio = datetime.datetime.now()
                                        str_data = dataBloqueio.__str__()
                                        bancoDados [contador]['bloqueio'] = str_data

                                        arq = open('banco-dados.txt', 'w')
                                        salvandoBancoDados = json.dumps(bancoDados)
                                        arq.write(salvandoBancoDados)
                                        arq.close()
                                        break

                            break
            
                else:
                    print('Você não pode acessar sua conta! ELA ESTÁ BLOQUEADA! ')
                    break
            
            if conta == 'nao':
                time.sleep(1)
                print('\033[31mO NÚMERO DE CONTA DIGITADO É INVALIDO!\033[m')
                time.sleep(1)
                break

            break

    if opçao == 6:                                        #TRANSFERÊNCIA
        arq = open("banco-dados.txt", 'r')
        stringBancoDados = arq.read()
        arq.close()

        bancoDados = json.loads(stringBancoDados)
        numDaMinhaConta = int(input('Digite o número da sua conta: '))

        contador = 0
        for c in range(len(bancoDados)):
            if numDaMinhaConta == bancoDados[c]['Num da conta']:
                contaConfirmada = 'SIM'
                break
            else:
                contaConfirmada = 'NAO'
            contador += 1
        
        if contaConfirmada == 'SIM':
            time.sleep(1)
            print('\033[32mNÚMERO DE CONTA CONFIRMADO\033[m')
            if bancoDados[contador]['ativandoChequeEspecial'] == '0':
                time.sleep(1)
                while True:
                    if bancoDados [contador]['bloqueio'] == 0:              
                        time.sleep(1)
                        confirmandoMinhaSenha = str(input('Digite a sua senha: '))
                        cont = 0
                        while True:
                            if confirmandoMinhaSenha == bancoDados[contador]['senha']:
                                time.sleep(2)
                                print('\033[32mSENHA VALIDADA!\033[m')
                                time.sleep(3)
                                numContaTransferencia = int(input('Qual é o número da conta do favorecido? '))
                                
                                contadorPraTransferencia = 0
                                for c in range(len(bancoDados)): 
                                    if numContaTransferencia == bancoDados[c]['Num da conta']:
                                        contaConfirmada2 = 'SIM'
                                        break
                                    else:
                                        contaConfirmada2 = 'NAO'
                                    contadorPraTransferencia += 1

                                if contaConfirmada2 == 'SIM':
                                    if bancoDados [contadorPraTransferencia]['bloqueio'] == 0:
                                        time.sleep(1)
                                        nomeDoFavorecido = bancoDados[contadorPraTransferencia]['nome']
                                        verificandoUsuario = str(input(f'\033[33mO nome do favorecido é "{nomeDoFavorecido}"?\033[m Digite [S/N]:')).strip().upper()[0]
                                        
                                        if verificandoUsuario == 'S':
                                            time.sleep(1)
                                            print('\033[32mFAVORECIDO VALIDADO!\033[m\n\033[33mAguarde...\033[m')
                                            time.sleep(1)
                                            valorTransferencia = int(input('Digite o valor da transferência: R$'))

                                            if valorTransferencia <= bancoDados[contador]['saldo']:
                                                time.sleep(1)
                                                confirmandoCpfDoFavorecido = str(input('Digite o CPF do favorecido: '))

                                                if confirmandoCpfDoFavorecido == bancoDados[contadorPraTransferencia]['CPF']:
                                                    print('\033[32mCPF CONFIRMADO!\033[m')
                                                    time.sleep(1)
                                                    print('Transfência sendo realizada!')
                                                    time.sleep(1)
                                                    
                                                    arq = open("banco-dados.txt", 'w')
                                                    bancoDados[contador]['saldo'] -= valorTransferencia
                                                    bancoDados[contadorPraTransferencia]['saldo'] += valorTransferencia
                                                    salvandoBancoDados = json.dumps(bancoDados)
                                                    arq.write(salvandoBancoDados)
                                                    arq.close()
                                                    print(f'A transferência de R${valorTransferencia}, foi realizada com \033[32mSUCESSO!\033[m')
                                                    break

                                                if confirmandoCpfDoFavorecido != bancoDados[contadorPraTransferencia]['CPF']:
                                                    time.sleep(1)
                                                    print('\033[31mO CPF digitado é INVÁLIDO!\033[m')
                                                    break

                                            if valorTransferencia > bancoDados[contador]['saldo']:
                                                print('\033[31mSALDO INVÁLIDO!\033[m')
                                                time.sleep(1)
                                                confirmando_cheque_especial = str(input('Você deseja ativar o cheque especial? DIGITE [S/N]: ')).upper()
                                                time.sleep(1.5)
                                                        
                                                if confirmando_cheque_especial == 'S':
                                                    time.sleep(1)
                                                    print('\033[32mO CHEQUE ESPECIAL FOI ATIVADO!\033[m')
                                                    time.sleep(1.5)
                                                    confirmandoSenha = str(input('Digite sua senha novamente: ')).strip()
                                                    cont =  0 
                                                    while True:
                                                        if confirmandoSenha == bancoDados[contador]['senha']:
                                                            time.sleep(1.5)
                                                            cheque_especial = 100.0

                                                            bancoDados [contador]['saldo'] += cheque_especial
                                                            
                                                            data_ativacao_cheque_especial = datetime.datetime.now()
                                                            str_data = data_ativacao_cheque_especial.strftime("%d/%m/%Y, %H:%M")         # SALVANDO DATA DA ATIVAÇÃO CHEQUE ESPECIAL
                                                            bancoDados [contador]['ativandoChequeEspecial'] = str_data
                                                            print('\033[32mSAQUE APROVADO!\033[m')
                                                                            
                                                            time.sleep(1)
                                                            
                                                            bancoDados [contador]['saldo'] -= valorTransferencia       
                                                            bancoDados [contador]['saldo'] -= cheque_especial
                                                            bancoDados [contador]['valorChequeEspecial'] = bancoDados [contador]['saldo']

                                                            time.sleep(1)
                                                            confirmandoCpfDoFavorecido = str(input('Digite o CPF do favorecido: '))

                                                            if confirmandoCpfDoFavorecido == bancoDados[contadorPraTransferencia]['CPF']:
                                                                print('\033[32mCPF CONFIRMADO!\033[m')
                                                                time.sleep(1)
                                                                print('Transfência sendo realizada!')
                                                                time.sleep(1)
                                                                
                                                                arq = open("banco-dados.txt", 'w')
                                                                bancoDados[contadorPraTransferencia]['saldo'] += valorTransferencia
                                                                salvandoBancoDados = json.dumps(bancoDados)
                                                                arq.write(salvandoBancoDados)
                                                                arq.close()
                                                                print(f'A transferência de R${valorTransferencia}, foi realizada com \033[32mSUCESSO!\033[m')
                                                                break

                                                            if confirmandoCpfDoFavorecido != bancoDados[contadorPraTransferencia]['CPF']:
                                                                time.sleep(1)
                                                                print('\033[31mO CPF digitado é INVÁLIDO!\033[m')
                                                                break
                                                            break

                                                        if confirmandoSenha != bancoDados[contador]['senha']:
                                                            print('\033[31mSENHA INVÁLIDA!\033[m')
                                                            cont += 1
                                                            print('Digite-a novamente ')
                                                            time.sleep(2)
                                                            confirmandoSenha = str(input('Informe sua senha: '))

                                                            if cont == 3:
                                                                print('\033[31mTENTATIVAS EXPIRADAS!\033[m')
                                                                time.sleep(1)
                                                                print('Você digitou sua senha errada mais de três vezes! Sua coonta foi BLOQUEADA por medidas de segurança.')
                                                                dataBloqueio = datetime.datetime.now()
                                                                str_data = dataBloqueio.__str__()
                                                                bancoDados [contador]['bloqueio'] = str_data

                                                                arq = open('banco-dados.txt', 'w')
                                                                salvandoBancoDados = json.dumps(bancoDados)
                                                                arq.write(salvandoBancoDados)
                                                                arq.close()
                                                                break   
                                                
                                                if confirmando_cheque_especial == 'N':
                                                    time.sleep(1)
                                                    print('\033[33mSeção de transferência encerrada!\033[m')
                                                    break
                                        
                                        if verificandoUsuario == 'N':
                                            time.sleep(1)
                                            print('\033[32mOBRIGADO POR INFORMAR QUE NÃO ERA O FAVORECIDO QUE DESEJAVA!\033[m')
                                            break
                                    
                                    else:
                                        time.sleep(1)
                                        print('\033[31mVocê não pode realizar a transfência para este favorecido, pois a conta dele está bloqueada.\033[m')
                                        break
                                
                                if contaConfirmada2 == 'NAO':
                                    time.sleep(1)
                                    print('\033[31mNÚMERO DE CONTA DIGITADO É INVÁLIDO!\033[m')
                                    break

                            if confirmandoMinhaSenha != bancoDados [contador]['senha']:
                                print('\033[31mSENHA DIGITADA INVÁLIDA!\033[m')
                                time.sleep(1)
                                cont += 1
                                time.sleep(1)                        
                                confirmandoMinhaSenha = str(input('Informe sua senha:'))
                                if cont == 3:
                                    print('TENTATIVAS EXPIRADAS!')
                                    time.sleep(1)
                                    print('Você digitou sua senha errada mais de três vezes! Sua conta foi BLOQUEADA por medidas de segurança.')

                                    dataBloqueio = datetime.datetime.now()
                                    str_data = dataBloqueio
                                    bancoDados [contador]['bloqueio'] = str_data

                                    arq = open("banco-dados.txt", 'w')
                                    salvandoBancoDados = json.dumps(bancoDados)
                                    arq.write(bancoDados)
                                    arq.close()
                                    break

                    else:
                        print('\033[31mvocê não pode acessar sua conta! ELA ESTÁ BLOQUEADA.\033[m')
                        break                   
                    break
                   
            if bancoDados[contador]['ativandoChequeEspecial'] != '0':
                time.sleep(1.5)
                print('\033[31mVOCÊ NAÕ PODE REALIZAR SAQUES ENQUANTO NÃO QUITAR O VALOR QUE FOI PEGO NO CHEQUE ESPECIAL!\033[m')
                time.sleep(1)
                print(f"\033[33mVocê ainda não pagou o valor gasto do cheque especial, para utilizá-lo novamente \nvocê deve pagar o valor usado do cheque especial que foi de RS{bancoDados [contador]['saldo']}\033[m")
                break
        
        if contaConfirmada == 'NAO':
            time.sleep(1)
            print('\033[31mO NÚMERO DE CONTA DIGITADO É INVÁLIDO!\033[m')
            break

    time.sleep(3)
    parada = input(str('Você deseja continuar no Caixa Eletrônico? Digite [S/N]: ')).strip().upper()[0]
    if parada == 'N':
        time.sleep(2)
        print('\033[32mCaixa Eletrônico encerrado! \033[m')
        break
