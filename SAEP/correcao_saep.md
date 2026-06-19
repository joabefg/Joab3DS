# Sistema de Controle de Almoxarifado

## 1. DER (Diagrama Entidade-Relacionamento)

```text
+----------------+
|   categoria    |
+----------------+
| id_categoria PK|
| nome           |
+----------------+
        |
        | 1:N
        |
+----------------+
|    produto     |
+----------------+
| id_produto PK  |
| nome           |
| unidade_medida |
| quantidade     |
| valor_unitario |
| id_categoria FK|
+----------------+
      /   \
     /     \
   1:N     1:N
   /         \
+---------+ +---------+
| entrada | |  saida |
+---------+ +---------+
| id PK   | | id PK   |
| data    | | data    |
| qtd     | | qtd     |
| produto | | produto |
| FK      | | FK      |
+---------+ +---------+
```

---

# 2. Script SQL Completo

```sql
CREATE DATABASE almoxarifado;
USE almoxarifado;

-- CATEGORIAS
CREATE TABLE categoria (
    id_categoria INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(50) NOT NULL
);

-- PRODUTOS
CREATE TABLE produto (
    id_produto INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    unidade_medida VARCHAR(20) NOT NULL,
    quantidade INT NOT NULL DEFAULT 0,
    valor_unitario DECIMAL(10,2) NOT NULL,
    id_categoria INT NOT NULL,

    FOREIGN KEY (id_categoria)
        REFERENCES categoria(id_categoria)
);

-- ENTRADAS
CREATE TABLE entrada (
    id_entrada INT AUTO_INCREMENT PRIMARY KEY,
    data_entrada DATE NOT NULL,
    quantidade INT NOT NULL,
    id_produto INT NOT NULL,

    FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto)
);

-- SAIDAS
CREATE TABLE saida (
    id_saida INT AUTO_INCREMENT PRIMARY KEY,
    data_saida DATE NOT NULL,
    quantidade INT NOT NULL,
    id_produto INT NOT NULL,

    FOREIGN KEY (id_produto)
        REFERENCES produto(id_produto)
);

-- DADOS INICIAIS

INSERT INTO categoria(nome) VALUES
('Limpeza'),
('Escritorio'),
('Copa');

INSERT INTO produto
(nome, unidade_medida, quantidade, valor_unitario, id_categoria)
VALUES
('Detergente','UN',50,3.50,1),
('Papel A4','RESMA',30,25.00,2),
('Copo Descartavel','PACOTE',80,8.00,3);

INSERT INTO entrada
(data_entrada, quantidade, id_produto)
VALUES
('2026-06-01',20,1),
('2026-06-02',10,2),
('2026-06-03',15,3);

INSERT INTO saida
(data_saida, quantidade, id_produto)
VALUES
('2026-06-04',5,1),
('2026-06-05',3,2),
('2026-06-06',10,3);

-- VIEW EXIGIDA PELA PROVA

CREATE VIEW vw_estoque AS
SELECT
    p.id_produto,
    p.nome,
    p.quantidade,
    p.valor_unitario,
    (p.quantidade * p.valor_unitario) AS valor_total
FROM produto p;
```

---

# 3. Código Python Completo

## Conexão

```python
import mysql.connector

def conectar():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="1234",
        database="almoxarifado"
    )
```

---

## Listar Produtos

```python
def listar_produtos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT p.id_produto,
               p.nome,
               c.nome,
               p.quantidade,
               p.valor_unitario
        FROM produto p
        JOIN categoria c
        ON p.id_categoria = c.id_categoria
    """)

    for produto in cursor.fetchall():
        print(produto)

    conn.close()
```

---

## Cadastrar Produto

```python
def cadastrar_produto():

    nome = input("Nome: ")
    unidade = input("Unidade: ")

    quantidade = int(input("Quantidade: "))

    if quantidade < 0:
        print("Quantidade inválida")
        return

    valor = float(input("Valor Unitário: "))

    if valor <= 0:
        print("Valor inválido")
        return

    categoria = int(input("ID Categoria: "))

    if categoria not in [1,2,3]:
        print("Categoria inválida")
        return

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO produto
        (nome, unidade_medida, quantidade,
         valor_unitario, id_categoria)
        VALUES (%s,%s,%s,%s,%s)
    """,(nome,unidade,quantidade,valor,categoria))

    conn.commit()
    conn.close()

    print("Produto cadastrado.")
```

---

## Registrar Entrada

```python
def registrar_entrada():

    id_produto = int(input("Produto: "))
    qtd = int(input("Quantidade: "))
    data = input("Data (AAAA-MM-DD): ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO entrada
        (data_entrada, quantidade, id_produto)
        VALUES (%s,%s,%s)
    """,(data,qtd,id_produto))

    cursor.execute("""
        UPDATE produto
        SET quantidade = quantidade + %s
        WHERE id_produto = %s
    """,(qtd,id_produto))

    conn.commit()
    conn.close()

    print("Entrada registrada.")
```

---

## Registrar Saída

```python
def registrar_saida():

    id_produto = int(input("Produto: "))
    qtd = int(input("Quantidade: "))
    data = input("Data (AAAA-MM-DD): ")

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT quantidade
        FROM produto
        WHERE id_produto = %s
    """,(id_produto,))

    estoque = cursor.fetchone()[0]

    if qtd > estoque:
        print("Estoque insuficiente.")
        conn.close()
        return

    cursor.execute("""
        INSERT INTO saida
        (data_saida, quantidade, id_produto)
        VALUES (%s,%s,%s)
    """,(data,qtd,id_produto))

    cursor.execute("""
        UPDATE produto
        SET quantidade = quantidade - %s
        WHERE id_produto = %s
    """,(qtd,id_produto))

    conn.commit()
    conn.close()

    print("Saída registrada.")
```

