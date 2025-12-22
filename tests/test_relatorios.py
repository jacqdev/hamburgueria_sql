import os
import sqlite3
import pytest

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Carrega o sampledata.sql da raiz do projeto
    sql_path = os.path.join(os.path.dirname(__file__), "..", "sampledata.sql")
    with open(sql_path, "r", encoding="utf-8") as f:
        cursor.executescript(f.read())

    conn.commit()
    return conn

def test_vendas_por_cliente(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT cliente_id, SUM(valor)
        FROM pedidos
        WHERE status='pago'
        GROUP BY cliente_id;
    """)
    resultados = cursor.fetchall()
    # Verifica se pelo menos um cliente tem vendas registradas
    assert len(resultados) > 0
    # Exemplo: cliente 1 deve ter gasto positivo
    cliente1 = [r for r in resultados if r[0] == 1][0]
    assert cliente1[1] > 0

def test_produtos_mais_vendidos(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT produto_id, COUNT(*)
        FROM pedidos
        WHERE status='pago'
        GROUP BY produto_id
        ORDER BY COUNT(*) DESC;
    """)
    resultados = cursor.fetchall()
    # Deve haver pelo menos um produto vendido
    assert len(resultados) > 0
    # O produto mais vendido deve ter pelo menos 1 venda
    assert resultados[0][1] >= 1

def test_ticket_medio(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT AVG(valor)
        FROM pedidos
        WHERE status='pago';
    """)
    ticket_medio = cursor.fetchone()[0]
    # Ticket médio deve ser maior que zero
    assert ticket_medio > 0
