lista = []
def adicionar_cliente(cadastro, email):  
     for valor in lista:
          if valor['nome'] == cadastro or valor['email'] == email: 
            print("Cadastro já existente.")
            return
     novo_cadastro = {"nome": cadastro, "email": email, "compras": 0}
     adicionar = lista.append(novo_cadastro)
     print("Cadastro adicionado com sucesso.")
     return adicionar

def remover_cliente(lista, cadastro):
    for nome in lista:
        if nome['nome'] == cadastro:
            lista.remove(nome)
            print("Cadastro removido com sucesso.")
            return
    print("Este cadastro não existe.")

def buscar_cliente(lista, cliente):
    for nome in lista:
        if nome['nome'] == cliente:
         print(f"nome: {nome['nome']}, email: {nome['email']}")
         return
    print("Este nome não existe.")    
            
def listar_clientes(lista):
    if not lista:
        print("Nenhum cadastro encontrado.")
        return
    for i, cadastro in enumerate(lista):
        print(f"Cliente: {i+1} = {cadastro}")
    
def registrar_compra(cadastro):
    for registro in lista:
        if registro['nome'] == cadastro: 
            registro['compras'] +=1
            print(f"Compra Registrada para: {registro['nome']}")
            return 
    print("Este cadastro não existe.")

def historico_compras(cadastro):
    for historico in lista:
        if historico['nome'] == cadastro:
            print(f'Cadastro: {cadastro}, Compras: {historico["compras"]}')
            return
    print("Este cadastro não existe.")

def cliente_com_mais_compras(lista):
    if not lista:
        print("Nenhum cadastro encontrado.")
        return
    cliente_top = lista[0]
    for cadastro in lista:
        if cadastro['compras'] > cliente_top['compras']:
            cliente_top = cadastro 
    print(f"Cliente com mais compras: {cliente_top}")


def total_de_clientes(lista):
    if not lista:
        print("A lista está vazia.")
    total = len(lista)
    print(f"Total de Clientes: {total}")
    return total    
                
while True:
    print("Menu:")
    print("1: Adicionar Cliente")
    print("2: Remover Cliente")
    print("3: Buscar Cliente")
    print("4: Listar Cliente")
    print("5: Registrar Compra")
    print("6: Ver Historico De Compras")
    print("7: Cliente Com Mais Compras")
    print("8: Total De Clientes")
    print("9: Sair")
    opçao = input("Qual opção deseja utilizar: ")
    match opçao:
        case "1":
            nome = input("Digite o nome: ")
            email = input("Qual email: ")
            adicionar_cliente(nome,email)

        case "2":
            remover = input("Deseja remover qual cliente: ")
            remover_cliente(lista,remover)    

        case "3":
            buscar = input("Buscar Cliente: ")
            buscar_cliente(lista,buscar)

        case "4":
            listar_clientes(lista)

        case "5":
            registrar = input("Informe o nome: ")
            registrar_compra(registrar)

        case "6":
            historico = input("Informe o nome: ")
            historico_compras(historico)     

        case "7":
            cliente_com_mais_compras(lista)

        case "8":
            total_de_clientes(lista)   

        case "9":
            print("Programa Finalizado.")
            break     


                          


