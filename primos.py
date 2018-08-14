i = 1
fim = 100
primo = False

def ehprimo(num):
    x = 1
    i_primo = 0
    while x < num:        
        if (num % x) == 0 :
            i_primo = i_primo + 1            
        
        x = x + 1
    if i_primo > 1:
        return False
    else:
        return True

while i < fim:    
    if ehprimo(i) == True:
        print(i)   
    
    i = i + 1




    
