# Resumo - Aula 1

> Para se inscrever na lista de e-mail e receber materiais como esse: [https://live.saldanha.dev](https://live.saldanha.dev)

> Para tirar dúvidas: [https://discord.gg/JEhamvz](https://discord.gg/JEhamvz)

> Para assistir as aulas ao vivo, segundas e quartas às 20h15: [https://twitch.tv/saldanha_dev](https://twitch.tv/saldanha_dev)

---

---

# Modo script vs Modo interativo

Normalmente escrevemos o nosso programa em um arquivo de texto com extensão `.py`, por exemplo, `aula1.py`, e então processamos esse arquivo com o `python`. Esse é o "modo script", onde escrevemos um "roteiro" (as instruções que queremos que o `python` processe) e esse roteiro é então executado.

O outro modo é o "modo interativo", muito utilizado para rascunho e testar alguns pequenos trechos de código. Nesse modo, a cada instrução fornecida, o  `python` executa essa instrução, **exibe o resultado da instrução na tela** e fica aguardando a próxima.

```python
Quando você ver o símbolo abaixo, significa que está no modo interativo
Assim, o python está aguardando a próxima instrução
>>> 
```

# Imprimindo valores na tela

```python
# Para imprimir o texto "Olá, mundo!"
print("Olá, mundo!")

# Para imprimir números ou variáveis, não utilizamos aspas
x = "Olá, mundo!"
print(x)
==> Olá, mundo!  # Funciona!

x = 10
print(x)
==> 10  # Também funciona
```

# Declarar variáveis

```python
# Armazenar o valor **inteiro** 10 em uma variável com o nome "x"
x = 10

# Armazenar o valor "Um texto" (como **texto**) na variável "y"
y = "Um texto" 
```

# Tipos de valores e variáveis

Valores e variáveis são classificados por seus **tipos**. Os que abordamos nessa aula foram:

- `int`: categoria dos números inteiros. Ex.: `x = 10`
- `float`: categoria dos números decimais (ou não-inteiros). Ex.: `x = 12.50` (lembre que usamos **`.`** ao invés de `,` para denotar casas decimais).
- `string`: categoria de textos, palavras, caracteres. Ex.: `x = "Curso de Programação"`.
    - É necessário utilizar aspas envolvendo o texto. Ou seja: `x = Oi tudo bem?` vai resultar em um erro.
    - Porém, quando tratamos números, não utilizamos aspas, senão estaríamos transformando esse número em uma **`string`.** Ex.: `x = "10"` — agora `x` armazena o valor "10" como **texto**.
- `boolean`: valores *`True`* ou *`False`.* Denotam a veracidade ou não de uma expressão. Por exemplo: `10 % 2 == 0` vai resultar em `True`.

> Podemos converter *strings* para *int* e *float* usando a função `int("10")` ou `float("10.50")`

# Lendo valores do usuário

Utilizamos a função `input("Algum texto...")` para exibir uma mensagem ao usuário (o que estiver entre as aspas) e aguardar o usuário digitar algum valor. Podemos salvar esse valor em uma variável. Exemplo: `x = input("Digite o valor de x")`

Lembre que sempre que o usuário insere um valor ele vem como ***string***. Se quisermos transformar em *int* ou *float* temos que usar `int(x)` ou `float(x)`.

# Operadores

`2 + 2 = 4`

`2 - 1 = 1`

`2 * 3 = 6`

`3 / 2 = 1.5`

`**` (Exponencial) ⇒ `2 ** 3 = 8` (2 * 2 * 2)

`//` (Divisão inteira) `3 // 2 = 1` (remove a parte decimal - depois do `.`)

`%` (Módulo, resto da divisão) ⇒ `4 % 2 = 0` e `5 % 2 = 1`.

 `+=` (Incremento) ⇒ `x += 1` é o equivalente a escrever `x = x + 1`. Ou seja, aumentar o valor da variável `x` em 1.

## Concatenação

Essa é uma operação especial feita com *strings.*

```python
>>> nome = "Gabriel"
>>> sobrenome = "Saldanha"
>>> nome + sobrenome
"GabrielSaldanha"
>>> nome + " " + sobrenome  # Note que adicionei uma string com um espaço em branco " "
"Gabriel Saldanha"

```

# Calculadora de juros compostos

Fórmula: `m = c * (1 + i) ** t`

Onde:

- `m`: montante final (resultado)
- `c`: capital inicial
- `i`: taxa de juros ao ano
- `t`: tempo do investimento (em anos)

Faça um programa que receba `c, i, t` do usuário e calcule o `m`

```python
c = input("Qual o valor inicial do investimento?")
i = input("Qual a taxa de juros anual?")
t = input("Qual o prazo do investimento?")

c_int = int(c)
i_int = int(i)
t_int = int(t)

i_float = i_int/100  # Converter a taxa (2%) para decimal (0.02)

m = c_int * (1 + i_float) ** t_int

print(m)
```

# Desafio

E se ao invés de apenas o **capital inicial** tivéssemos investimentos anuais? Ou seja, todo ano fosse depositado um valor.

Fórmula: `m = (a * ((1 + i) ** t - 1)) / i`

Onde `a` é o valor do aporte anual.