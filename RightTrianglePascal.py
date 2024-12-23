import sympy as sp
# Initiation
a,b = sp.symbols('a b')
list = []
max_value = int(input("masukkan angka : "))
n = 0

# Looping for power
while n < max_value :
    if n == 0 :
        list.append("1\n")
    elif n == 1 :
        list.append("1 1\n")
    else :   
        list.append("1 ")
        expr = str(sp.expand((a+b)**n))       
        list_expression = expr.split("+")
        for i in range(1,(len(list_expression)-1)) :
            term = str(list_expression[i]).strip()
            index = term.index("*")
            coeff = term[0:index]
            list.append(coeff + " ")
        list.append("1\n")
    
    n += 1

result = "".join(list)
print(result)

# Output

# 1
# 1 1
# 1 2 1
# 1 3 3 1
# 1 4 6 4 1
# 1 5 10 10 5 1
# 1 6 15 20 15 6 1
# 1 7 21 35 35 21 7 1
# 1 8 28 56 70 56 28 8 1
# 1 9 36 84 126 126 84 36 9 1


