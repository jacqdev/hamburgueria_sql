import os
import sqlite3
import pytest

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

def test_total_vendas(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT SUM(valor) FROM pedidos WHERE status='pago';")
    total = cursor.fetchone()[0]
    assert round(total, 2) == 395.4  # soma correta dos pedidos pagos

def test_pedidos_cancelados(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status='cancelado';")
    total = cursor.fetchone()[0]
    assert total == 2  # sampledata.sql tem 2 cancelados

def test_pedidos_abertos(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM pedidos WHERE status='aberto';")
    total = cursor.fetchone()[0]
    assert total == 1  # sampledata.sql tem 1 aberto
