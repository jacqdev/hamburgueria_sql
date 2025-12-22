import csv, os

# Caminho da pasta onde estão os arquivos
base_dir = r"C:\Users\thiag\OneDrive\Documentos\hamburgueria_sql"

# Carregar produtos em um dicionário {id: nome}
produtos = {}
with open(os.path.join(base_dir, "produto.csv"), newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        produtos[row["id"]] = row["nome"]

# Contar vendas de cada produto a partir do pedido_itens.csv
vendas = {}
with open(os.path.join(base_dir, "pedido_itens.csv"), newline="", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    for row in reader:
        pid = row["produto_id"]
        qtd = int(row["quantidade"])
        vendas[pid] = vendas.get(pid, 0) + qtd

# Ordenar ranking dos produtos mais vendidos
ranking = sorted(vendas.items(), key=lambda x: x[1], reverse=True)

print("Ranking de produtos mais vendidos:")
for pid, qtd in ranking:
    print(f"{produtos[pid]} - {qtd} unidades vendidas")

    