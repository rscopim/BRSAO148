def main():
    print("🛒 Lita de compras")
    print("Digite os itens desejados. Para encerrar, digite 'fim'.\n")

    lista_compras = []

    while True:
        item = input("Adicione um item: ").strip()
        if item.lower() == "fim":
            break
        if item == "":
            print("⚠ Item vazio ignorado.")
            continue
        lista_compras.append(item)
        print(f"✅ '{item}' adicionado à lista.")

    print("\n📋 Parabéns, voce criou uma lista de compras das mais caras kkkkk:")
    if lista_compras:
        for i, produto in enumerate(lista_compras, 1):
            print(f"{i}. {produto}")
    else:
        print("Nenhum item foi adicionado.")

# Execução principal
if __name__ == "__main__":
    main()