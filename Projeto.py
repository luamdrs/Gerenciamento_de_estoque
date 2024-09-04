from time import sleep
# Função para exibir o menu de opções
def exibir_menu():
    print('=== Sistema de Gerenciamento de Estoque ===')
    print('[1] Adicionar item')
    print('[2] Remover item')
    print('[3] Exibir estoque')
    print('[4] Calcular valor total do estoque')
    print('[5] Sair do programa')
    print('=' * 43)


# Função para adicionar um item ao estoque
def adicionar_item(estoque):
    nome = input('Nome do item: ')
    quantidade = int(input('Quantidade: '))
    preco = float(input('Preço unitário: R$'))

    # Se o item já existir no estoque, a quantidade é atualizada somando-se à existente.
    if nome in estoque:
        estoque[nome]['quantidade'] += quantidade
    # Se o item não existir, ele é adicionado ao estoque com a quantidade e o preço informados.
    else:
        estoque[nome] = {'quantidade': quantidade, 'preco': preco}
    # Uma mensagem é exibida confirmando a adição ou atualização do item.
    print(f'Item {nome} adicionado ao estoque com sucesso!')


# Função para remover um item do estoque
def remover_item(estoque):
    nome = input('Nome do item a ser removido: ')
    # Se o item existir no estoque, o usuário pode remover uma quantidade específica.
    if nome in estoque:
        quantidade = int(input('Quantidade a remover: '))
        # Se a quantidade removida for igual ou maior que a quantidade no estoque, o item é removido completamente.
        if quantidade >= estoque[nome]['quantidade']:
            del estoque[nome]
            print(f'Item {nome} removido completamente do estoque.')
        # Se a quantidade removida for menor que a quantidade disponível, a quantidade é atualizada.
        else:
            estoque[nome]['quantidade'] -= quantidade
            # Uma mensagem é exibida confirmando a remoção ou atualização do item.
            print(f'Quantidade de {nome} atualizada para {estoque[nome]['quantidade']}.')
    # Se o item não existir, uma mensagem é exibida informando que o item não está no estoque.
    else:
        print(f'O item {nome} não está no estoque.')


# Função para exibir o estoque atual
def exibir_estoque(estoque):
    # Se o estoque estiver vazio, exibe uma mensagem informando isso.
    if not estoque:
        print('O estoque está vazio.')
    # Se houver itens no estoque, a função percorre o dicionário estoque e imprime o nome de cada item, a quantidade disponível e o preço unitário.
    else:
        print('=== Estoque Atual ===')
        for nome, dados in estoque.items():
            print(f'{nome}: {dados['quantidade']} unidades - R$ {dados['preco']:.2f} cada')
        print('=' * 20)


# Função para calcular o valor total do estoque
def calcular_valor_total(estoque):
    # A função utiliza uma expressão de soma (sum) que percorre cada item do estoque, multiplicando a quantidade pelo preço para cada item e somando esses valores.
    valor_total = sum(dados['quantidade'] * dados['preco'] for dados in estoque.values())
    print(f'Valor total do estoque: R$ {valor_total:.2f}')


# Função principal que controla o fluxo do programa
def sistema_gerenciamento_estoque():
    # Cria o dicionário estoque, que inicialmente é vazio.
    estoque = {}
    # Entra em um loop infinito que continuará rodando até que o usuário escolha sair do programa.
    while True:
        exibir_menu()
        opcao = int(input('Escolha uma opção: '))

        if opcao == 1:
            adicionar_item(estoque)
        elif opcao == 2:
            remover_item(estoque)
        elif opcao == 3:
            exibir_estoque(estoque)
        elif opcao == 4:
            calcular_valor_total(estoque)
        elif opcao == 5:
            print('Saindo do sistema...')
            sleep(2)
            print('\033[1;35mPrograma finalizado!\033[m')
            break
        else:
            print('\033[1;31mOpção inválida! Tente novamente!\033[m')


# Iniciar o sistema de gerenciamento de estoque
# Fora de todas as funções, o programa chama a função sistema_gerenciamento_estoque() para começar a execução.
sistema_gerenciamento_estoque()