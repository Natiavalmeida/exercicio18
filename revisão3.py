'''Maquina de cafe:
    1º Pedir o numero do produto
    2º valor do produto
    3º Inserir o cartao
    4º Senha do cartao
    5º Entregar o produto
'''

# Produtos disponiveis 
produtos = ['café', 'capuccino', 'café com leite','chocolate']
#Senha do cartão do usuário
senhaCorreta = 1234

def pagamento():
    #Insira o cartão
    print('insira o cartao')
    #conferindo a senha
    senha = input("Digite sua senha: ")
    if (senha == str(senhaCorreta)):
        print('Senha confirmada. Espere a entrega do produto.')
    else:
        print('senha incorreta, por favor tente novamente')
        menuprincipal()

#Inicio da função menu pricipal
def menuprincipal():
    opcao = input('Menu: 1. Café (R$ 2,00) | 2. Capuccino (R$ 3,50) | 3.Café com Leite ( R$4,00 ) | 4. Chocolate ( R$4,50 ) | 5. Sair | Digite o número do produto:')
    #chamando a função "Menu principal"

    if(opcao == '1'):
    #opcao 1. café
        print('voce escolheu: '+ produtos[0])
        print(produtos[0]+ ' R$ 2,00')
        pagamento()

    elif(opcao == '2'):
        #opcao 2. capuccino
        print('voce escolheu: '+ produtos[1])
        print(produtos[1]+ ' R$ 3,50')
        pagamento()

    elif(opcao == '3'):
        #opcao 2. cafe com leite
        print('voce escolheu: '+ produtos[2])
        print(produtos[2]+ ' R$ 4,00')
        pagamento()

    elif(opcao == '4'):
        #opcao 2. chocolate
        print('voce escolheu: '+ produtos[3])
        print(produtos[3]+ ' R$ 4,50')
        pagamento()

    elif(opcao == '5'):
        print("obrigado pela preferencia")
        exit()
    else:
        print('Voce digitou uma opcao invalida. Por favor, tente novamente.')
        menuprincipal()
    #Aqui é o fim da função
menuprincipal()