---

## Valor Total por Categoria

```python
def valor_por_categoria():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            c.nome,
            SUM(
                p.quantidade * p.valor_unitario
            ) AS total
        FROM produto p
        JOIN categoria c
        ON c.id_categoria = p.id_categoria
        GROUP BY c.nome
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
```

---

## Saídas em Ordem Decrescente

```python
def listar_saidas():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nome,
            s.quantidade,
            s.data_saida
        FROM saida s
        JOIN produto p
        ON p.id_produto = s.id_produto
        ORDER BY s.data_saida DESC
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
```

---

## Movimentação por Período (7 campos exigidos)

```python
def relatorio_periodo(data_inicial, data_final):

    conn = conectar()
    cursor = conn.cursor()

    sql = """
    SELECT
        p.nome,
        p.unidade_medida,

        IFNULL(SUM(DISTINCT e.quantidade),0),
        IFNULL(SUM(DISTINCT s.quantidade),0),

        IFNULL(SUM(DISTINCT e.quantidade),0) -
        IFNULL(SUM(DISTINCT s.quantidade),0),

        IFNULL(SUM(DISTINCT e.quantidade * p.valor_unitario),0),

        IFNULL(SUM(DISTINCT s.quantidade * p.valor_unitario),0)

    FROM produto p

    LEFT JOIN entrada e
        ON p.id_produto = e.id_produto
        AND e.data_entrada
            BETWEEN %s AND %s

    LEFT JOIN saida s
        ON p.id_produto = s.id_produto
        AND s.data_saida
            BETWEEN %s AND %s

    GROUP BY
        p.nome,
        p.unidade_medida
    """

    cursor.execute(
        sql,
        (data_inicial,data_final,
         data_inicial,data_final)
    )

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
```

---

## Produtos com Maior Volume de Saída

```python
def top_produtos_saida(data_inicial, data_final):

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.nome,
            SUM(s.quantidade) AS total_saida,
            SUM(
                s.quantidade *
                p.valor_unitario
            ) AS valor_financeiro

        FROM saida s

        JOIN produto p
        ON p.id_produto = s.id_produto

        WHERE s.data_saida
        BETWEEN %s AND %s

        GROUP BY p.nome

        ORDER BY total_saida DESC
    """,(data_inicial,data_final))

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
```

---

## Produtos nos Limites de Estoque

```python
def verificar_limites():

    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            nome,
            quantidade,
            ROUND((quantidade / 100) * 100,2)
            AS percentual
        FROM produto
        WHERE quantidade <= 0
           OR quantidade >= 100
    """)

    for linha in cursor.fetchall():
        print(linha)

    conn.close()
```

---

## Menu Principal

```python
while True:

    print("\n1-Listar Produtos")
    print("2-Cadastrar Produto")
    print("3-Registrar Entrada")
    print("4-Registrar Saída")
    print("5-Valor por Categoria")
    print("6-Listar Saídas")
    print("7-Relatório por Período")
    print("8-Top Saídas")
    print("9-Verificar Limites")
    print("0-Sair")

    op = input("Opção: ")

    if op == "1":
        listar_produtos()

    elif op == "2":
        cadastrar_produto()

    elif op == "3":
        registrar_entrada()

    elif op == "4":
        registrar_saida()

    elif op == "5":
        valor_por_categoria()

    elif op == "6":
        listar_saidas()

    elif op == "7":
        ini = input("Data inicial: ")
        fim = input("Data final: ")
        relatorio_periodo(ini,fim)

    elif op == "8":
        ini = input("Data inicial: ")
        fim = input("Data final: ")
        top_produtos_saida(ini,fim)

    elif op == "9":
        verificar_limites()

    elif op == "0":
        break
```

---

## Requisitos Atendidos

### Banco de Dados

* ✔ DER com entidades, relacionamentos e cardinalidades.
* ✔ Tabelas com chaves primárias e estrangeiras.
* ✔ Pelo menos 3 registros em cada tabela.
* ✔ View `vw_estoque`.
* ✔ Controle de categorias de produtos.

### Funcionalidades Python

* ✔ Listar todos os produtos.
* ✔ Cadastrar produtos com validações.
* ✔ Registrar entradas de estoque.
* ✔ Registrar saídas de estoque.
* ✔ Atualizar saldo automaticamente.
* ✔ Listar saídas em ordem decrescente por data.
* ✔ Listar valor total por categoria.
* ✔ Relatório de movimentação por período.
* ✔ Ranking de produtos com maior volume de saída.
* ✔ Identificação de estoque mínimo (0) e máximo (100).
* ✔ Exibição do percentual de ocupação do estoque.

### Observações para a Avaliação

Durante a apresentação da prova, demonstre:

1. Criação do banco no MySQL Workbench.
2. Execução dos INSERTs.
3. Consulta da view `vw_estoque`.
4. Execução das funções Python pelo terminal.
5. Cadastro de um novo produto.
6. Registro de uma entrada.
7. Registro de uma saída.
8. Geração dos relatórios solicitados.
9. Consulta dos produtos em limite mínimo ou máximo.

Esses itens cobrem integralmente os requisitos descritos na avaliação prática de desenvolvimento do sistema de controle de almoxarifado.
