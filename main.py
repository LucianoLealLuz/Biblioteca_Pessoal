import os
from datetime import datetime

biblioteca = []

def cadastrar_livro():
  nome_livro = input ("Digite o nome do livro: ").strip().title()
  autor_livro = input ("Digite o nome do autor: ").strip().title()
  ano_livro = input ("Digite o ano de publicação: ").strip()
  editora_livro = input ("Digite o nome da editora: ").strip().title()
  while True:
        resposta = input("Você já leu esse livro? (s/n): ").strip().lower()
        if resposta.startswith('s'):
            lido_bool = True
            break
        elif resposta.startswith('n'):
            lido_bool = False
            break
        else:
            print("Erro: Por favor, responda apenas com 'sim' ou 'não'.")
  try:
        preco_input = input("Digite quanto pagou no livro: ").replace(',', '.')
        preco_livro = float(preco_input)
  except ValueError:
        print("Valor inválido! Definindo preço como 0.0")
        preco_livro = 0.0
  data_registro = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
  livro = {
    "nome": nome_livro,
    "autor": autor_livro,
    "ano": ano_livro,
    "editora": editora_livro,
    "lido": lido_bool,
    "preço": preco_livro,
    "data_registro": data_registro
  }
  biblioteca.append(livro)
  print (f"Livro {nome_livro} cadastrado com sucesso!")
  retornar_menu()

def listar_livros():
  for livro in biblioteca:
    print (f"Nome: {livro['nome']}, Autor: {livro['autor']}, Ano: {livro['ano']}, Editora: {livro['editora']}, Lido: {livro['lido']}, Preço: R${livro['preço']:.2f}, Data de Registro: {livro['data_registro']}")
  retornar_menu()
  
def valor_colecao():
  valor_total = sum(livro['preço'] for livro in biblioteca)
  print (f"Valor total da coleção: R${valor_total:.2f}")
  retornar_menu()
  
def deletar_livro():
  nome_livro = input ("Digite o nome do livro que deseja deletar: ")
  for livro in biblioteca:
    if livro['nome'] == nome_livro:
      biblioteca.remove(livro)
      print (f"Livro {nome_livro} deletado com sucesso!")
      retornar_menu()
  print (f"Livro {nome_livro} não encontrado na biblioteca.")
  retornar_menu()

def atualizar_livro():
  nome_livro = input ("Digite o nome do livro que deseja atualizar: ")
  for livro in biblioteca:
    if livro['nome'] == nome_livro:
      autor_livro = input ("Digite o novo nome do autor: ")
      ano_livro = input ("Digite o novo ano de publicação: ")
      editora_livro = input ("Digite o novo nome da editora: ")
      lido = input ("Você já leu esse livro completamente? (s/n): ")
      livro['autor'] = autor_livro
      livro['ano'] = ano_livro
      livro['editora'] = editora_livro
      livro['lido'] = lido
      print (f"Livro {nome_livro} atualizado com sucesso!")
      retornar_menu()
  print (f"Livro {nome_livro} não encontrado na biblioteca.")
  retornar_menu()
  
def listar_numero_lidos_nao_lidos():  
  lidos = sum(1 for livro in biblioteca if livro['lido'])
  nao_lidos = sum(1 for livro in biblioteca if not livro['lido'])
  print (f"Livros lidos: {lidos}")
  print (f"Livros não lidos: {nao_lidos}")
  retornar_menu()

def finalizar_app():
  print ("Encerrando o aplicativo. Obriado por usar a Biblioteca Pessoal!")
  exit()
  
def retornar_menu():
  input ("Aperte Enter para retornar ao menu principal...")
  main()
  
def opcao_invalida():
  print ("Opção inválida. Por favor, escolha uma opção válida.")

def listar_titulo():
  print (''' 
██████╗░██╗██████╗░██╗░░░░░██╗░█████╗░████████╗███████╗░█████╗░░█████╗░
██╔══██╗██║██╔══██╗██║░░░░░██║██╔══██╗╚══██╔══╝██╔════╝██╔══██╗██╔══██╗
██████╦╝██║██████╦╝██║░░░░░██║██║░░██║░░░██║░░░█████╗░░██║░░╚═╝███████║
██╔══██╗██║██╔══██╗██║░░░░░██║██║░░██║░░░██║░░░██╔══╝░░██║░░██╗██╔══██║
██████╦╝██║██████╦╝███████╗██║╚█████╔╝░░░██║░░░███████╗╚█████╔╝██║░░██║
╚═════╝░╚═╝╚═════╝░╚══════╝╚═╝░╚════╝░░░░╚═╝░░░╚══════╝░╚════╝░╚═╝░░╚═╝

██████╗░███████╗░██████╗░██████╗░█████╗░░█████╗░██╗░░░░░
██╔══██╗██╔════╝██╔════╝██╔════╝██╔══██╗██╔══██╗██║░░░░░
██████╔╝█████╗░░╚█████╗░╚█████╗░██║░░██║███████║██║░░░░░
██╔═══╝░██╔══╝░░░╚═══██╗░╚═══██╗██║░░██║██╔══██║██║░░░░░
██║░░░░░███████╗██████╔╝██████╔╝╚█████╔╝██║░░██║███████╗
╚═╝░░░░░╚══════╝╚═════╝░╚═════╝░░╚════╝░╚═╝░░╚═╝╚══════╝''')
  
def listar_opcoes():
  print ("1 - Cadastrar Livro")
  print ("2 - Listar Livros")
  print ("3 - Deletar Livro")
  print ("4 - Atualizar Livro")
  print ("5 - Valor da Coleção")
  print ("6 - Listar número de livros lidos e não lidos da coleção")
  print ("7 - Sair")

def escolher_opcao():
  try:
    opcao_escolhida = int(input ("Digite o número da opção desejada: "))
    if opcao_escolhida == 1:
      cadastrar_livro()
    elif opcao_escolhida == 2:
      listar_livros()
    elif opcao_escolhida == 3:
      deletar_livro()
    elif opcao_escolhida == 4:
      atualizar_livro()
    elif opcao_escolhida == 5:
      valor_colecao()
    elif opcao_escolhida == 6:
      listar_numero_lidos_nao_lidos()
    elif opcao_escolhida == 7:
      finalizar_app()
    else:
      opcao_invalida()
  except ValueError:
    opcao_invalida()
  
def main():
  os.system('cls')
  listar_titulo()
  listar_opcoes()
  escolher_opcao()

if __name__ == "__main__":
  main()
  
''' Falta implementar:
- Buscar livro por chave (nome, autor, editora)
- Ordenar livros por nome, autor, editora, ano
- Salvar biblioteca em arquivo (txt, json, csv)
- Ler biblioteca de arquivo (txt, json, csv)
- Melhorar opcao de atualizar livro (perguntar quais campos deseja atualizar)
- No cadastro, colocar qual o tipo de livro (livro, manga, revista, hq)
''' 