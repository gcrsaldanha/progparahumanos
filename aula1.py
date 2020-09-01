c = input("Qual o valor inicial do investimento?")
i = input("Qual a taxa de juros anual?")
t = input("Qual o prazo do investimento?")

c_int = int(c)
i_int = int(i)
t_int = int(t)

i_float = i_int/100

m = c_int * (1 + i_float) ** t_int

print(m)


