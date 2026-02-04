print('===CONVERSOR DE BITCOIN (Simples)===')
print('1 - Real(BRL) para bitcoin(BTC)')
print('2 - Bitcoin(BTC) para Real(BRL)')

opcao = input('Escolha a opção (1 ou 2): ')
preco_btc = 380000.00 # valor fixo para o exemplo
 
if opcao == '1':
    valor_brl = float(input('Digite o valor em Real (BRL): '))
    valor_btc = valor_brl / preco_btc
    print(f'R$ {valor_brl:.2f} equivalem a {valor_btc:.8f}BTC')
    
elif opcao == '2':
    valor_btc = float(input('Quantos bitcoins (BTC) você tem? '))
    valor_brl = valor_btc * preco_btc
    print(f'{valor_btc:.8f} BTC equivalem a R$ {valor_brl:.2f}')

else:
    print('opção inválida. por favor, escolha 1 ou 2.')

        