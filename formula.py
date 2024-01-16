import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

def calcular_preco_teto():
    try:
        # Limpar a tela no início do programa
        limpar_tela()

        # Solicitar ao usuário para inserir os dados necessários
        dividendo_ttm = float(input("Insira o dividendo anual por ação: ").replace(',', '.'))
        porcentagem_dividendo = float(input("Insira a porcentagem desejada do dividendo): ").replace(',', '.'))

        # Calcular o preço teto usando a fórmula simplificada
        preco_teto = dividendo_ttm / (porcentagem_dividendo / 100)

        # Exibir o resultado
        print(f"O preço teto estimado da ação é: {preco_teto:.2f}")
    except ValueError:
        print("Por favor, insira valores numéricos válidos.")

def reiniciar_programa():
    reiniciar = input("Deseja reiniciar o programa? (s/n): ")
    return reiniciar.lower() == 's'

while True:
    calcular_preco_teto()
    if not reiniciar_programa():
        break
