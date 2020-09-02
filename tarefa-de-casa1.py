# Solução da mscalil

a = input ("Qual o aporte anual? ")
i = input ("Qual a taxa de juros anual? ")
t = input ("Por quantos anos será feito o investimento? ")

a_int = float(a)
i_int = float(i)
t_int = float(t)
i_float = float(i_int/100)

m = (a_int*((1 + i_float)**t_int-1))/i_float

print("Você terá R$"+str(m))


# Trocar anual por mensal
# https://forex-social.com/ferramentas/calculadora-lucros-aportes/
