import os
import sqlite3
import pytest

# Fixture que cria um banco em memória e carrega o sampledata.sql
@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Caminho correto para o sampledata.sql (na raiz do projeto)
    sql_path = os.path.join(os.path.dirname(__file__), "..", "sampledata.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    conn.commit()
    return conn

def test_clientes_existem(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM clientes;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 clientes

def test_produtos_existem(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 produtos

def test_pedidos_existem(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 pedidos
