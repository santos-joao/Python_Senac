#Criando um lista simples com 3 pokémons
pokemons = ["Pikachu", "Charmander", "Bulbasaur"]

#Exibindo a lista
print("Lista de Pokémons: ", pokemons)

#Acessando o primeiro Pokémon da lista
print("Primeiro Pokémon: ", pokemons[0])

#Adicionando um novo Pokémon á lista
pokemons.append("squirtle")
print("Lista de Pkémons após adicionar Squirtle:", pokemons)

#Removendo o Pókemon "Charmander" da lista
pokemons.remove("Charmander")
print("Lista de Pokémons após remover Charmander:", pokemons)

#Exibindo o tamanho da lista
print("numero de Pokémons na lista:", len(pokemons))