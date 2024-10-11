from databases import Database as db
import asyncio
# Inicializa a conexão com o banco de dados usando SQLite com suporte a async
database = db('sqlite+aiosql:///cafevovo.db')

class CRUD():
    async def _init_(self):
        # Conecta ao banco de dados de forma assíncrona
        await database.connect()

    async def create(self, table, col1, col2, col3, col4, col5, col6='', col7=''):
        '''
        Insere um novo registro na tabela especificada.
        
        A tabela pode ser uma das seguintes:
        - cadastros       (cadastro_id, nome, endereco, telefone, cpf_cnpj, email, data_cadastro)
        - financeiro      (financeiro_id, tipo_movimento, data_movimento, valor, venda_id, compra_id, descricao)
        - relatorio_anual (ano, receita_total, lucro_bruto, despesa_operacional, custo_por_pedido, crescimento_receita, meta_crescimento)
        - expedicao       (expedicao_id, venda_id, data_envio, status_entrega, transportadora, custo_entrega)
        - itens_compra    (item_compra_id, compra_id, produto_id, quantidade, preco_unitario, sub_total)
        - itens_venda     (item_venda_id, venda_id, produto_id, quantidade, preco_unitario, sub_total)
        - compras         (compra_id, fornecedor_id, data_compra, valor_total, status_pagamento)
        - vendas          (venda_id, cliente_id, data_venda, valor_total, status_pagamento)
        - produtos        (produto_id, nome_produto, categoria, preco, validade)
        '''
         # Cria a consulta SQL e os valores com base na tabela especificada
        match table:
            case 'cadastros':
                query = 'INSERT INTO cadastros(cadastro_id, nome, endereco, telefone, cpf_cnpj, email, data_cadastro) VALUES (:col1, :col2, :col3, :col4, :col5, :col6, :col7)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6, 'col7':col7}
                         ]
            case 'financeiro':
                query = 'INSERT INTO financeiro(financeiro_id, tipo_movimento, data_movimento, valor, venda_id, compra_id, descricao) VALUES (:col1, :col2, :col3, :col4, :col5, :col6, :col7)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6, 'col7':col7}
                         ]
            case 'relatorio_anual':
                query = 'INSERT INTO relatorio_anual(ano, receita_total, lucro_bruto, despesa_operacional, custo_por_pedido, crescimento_receita, meta_crescimento) VALUES (:col1, :col2, :col3, :col4, :col5, :col6, :col7)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6, 'col7':col7}
                         ]
            case 'expedicao':
                query = 'INSERT INTO expedicao(expedicao_id, venda_id, data_envio, status_entrega, transportadora, custo_entrega) VALUES (:col1, :col2, :col3, :col4, :col5, :col6)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6}
                         ]
            case 'itens_compra':
                query = 'INSERT INTO itens_compra(item_compra_id, compra_id, produto_id, quantidade, preco_unitario, sub_total) VALUES (:col1, :col2, :col3, :col4, :col5, :col6)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6}
                         ]
            case 'itens_venda':
                query = 'INSERT INTO itens_venda(item_venda_id, venda_id, produto_id, quantidade, preco_unitario, sub_total) VALUES (:col1, :col2, :col3, :col4, :col5, :col6)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5, 'col6':col6}
                         ]
            case 'compras':
                query = 'INSERT INTO compras(compra_id, fornecedor_id, data_compra, valor_total, status_pagamento) VALUES (:col1, :col2, :col3, :col4, :col5)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5}
                         ]
            case 'vendas':
                query = 'INSERT INTO vendas(venda_id, cliente_id, data_venda, valor_total, status_pagamento) VALUES (:col1, :col2, :col3, :col4, :col5)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5}
                         ]
            case 'produtos':
                query = 'INSERT INTO produtos(produto_id, nome_produto, categoria, preco, validade) VALUES (:col1, :col2, :col3, :col4, :col5)'
                values = [
                {'col1':col1, 'col2':col2, 'col3':col3, 'col4':col4, 'col5':col5}
                         ]
            case _:
                print('TABELA NÃO ENCONTRADA')
                return   
            
        # Executa a consulta de inserção com os valores especificados
        await database.execute_many(query=query, values=values)

    async def read(self, table, parameter='*'):
        '''
        Busca registros na tabela especificada.
        
        Parâmetros:
        - table: Nome da tabela a ser consultada.
        - parameter: Colunas específicas a serem buscadas, padrão é todas (*).
        
        Exemplo de uso: 
        
        read('vendas', 'venda_id')
        '''
        if parameter == '':
            parameter = '*'
        query = f"SELECT {parameter} FROM {table}"
        rows = await database.fetch_all(query=query)

        # Converte as linhas em uma lista de dicionários para facilitar o acesso
        itens = []
        for row in rows:
            itens.append(dict(row))
        return itens
    
    async def update(self, table, set, condition):
        '''
        Atualiza registros na tabela especificada.
        
        Parâmetros:
        - table: Nome da tabela a ser atualizada.
        - set: Cláusula SET definindo quais campos atualizar.
        - condition: Cláusula WHERE para especificar quais registros atualizar.
        
        Exemplo de uso: 

        update('produtos', 'nome_produto = "product"', 'produto_id = 1')
        '''
        query = f"""
UPDATE {table}
SET {set}
WHERE {condition}
"""
        await database.execute(query=query)

    async def delete(self, table, condition):
        '''
        Deleta registros da tabela especificada.
        
        Parâmetros:
        - table: Nome da tabela de onde deletar.
        - condition: Cláusula WHERE para especificar quais registros deletar.
        
        Exemplo de uso: 
        
        delete('produtos', 'produto_id = 1')
        '''
        query = f"DELETE FROM {table} WHERE {condition}"
        await database.execute(query=query)

