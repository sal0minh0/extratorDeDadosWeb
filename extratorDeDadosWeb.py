import requests
from bs4 import BeautifulSoup
# a biblitoteca bs4 é um html parser ou xml parser
import chardet
# bibliote chardet é usada para detectar a codificação de textos ou arquivos

# Caminho para o arquivo HTML
caminho_arquivo = 'arquivo_exemplo.html'

# Detecta a codificação do arquivo
with open(caminho_arquivo, 'rb') as arquivo:
    raw_data = arquivo.read()
    resultado = chardet.detect(raw_data)
    encoding = resultado['encoding']

# Agora, use a codificação detectada para abrir o arquivo
with open(caminho_arquivo, 'r', encoding=encoding) as arquivo:
    conteudo_html = arquivo.read()

# Parseia o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(conteudo_html, 'lxml')

# Encontra as tags 'td' com classe 'acervo-titulo'
titulos = soup.find_all("td", class_="acervo-titulo")

# Para cada 'td', encontra o título dentro da tag 'strong'
titulos_strong = [td.find("strong") for td in titulos if td.find("strong")]

# Encontra os preços
precos = soup.find_all("td", class_="acervo-preco text-center")

# Define o número mínimo de itens entre títulos e preços
min_length = min(len(titulos_strong), len(precos))

# Cria uma lista de tuplas (título, preço) até o número mínimo
titulos_precos = [(titulos_strong[i].get_text(strip=True), precos[i].get_text(strip=True)) for i in range(min_length)]

# Ordena a lista de tuplas com base no título (primeiro elemento da tupla)
titulos_precos_ordenados = sorted(titulos_precos, key=lambda x: x[0])

# Caminho do arquivo de saída
caminho_saida = 'precos4.txt'

# Escreve os títulos e preços ordenados em um arquivo de texto
with open(caminho_saida, 'w', encoding='utf-8') as arquivo_saida:
    for titulo, preco in titulos_precos_ordenados:
        arquivo_saida.write(f"{preco}\n")
        # Exibe os títulos restantes sem preços, se houver
    if len(titulos_strong) > min_length:
        print("\nTítulos sem preços correspondentes:\n")
        for i in range(min_length, len(titulos_strong)):
            print(f"{titulos_strong[i].get_text(strip=True)}")

# Exibe os preços restantes sem títulos, se houver
    if len(precos) > min_length:
        print("\nPreços sem títulos correspondentes:\n")
        for i in range(min_length, len(precos)):
            print(f"{precos[i].get_text(strip=True)}")

# Mensagem de confirmação
print(f"Lista de títulos e preços foi escrita em '{caminho_saida}'.")
