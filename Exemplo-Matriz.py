var_matriz  = ['teste','cachorro','casa','carro']
var_matriz2 = ['asdasdasd','casa','cccc','gggggg']
var_result = []
for i in var_matriz:
    l = False
    for i2 in var_matriz2:
        if i == i2 and l == False:
            l = True

    result = [i, l]
    var_result.append(result)            

for i3 in var_result:
    if i3[1] == False:
        print(i3)
        var_result.remove(i3)

for i2 in var_result:
    print(i2)
