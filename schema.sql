-- Esquema para banco de dados de árvore genealógica

-- Tabela de pessoas
CREATE TABLE IF NOT EXISTS person (
    id SERIAL PRIMARY KEY,
    name VARCHAR(255) NOT NULL
);

-- Tabela de relacionamentos
CREATE TABLE IF NOT EXISTS relationship (
    id SERIAL PRIMARY KEY,
    parent_id INTEGER REFERENCES person(id),
    child_id INTEGER REFERENCES person(id)
);

-- Índices para otimização de consultas
CREATE INDEX IF NOT EXISTS idx_relationship_parent ON relationship(parent_id);
CREATE INDEX IF NOT EXISTS idx_relationship_child ON relationship(child_id);