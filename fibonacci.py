var_1 = int(input("informe ate que numero deseja repetir"))
atual = int(input("informe o numero para comecar"))

anterior = 0

while atual < var_1:                  
    if anterior == 0:
        print(atual)
    fib = atual + anterior
    anterior = atual
    atual = fib    
    print(fib)

