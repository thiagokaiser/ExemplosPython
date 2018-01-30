import xlwt

def gera_excel(nomeaba,dados, cabecalho):
    rows  = dados
    rows2 = cabecalho
    ws = wb.add_sheet(nomeaba)

    row_num = 0
    font_style = xlwt.XFStyle()
    font_style.font.bold = True
    
    if cabecalho:        
        style = xlwt.easyxf('pattern: pattern solid, fore_colour gray25; font: colour black, bold True; align: horiz center;'
                            'borders: left thin, right thin, top thin, bottom thin;')
        ws.write_merge(0, 0, 0, 6, 'Long Cell',style=style)
        row_num += 1
        cabecalho2 = ['Username', 'First name', 'Last name', 'Email address', ]
        for col_num in range(len(cabecalho2)):
            ws.write(row_num, col_num, cabecalho2[col_num], style=style)            
        for row in rows2:
            row_num += 1
            for col_num in range(len(row)):
                ws.write(row_num, col_num, row[col_num], style=style)            
        row_num += 1

    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    columns = ['Username', 'First name', 'Last name', 'Email address', ]

    for col_num in range(len(columns)):
        ws.write(row_num, col_num, columns[col_num], font_style)

    # Sheet body, remaining rows
    font_style = xlwt.XFStyle()

    
    for row in rows:
        row_num += 1
        for col_num in range(len(row)):
            ws.write(row_num, col_num, row[col_num], font_style)

    
wb = xlwt.Workbook(encoding='utf-8')

#cabecalho = {'empresa': 'teste01', 'campo2' : 'campo'}
cabecalho = ['1234']

dados = ['1234','5678']
gera_excel('user',dados,cabecalho)

wb.save('teste.xls')
