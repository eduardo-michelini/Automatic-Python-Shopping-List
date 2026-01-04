print("Lista de compras automática")
nome_lista = input("Digite seu nome: ")
lista_compras = []

while True:
    print(" Menu lista compras: ")
    print("1 - Adicionar item")
    print("2 - Remover item")
    print("3 - Ver lista")
    print("4 - Consultar item específico")
    print("5 - Sair")

    menu_opçoes = int(input("Digite o número que você deseja: "))

    if menu_opçoes == 1:
        item_adicionar = input(f"Qual item você deseja adicionar senhor(a) {nome_lista}: ").lower()
        lista_compras.append(item_adicionar)
        print(f"Senhor(a) {nome_lista} o item {item_adicionar} foi adicionado com sucesso!")
        
    elif menu_opçoes == 2:
        item_remover = input(f"Digite o item que você deseja remover senhor(a) {nome_lista}: ").lower()
        if item_remover in lista_compras:
            lista_compras.remove(item_remover)
            print(f"Senhor(a) {nome_lista} o seu item foi removido com sucesso!")
        else:
            print(f"Senhor(a) {nome_lista} o item solicitado não existe na lista!")
        
    elif menu_opçoes == 3:
        for item in lista_compras:
            print(f" - {item}")
        if not lista_compras:
            print("Não há nenhum item na lista!")
    
    elif menu_opçoes == 4:
        item_especifico = input(f"Digite o item específico que você senhor(a) {nome_lista} gostaria de consultar: ").lower()
        if item_especifico in lista_compras:
            print(f"O item {item_especifico} está na lista! ")
        else:
            print(f"O item {item_especifico} não está na lista !")
    
    if menu_opçoes == 5:
        print("Lista final:")
        for item in lista_compras:
            print(f" - {item}")
        if not lista_compras:
            print("Sua lista terminou vazia!")
        else:
            print("Sua lista de compras foi concluída com êxito!")    
        break
        
