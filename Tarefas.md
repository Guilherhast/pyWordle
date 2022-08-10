# Tarefas

## Original

<https://www.nytimes.com/games/wordle/index.html>

<https://term.ooo/>

## Globals

### Links

<https://docs.python.org/3/library/__main__.html>

<https://docs.python.org/3/library/os.html>

<https://docs.python.org/3/library/os.path.html#os.path.dirname>

<https://docs.python.org/3/library/os.path.html#os.path.realpath>

<https://docs.python.org/3/library/os.path.html#os.path.join>

### Instruções

Criar um arquivo chamado globals.py

Nesse arquivo devem existir variáveis que serão usadas
tanto no servidor quanto no script de configuração.


**Database**

* Caminho da pasta onde se localiza o banco de dados
* Caminho do arquivo onde ficarão todas palavras
* Caminho do arquivo onde ficarão as palavras do tamanho específico
* Caminho do arquivo onde ficará a data de início

**Config**
* Url do arquivo com palavras em portugues
* Tamanho das palavras usadas no app

**Network**

* Caminho da pasta pública no servidor
* Endereço do server (0.0.0.0)
* Porta do server
* Tupla com endereço e porta


## Server v0.0.1

### Links

<https://docs.python.org/3/library/http.server.html>

<https://pythonbasics.org/webserver/#Web-server>


<https://docs.python.org/3/library/http.server.html#http.server.BaseHTTPRequestHandler.path>

### Instruções

Crie um servidor que serve uma palavra de 5 letras.

Exemplo: serve

Esse servidor deve usar a função `get_word(path)` para recuperar a palavra.


## Server v0.0.4

### Links

<https://programtalk.com/python-examples/SimpleHTTPServer.SimpleHTTPRequestHandler.do_GET/#links-58294b18d7f9ad419842be66>

### Instruções

Crie um servidor que além da palavra serve os arquivos na
pasta `public`.

## Finalizar o front

### Links

<https://docs.python.org/3/library/functions.html#func-range>

<https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions>

<https://docs.python.org/3/tutorial/datastructures.html#more-on-lists>

<https://www.w3schools.com/xml/xml_http.asp>

<https://colab.research.google.com/drive/17deF5-umfbZzPe4JuM_Vrrfx-kkUKXzG?usp=sharing>

### Instruções

No arquivo script.py procure pela palavra 'TODO'.
Você achará as funções `get_word` e `calc_colors`.

Caso tenha problema em carregar uma nova versão do script você pode alterar a linha:

```html
<py-script src="script.py">
```

Para:

```html
<py-script src="script.py?v=2">
```

E seguir alterando a versão até concluir o front-end.

**Computation**

Use este desafio para te ajudar com a função.

<https://colab.research.google.com/drive/17deF5-umfbZzPe4JuM_Vrrfx-kkUKXzG?usp=sharing>

Altere a função `calc_colors` para retornar `'G'` para as letras corretas,  `'Y'` para as letras
presentes na palavra e  `''` para as letras incorretas.

**Request**

Altere a função `get_word` para solicitar a palavra usando o api.

## Config server


Criar um script em python que realiza as seguintes tarefas.

1. Criar pasta do banco de dados
2. Criar banco de dados principal
	- Fazer o download de um banco de dados com todas palavras em português
	- Salvar esse banco de dados no arquivo especificado
3. Criar banco de dados filtrado
	- Extrair palavras com o tamanho especificado
	- Colocar as palavras em ordem aleatória
	- Salvar essas palavras no arquivo especificado
4. Escrever em um no arquivo especificado a data de início do jogo

### Passos

**Hello**

<https://docs.python.org/3/library/__main__.html>

1. Fazer script que roda a função 'main' e escreve algo na tela

**Database**

<https://docs.python.org/3/library/os.html#os.makedirs>

<https://docs.python.org/3/library/urllib.request.html#urllib.request.urlretrieve>

1. Criar função para criar a pasta 'db_folder'
2. Criar função para fazer o download do banco de dados nesta pasta

**Processamento**

<https://docs.python.org/3/library/functions.html#open>

1. Criar função para gerar lista filtrada ( somente com palavras
do tamanho desejado ).
2. Criar função que embaralha a lista e a escreve no arquivo desejado.

**Date**

<https://docs.python.org/3/library/datetime.html#module-datetime>

<https://docs.python.org/3/library/datetime.html#datetime.date.isoformat>

1. Criar função que escreve a data atual no formato iso no arquivo desejado.

## Server

O server deve calcular e servir a palavra do dia.
Esse server pode também receber como parâmetro o dia e usá-lo caso não seja maior que o número
de dias que o server está online.

### Passos

**Alt main**

Criar uma `main` alternativa e executá-la.
Ela deve escrever algo na tela.


**Read date**

<https://docs.python.org/3/library/datetime.html#datetime.date.fromisoformat>

Criar uma função que lê a data.
(Essa e as próximas funções serão testadas usando a função `alt_main`).

**Params**

Criar uma função que lê o parâmetro day=n na url.

**Days from start**

<https://docs.python.org/3/library/re.html#re.match>

<https://docs.python.org/3.3/library/stdtypes.html?highlight=split#str.split>

<https://regex101.com/>

Use essas strings para teste:

```
localhost/
localhost/day/20
localhost/?teste=10
localhost/?day=
localhost/?day=aa
localhost/?day=20
localhost/?day=1
localhost/?day=01
```

Criar função que usa o dia atual e a data lida para dizer a quantos dias
o jogo começou.

**get nTh word**

<https://docs.python.org/3/library/linecache.html#linecache.getline>

Criar função que recebe um número n e retorna a enésima palavra.
Caso um número não seja fornecido, ela retorna a primeira palavra.

**Back to main**

Voltar a usar a função main que serve a página.
Deletar a função alternativa criada.


**Current day**

Servir a enésima palavra usando o mínimo entre o dia recebido e o dia atual.


**Final test**

Testar tudo para ver se funciona.
