import pickle
import os.path

class Pokemon:
    def __init__(self, numero, nome):
        self.numero = numero
        self.nome = nome

class NoPokemon:
    def __init__(self, pokemon):
        self.pokemon = pokemon
        self.esquerda = None
        self.direita = None

class ArvorePokemon:
    def __init__(self):
        self.raiz = None

    def incluir_pokemon(self, pokemon):
        if self.raiz is None:
            self.raiz = NoPokemon(pokemon)
        else:
            self._incluir_pokemon_recursivo(pokemon, self.raiz)

    def _incluir_pokemon_recursivo(self, pokemon, no_atual):
        if pokemon.numero < no_atual.pokemon.numero:
            if no_atual.esquerda is None:
                no_atual.esquerda = NoPokemon(pokemon)
            else:
                self._incluir_pokemon_recursivo(pokemon, no_atual.esquerda)
        elif pokemon.numero > no_atual.pokemon.numero:
            if no_atual.direita is None:
                no_atual.direita = NoPokemon(pokemon)
            else:
                self._incluir_pokemon_recursivo(pokemon, no_atual.direita)

    def consultar_pokemon(self, numero):
        return self._consultar_pokemon_recursivo(numero, self.raiz)

    def _consultar_pokemon_recursivo(self, numero, no_atual):
        if no_atual is None or no_atual.pokemon.numero == numero:
            return no_atual
        if numero < no_atual.pokemon.numero:
            return self._consultar_pokemon_recursivo(numero, no_atual.esquerda)
        return self._consultar_pokemon_recursivo(numero, no_atual.direita)

    def excluir_pokemon(self, numero):
        self.raiz = self._excluir_pokemon_recursivo(numero, self.raiz)

    def _excluir_pokemon_recursivo(self, numero, no_atual):
        if no_atual is None:
            return no_atual

        if numero < no_atual.pokemon.numero:
            no_atual.esquerda = self._excluir_pokemon_recursivo(numero, no_atual.esquerda)
        elif numero > no_atual.pokemon.numero:
            no_atual.direita = self._excluir_pokemon_recursivo(numero, no_atual.direita)
        else:
            if no_atual.esquerda is None:
                return no_atual.direita
            elif no_atual.direita is None:
                return no_atual.esquerda

            temp = self._encontrar_menor_pokemon(no_atual.direita)
            no_atual.pokemon = temp.pokemon
            no_atual.direita = self._excluir_pokemon_recursivo(temp.pokemon.numero, no_atual.direita)

        return no_atual

    def _encontrar_menor_pokemon(self, no):
        atual = no
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual

    def maior_pokemon(self):
        atual = self.raiz
        while atual.direita is not None:
            atual = atual.direita
        return atual.pokemon

    def menor_pokemon(self):
        atual = self.raiz
        while atual.esquerda is not None:
            atual = atual.esquerda
        return atual.pokemon

    def imprimir_arvore(self):
        self._imprimir_arvore_recursivo(self.raiz)

    def _imprimir_arvore_recursivo(self, no_atual):
        if no_atual is not None:
            self._imprimir_arvore_recursivo(no_atual.esquerda)
            print(f"Número: {no_atual.pokemon.numero}, Nome: {no_atual.pokemon.nome}")
            self._imprimir_arvore_recursivo(no_atual.direita)

    def gravar_arvore_em_disco(self, arquivo):
        with open(arquivo, 'wb') as file:
            pickle.dump(self.raiz, file)

    def carregar_arvore_do_disco(self, arquivo):
        if os.path.exists(arquivo):
            with open(arquivo, 'rb') as file:
                self.raiz = pickle.load(file)
                print(f"Carregando o arquivo {arquivo}.")
        else:
            print("Arquivo não encontrado.")
            return

# Menu de interação
def menu():
    arvore_pokemon = ArvorePokemon()

    while True:
        print("\nOpções:")
        print("1. Incluir Pokémon")
        print("2. Excluir Pokémon")
        print("3. Consultar Pokémon")
        print("4. Maior Pokémon")
        print("5. Menor Pokémon")
        print("6. Imprimir árvore")
        print("7. Gravar árvore em disco")
        print("8. Carregar árvore em disco")
        print("9. Desenvolvedores")
        print("10. Sair")

        opcao = int(input("Escolha uma opção: "))

        if opcao == 1:
            numero = int(input("Digite o número do Pokémon a ser incluído: "))
            nome = input("Digite o nome do Pokémon: ")
            pokemon = Pokemon(numero, nome)
            arvore_pokemon.incluir_pokemon(pokemon)
            print(f"Pokemon {pokemon.nome} incluído com sucesso!")
        elif opcao == 2:
            numero = int(input("Digite o número do Pokémon a ser excluído: "))
            arvore_pokemon.excluir_pokemon(numero)
            print(f"Pokemon de número {numero} excluído, se existir.")
        elif opcao == 3:
            numero = int(input("Digite o número do Pokémon a ser consultado: "))
            resultado = arvore_pokemon.consultar_pokemon(numero)
            if resultado:
                print(f"O Pokémon com número {numero} foi encontrado na árvore: {resultado.pokemon.nome}")
            else:
                print(f"O Pokémon com número {numero} não está na árvore.")
        elif opcao == 4:
            maior = arvore_pokemon.maior_pokemon()
            print(f"Maior Pokémon: Número - {maior.numero}, Nome - {maior.nome}")
        elif opcao == 5:
            menor = arvore_pokemon.menor_pokemon()
            print(f"Menor Pokémon: Número - {menor.numero}, Nome - {menor.nome}")
        elif opcao == 6:
            print("Árvore de Pokémon:")
            arvore_pokemon.imprimir_arvore()
        elif opcao == 7:
            nome_arquivo = input("Digite o nome do arquivo para gravar a árvore: ")
            arvore_pokemon.gravar_arvore_em_disco(nome_arquivo)
            print(f"Árvore de Pokémon gravada no arquivo {nome_arquivo}.")
        elif opcao == 8:
            nome_arquivo = input("Digite o nome do arquivo para carregar a árvore: ")
            arvore_pokemon.carregar_arvore_do_disco(nome_arquivo)
        elif opcao == 9:
            print("Desenvolvedores: \n Victor Reis- 202210760 \n Daniel - XX \n Mateus - XX \n Everton - XX")
        elif opcao == 10:
            print("Saindo do programa...")
            break
        else:
            print("Opção inválida. Escolha novamente.")

# Iniciar o menu de interação
menu()
