import requests
from bs4 import BeautifulSoup
import chardet
import pandas as pd

# Caminho para o arquivo HTML
caminho_arquivo = 'MedicamentosGenericos.html'

# Detecta a codificação do arquivo
with open(caminho_arquivo, 'rb') as arquivo:
    dados = arquivo.read()
    resultado = chardet.detect(dados)
    encoding = resultado['encoding']

# Agora, use a codificação detectada para abrir o arquivo
with open(caminho_arquivo, 'r', encoding=encoding) as arquivo:
    conteudo_html = arquivo.read()

# Parseia o conteúdo HTML usando o BeautifulSoup
soup = BeautifulSoup(conteudo_html, 'lxml')

# Encontra os titulos as tags 'td' com classe 'acervo-titulo'
titulos = soup.find_all("td", class_="collection-link")

# Para cada 'td', encontra o título dentro da tag 'strong'
titulos_strong = [td.find("strong") for td in titulos if td.find("strong")]

# Encontra os preços
precos = soup.find_all("td", class_="valor-por") <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<- MODIFICAR PELAS CLASSES DESSA PAGINA

# Define o número mínimo de itens entre títulos e preços
min_length = min(len(titulos_strong), len(precos))

# Cria uma lista de tuplas (título, preço) até o número mínimo
titulos_precos = [(titulos_strong[i].get_text(strip=True), precos[i].get_text(strip=True)) for i in range(min_length)]

# Ordena a lista de tuplas com base no título (primeiro elemento da tupla)
titulos_precos_ordenados = sorted(titulos_precos, key=lambda x: x[0])

# Cria um DataFrame do pandas
df = pd.DataFrame(titulos_precos_ordenados, columns=['Título', 'Preço'])

# Caminho do arquivo de saída
caminho_saida_excel = 'precos.xlsx'

# Salva o DataFrame em um arquivo Excel
df.to_excel(caminho_saida_excel, index=False)

# Mensagem de confirmação
print(f"Lista de títulos e preços foi escrita em '{caminho_saida_excel}'.")

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