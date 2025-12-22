-- Criar tabela clientes
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    email TEXT,
    telefone TEXT
);

-- Criar tabela produtos
CREATE TABLE IF NOT EXISTS produtos (
    id INTEGER PRIMARY KEY,
    nome TEXT,
    categoria TEXT,
    preco REAL
);

-- Criar tabela pedidos
CREATE TABLE IF NOT EXISTS pedidos (
    id INTEGER PRIMARY KEY,
    cliente_id INTEGER,
    data TEXT,
    status TEXT,
    valor REAL,
    itens INTEGER,
    FOREIGN KEY (cliente_id) REFERENCES clientes(id)
);

-- Inserir clientes
INSERT INTO clientes VALUES (1,'Ana Souza','ana.souza@email.com','(21) 99999-1111');
INSERT INTO clientes VALUES (2,'Carlos Lima','carlos.lima@email.com','(21) 98888-2222');
INSERT INTO clientes VALUES (3,'Mariana Alves','mariana.alves@email.com','(21) 97777-3333');
INSERT INTO clientes VALUES (4,'João Pedro','joao.pedro@email.com','(21) 96666-4444');
INSERT INTO clientes VALUES (5,'Fernanda Costa','fernanda.costa@email.com','(21) 95555-5555');
INSERT INTO clientes VALUES (6,'Ricardo Silva','ricardo.silva@email.com','(21) 94444-6666');
INSERT INTO clientes VALUES (7,'Patrícia Gomes','patricia.gomes@email.com','(21) 93333-7777');
INSERT INTO clientes VALUES (8,'Lucas Ferreira','lucas.ferreira@email.com','(21) 92222-8888');
INSERT INTO clientes VALUES (9,'Beatriz Ramos','beatriz.ramos@email.com','(21) 91111-9999');
INSERT INTO clientes VALUES (10,'Thiago Martins','thiago.martins@email.com','(21) 90000-0000');

-- Inserir produtos
INSERT INTO produtos VALUES (1,'Cheeseburger','Lanche',18.90);
INSERT INTO produtos VALUES (2,'Duplo Bacon','Lanche',25.00);
INSERT INTO produtos VALUES (3,'Vegetariano','Lanche',22.50);
INSERT INTO produtos VALUES (4,'Batata Frita','Acompanhamento',12.00);
INSERT INTO produtos VALUES (5,'Onion Rings','Acompanhamento',14.00);
INSERT INTO produtos VALUES (6,'Refrigerante Lata','Bebida',6.00);
INSERT INTO produtos VALUES (7,'Suco Natural','Bebida',8.50);
INSERT INTO produtos VALUES (8,'Milkshake Chocolate','Sobremesa',15.00);
INSERT INTO produtos VALUES (9,'Milkshake Morango','Sobremesa',15.00);
INSERT INTO produtos VALUES (10,'Brownie','Sobremesa',10.00);

-- Inserir pedidos
INSERT INTO pedidos VALUES (1,1,'2025-01-10','pago',45.90,2);
INSERT INTO pedidos VALUES (2,2,'2025-01-11','pago',32.50,1);
INSERT INTO pedidos VALUES (3,3,'2025-01-12','cancelado',0.00,0);
INSERT INTO pedidos VALUES (4,1,'2025-01-15','pago',60.00,3);
INSERT INTO pedidos VALUES (5,4,'2025-01-16','aberto',28.00,1);
INSERT INTO pedidos VALUES (6,5,'2025-01-20','pago',75.00,4);
INSERT INTO pedidos VALUES (7,6,'2025-01-22','pago',52.00,2);
INSERT INTO pedidos VALUES (8,7,'2025-01-25','pago',40.00,2);
INSERT INTO pedidos VALUES (9,8,'2025-01-28','cancelado',0.00,0);
INSERT INTO pedidos VALUES (10,9,'2025-01-30','pago',90.00,5);
