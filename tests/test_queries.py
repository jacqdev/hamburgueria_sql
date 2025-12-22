import os
import sqlite3
import pytest

@pytest.fixture(scope="module")
def conn():
    connection = sqlite3.connect(":memory:")
    cursor = connection.cursor()

    # Caminho correto para o sampledata.sql (na raiz do projeto)
    sql_path = os.path.join(os.path.dirname(__file__), "..", "sampledata.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        sql_script = f.read()
    cursor.executescript(sql_script)
    connection.commit()

    yield connection
    connection.close()

def test_clientes_existem(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM clientes;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 clientes

def test_produtos_existem(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM produtos;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 produtos

def test_pedidos_existem(conn):
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos;")
    total = cursor.fetchone()[0]
    assert total == 10  # sampledata.sql tem 10 pedidos
