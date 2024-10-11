from SQL import CRUD  # Importando as operações CRUD do módulo SQL
from asyncio import run  # Importando a função run para lidar com chamadas assíncronas
from os import system as clear  # Importando o comando system para limpar o console
from localizer import localize

# Instanciando a classe CRUD
crud = CRUD()

# Loop principal para perguntar continuamente ao usuário
while True:
    try:
        # Pergunta ao usuário qual ação deseja realizar
        action = int(input('1-Inserir dado \n2-Ler tabela \n3-Atualizar \n4-Deletar\n'))
    except ValueError:
        # Se a entrada não for um inteiro, continua o loop
        continue

    clear('cls')  # Limpa o console

    try:
        # Pergunta ao usuário para selecionar uma tabela
        table = int(input('Insira a Tabela:\n1-cadastros\n2-compras\n3-expedição\n4-financeiro\n5-itens compra\n6-itens venda\n7-produtos\n8-relatorio anual\n9-vendas\n'))
    except ValueError:
        # Se a entrada não for um inteiro, continua o loop
        continue

    # Mapeia a seleção da tabela do usuário para os nomes reais das tabelas
    match table:
        case 1:
            table = 'cadastros'
        case 2:
            table = 'compras'
        case 3:
            table = 'expedicao'
        case 4:
            table = 'financeiro'
        case 5:
            table = 'itens_compra'
        case 6:
            table = 'itens_venda'
        case 7:
            table = 'produtos'
        case 8:
            table = 'relatorio_anual'
        case 9:
            table = 'vendas'

    clear('cls')  # Limpa o console novamente para a próxima entrada

    # Executa a ação com base na seleção do usuário
    match action:
        case 1:  # Inserir dados
            values = str(input('Insira os dados separados por vírgula\n')).split(',')
            # Verifica o número de valores e chama o método create de acordo
            if len(values) == 5:
                run(crud.create(table, values[0], values[1], values[2], values[3], values[4]))
            elif len(values) == 6:
                run(crud.create(table, values[0], values[1], values[2], values[3], values[4], values[5]))
            elif len(values) == 7:
                run(crud.create(table, values[0], values[1], values[2], values[3], values[4], values[5], values[6]))
            else:
                print('Valores inseridos incorretamente')  # Mensagem de erro para entrada incorreta

        case 2:  # Ler dados da tabela
            parameter = str(input('Insira a coluna a ser filtrada:\n'))
            # Se nenhum parâmetro for dado, padrão é '*'
            if parameter == '':
                parameter = '*'
            try:
                # Executa a operação de leitura e imprime os resultados
                print(run(crud.read(table, parameter)))
            except Exception:
                print('Erro ao ler a tabela')  # Mensagem de erro para falha na leitura
            # Aguarda a entrada do usuário antes de limpar o console novamente
            con = input()

        case 3:  # Atualizar dados
            set = str(input('Insira a coluna junto ao novo dado\nex: "ID = 1"\n'))
            condition = str(input('Insira uma coluna da linha a ser procurada\nex: "ID = 10"\n'))
            run(crud.update(table, set, condition))  # Chama o método de atualização

        case 4:  # Deletar dados
            condition = str(input('Insira o local a ser apagado\nex: "ID = 1"\n'))
            run(crud.delete(table, condition))  # Chama o método de deleção

    clear('cls')  # Limpa o console para a próxima iteração






