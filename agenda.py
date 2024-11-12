import json
 
# Inicializa a agenda em uma lista  
agenda = []

def pesquisaAgenda():
    nomePesquisa = input("Digite o nome do contato que você quer pesquisar")
    for contato in agenda:
        if nomePesquisa.lower() in contato['nome'].lower():
            print(contato)


# Função para carregar as informações ja existentes do json
def carregarAgenda():
    try:
        with open('agenda.json', 'r') as arquivo:
            return json.load(arquivo)  # Retorna a lista do json
    except:
        return []  # Se der algum problema retornar uma lista vazia
 
# Função para salvar as novas informaçoes no json    
def salvarAgenda():
    with open('agenda.json', 'w') as arquivo:
        json.dump(agenda, arquivo, indent=4)  
 
# Função para mostrar todos os contatos na agenda
def mostrarAgenda():
    
        if agenda == []:
            print("\nAgenda Vazia")
        else:    
            print("\nTodos os contatos na agenda:\n")
            for contato in agenda:
                for chave, valor in contato.items():
                    print(f"{chave}: {valor}")
                print()  
 
def excluirContato(): # Função que exclui o contato
    nomeApagar = input("Digite o nome do contato que você quer excluir: ")
    for contato in agenda:
        if contato["nome"].lower() == nomeApagar.lower():  
            confirmacao = input("Tem certeza que deseja excluir? Digite S para confirmar ")
            if confirmacao.lower() == 's':
                agenda.remove(contato)
            else:
                print("Cancelado")
    salvarAgenda()

def editarContato(): # Função para editar contatos preexistentes
    nomeEditar = input("Digite o nome do contato que você deseja editar ")
    for contato in agenda:
        if contato["nome"] == nomeEditar:
            nomeEditado = input("Escreva o nome para alterar ") 
            telefoneEditado = input("Escreva o telefone para alterar ") 
            emailEditado = input("Escreva o email para alterar ")

            if nomeEditado:
                contato["nome"] = nomeEditado
            if telefoneEditado:
                contato["telefone"] = telefoneEditado
            if emailEditado:
                contato["email"] = emailEditado
            
            salvarAgenda()
            break
 
# Função para adicionar um novo contato
def adicionarContato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o telefone do contato: ")
    email = input("Digite o email do contato: ")
    
    for contato in agenda:
        if nome.lower() == contato["nome"].lower():
            print("ERRO: contato ja existente")
            return
        
        if nome == "":
            print("ERRO: É necessário colocar um nome")
            return
   
    contato = {
        "nome": nome,
        "telefone": telefone,
        "email": email
    }

    agenda.append(contato)  # Adiciona o contato a agenda
    salvarAgenda()

        

agenda = carregarAgenda()

# Menu
while True:
    continuar = int(input(
        "\nEscolha uma opção:\n"
        "1 - Para adicionar contato\n"
        "2 - Para excluir algum contato\n"
        "3 - Para editar algum contato\n"
        "4 - Para mostrar a agenda\n"
        "5 - Para pesquisar algum contato\n"
        "6 - Para parar a execução\n"
        "Digite sua opção: "
    ))
 
    match continuar:
        case 1:
            adicionarContato()
        case 2:
            excluirContato()
        case 3:
            editarContato()
        case 4:
            mostrarAgenda()
        case 5:
            pesquisaAgenda()
        case 6:
            break
        case _:
            print("Opção inválida! Tente novamente.")