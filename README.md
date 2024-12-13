# Primeira experiencia de trabalho (Freelance): Uma solução para a Loja de Livros: [Sebo Baleia](https://www.instagram.com/sebobaleia/)<br>

## Problema: Precisava de alguns dados cadastrados do site numa planília de Excel para organizar o acervo físico

### O que eu fiz nesse Job:
1. Extrair dados de uma página Html;

- Baixei 4 páginas do Acervo Virtual para a empresa pelo site da [Estante Virtual](https://www.estantevirtual.com.br/); 

2. Verifiquei um padrão com as tags "td" (table data) com as classes html relacionadas a títulos (acervo-titulo) e os preços (acervo-preco text-center). Daí eu poderia:

3. Extrair títulos e os preços (exemplos: [títulos.txt](titulos.txt) e [preços.txt](precos.txt))
4. Gerei [números com um contador](contador.py) dependendo de cada linha no Excel;

5. Reuni os dados numa panília do Excel.

### Novidade: Melhorias no Programa
- Agora ao invés de gerar em arquivos de texto
- O programa gerará num arquivo Excel diretamente

### Ferramentas usadas

- [Python](https://www.python.org/)
- [BeautifulSoup4](https://pypi.org/project/beautifulsoup4/)
- [Requests](https://pypi.org/project/requests/)
- [Chardet](https://pypi.org/project/chardet/)

### Exemplo com uma empresa aleatória
- [Drogasil](https://www.drogariasaopaulo.com.br/medicamentos/Gen%C3%A9ricos?PS=48&map=c,specificationFilter_392)
- Irei pegar os títulos e preços dessa página acima irei extrair e colocar numa planília do excel

## Verifique que você tenha Python, BeautifulSoup, o Requests e o Chardet instalado:

```py
    pip install beautifulsoup4
    pip install requests
    pip install chardet
```

## Tutorial para usar com sua página Web

0. Clone esse repositório na sua máquina local e instale o [Python]((https://www.python.org/downloads/)) e as biliotecas
1. Pegue seu arquivo Html/Xml e coloque nessa pasta clonada
3. 
