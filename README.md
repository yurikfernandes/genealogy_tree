# Genealogy Tree API

## Descrição

Genealogy Tree é uma API para gerenciar e visualizar árvores genealógicas. A aplicação permite cadastrar pessoas, registrar relacionamentos de parentesco e consultar árvores genealógicas completas.

## Tecnologias Utilizadas

- **Backend**: Python 3
- **Banco de Dados**: PostgreSQL
- **Infraestrutura**: Docker e Docker Compose

## Estrutura do Projeto

O projeto segue uma arquitetura em camadas:

```
genealogy_tree/
├── genealogy/              # Código-fonte principal
│   ├── __init__.py
│   ├── db_connector.py     # Conexão com o banco de dados
│   ├── handler.py          # Manipulador de requisições HTTP
│   ├── models.py           # Modelos de dados e operações CRUD
│   ├── server.py           # Servidor HTTP
│   └── service.py          # Lógica de negócio
│
├── tests/                  # Testes automatizados
├── docker-compose.yml      # Configuração de contêineres
├── Dockerfile              # Configuração da imagem Docker
├── init_db.py              # Script para inicializar o banco de dados
├── main.py                 # Ponto de entrada da aplicação
├── requirements.txt        # Dependências do projeto
└── schema.sql              # Esquema do banco de dados
```

## Instalação e Execução

### Pré-requisitos

- Python 3.9+
- PostgreSQL 15+
- Docker e Docker Compose (opcional)

### Execução Local

1. Clone o repositório
2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```
3. Configure as variáveis de ambiente ou use os valores padrão:
   ```
   DB_NAME=genealogy_tree
   DB_USER=postgres
   DB_PASSWORD=123456
   DB_HOST=localhost
   DB_PORT=5432
   ```
4. Inicialize o banco de dados:
   ```bash
   python init_db.py
   ```
5. Inicie a aplicação:
   ```bash
   python main.py
   ```
6. Acesse a API em: http://localhost:8080

### Execução com Docker

1. Clone o repositório
2. Inicie os contêineres:
   ```bash
   docker compose up
   ```
3. Acesse a API em: http://localhost:8080

## API Endpoints

A API disponibiliza os seguintes endpoints:

- `GET /persons`: Lista todas as pessoas cadastradas
- `GET /persons/{id}`: Obtém detalhes de uma pessoa específica
- `POST /persons`: Cadastra uma nova pessoa
- `PUT /persons/{id}`: Atualiza dados de uma pessoa
- `DELETE /persons/{id}`: Remove uma pessoa

- `GET /relationships`: Lista todos os relacionamentos
- `GET /relationships/{id}`: Obtém detalhes de um relacionamento específico
- `POST /relationships`: Cadastra um novo relacionamento
- `PUT /relationships/{id}`: Atualiza um relacionamento
- `DELETE /relationships/{id}`: Remove um relacionamento

- `GET /tree?id={person_id}&depth={depth}`: Obtém a árvore genealógica de uma pessoa

## Testes

Para executar os testes automatizados:

```bash
pytest
```
