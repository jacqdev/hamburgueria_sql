import sqlite3, csv, pytest, os

@pytest.fixture
def db_conn():
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()

    # Cria tabela pedidos
    cursor.execute("""
    CREATE TABLE pedidos (
        id INTEGER PRIMARY KEY,
        cliente_id INTEGER,
        data TEXT,
        status TEXT,
        valor REAL,
        itens INTEGER
    );
    """)

    # Caminho base (raiz do projeto)
    base_dir = os.path.dirname(os.path.dirname(__file__))

    # Carrega pedidos.csv
    with open(os.path.join(base_dir, "pedidos.csv"), newline="", encoding="utf-8") as f:
        reader = csv.reader(f); next(reader)
        for row in reader:
            cursor.execute("INSERT INTO pedidos VALUES (?, ?, ?, ?, ?, ?)", row)

    conn.commit()
    return conn

def test_total_itens_vendidos(db_conn):
    cursor = db_conn.cursor()
    cursor.execute("""
        SELECT SUM(itens) AS total_itens
        FROM pedidos
        WHERE status='pago';
    """)
    resultado = cursor.fetchone()
    assert resultado is not None
    print(f"Total de itens vendidos: {resultado[0]}")
    assert resultado[0] > 0
