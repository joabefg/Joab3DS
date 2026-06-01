Ensinar sobre Banco de dados
- Banco de dados
- SGBD
- Armazenamento e Backup
- Relacionais e NoSQL
- CRUD
Ensinar criar database parque_diversoes.
Atividade: Criar database parque_aquatico.

Ensinar sobre tabela e registros
Ensinar criar tabela atracoes (id, nome, status)
Atividade: Criar tabela bilheteria(id, visitante, valor)

Ensinar sobre driver
Instalar driver
Ensinar criar conexão (incluindo try/catch/except)
Atividade: Criar outro usuário do banco e alterar a conexão para o novo usuário/banco.

Ensinar sobre cursor e commit/rollback e porque tem que fechar conexão  
Ensinar cadastrar em atracoes
Desafio: cadastrar usando input e não hard coded
Atividade: cadastrar em bilheteria

Ensinar FetchAll
Ensinar buscar/listar atrações com status manutenção
Atividade: Mostrar total arrecadado

Desafio: criar menu de acesso.






















ATRACOES (
    id INT PK NN AI
    nome VARCHAR(100) NN
    status VARCHAR(45) 'Funcionando'
)
bilheteria (
    id INT PK NN AI
    visitante VARCHAR(100) NN
    valor DECIMAL(10, 2) NN
)

