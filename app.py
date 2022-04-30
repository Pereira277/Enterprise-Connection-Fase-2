list = [
#   empresa, senha, ajuda, numero, nome, mail, data, criticidade
    ["Canva",False,False,True,False,False, 2019, 0],
    ["Hurb",False,False,True,False,False, 2020, 0],
    ["Adobe",True,False,False,False,False, 2019, 0],
    ["Fiap",False,True,False,False,False, 2018, 0],
    ["Google",False,False,True,False,False, 2015, 0],
    ["Facebook",False,True,True,False,False, 2022, 0],
    ["Instagram",False,False,False,False,False, 2010, 0],
    ["Reddit",False,False,True,False,False, 2008, 0],
    ["Mercadolivre",False,True,True,False,False, 2022, 0],
    ["Amazon",False,True,False,False,False, 2019, 0],
    ["Twitter",True,True,True,True,False, 2016, 0],
    ["Notion",False,True,True,True,True, 2021, 0],
    ["Microsoft",False,False,False,False,False, 2005, 0],
    ["Steam",True,True,False,False,False, 2019, 0],
    ["Whatsapp",True,True,True,False,True, 2022, 0],
    ["Telegram",False,False,True,False,False, 2020, 0],
    ["Spotify",False,True,True,True,False, 2019, 0],
    ["Uber",False,True,True,True,True, 2020, 0],
    ["Linkedin",False,False,True,True,True, 2020, 0],
    ["Discord",False,False,False,True,True, 2019, 0],
]

def criticidade(list):
    # Define o valor de criticidade do vazamento
    for i in range(len(list)):
        for j in range(1,6):
            if list[i][j] == True:
                if j == 5:
                    list[i][7] += 5
                if j == 4:
                    list[i][7] += 10
                if j == 3:
                    list[i][7] += 20
                if j == 2:
                    list[i][7] += 40
                if j == 1:
                    list[i][7] += 80  

    # Bubble sort
    for i in range(len(list)-1):
        for j in range(0, len(list)-i-1):
            if list[j][7] < list[j + 1][7]:
                list[j], list[j + 1]= list[j + 1], list[j]
            # Desempata utilizando a data 
            if list[j][7] == list[j + 1][7]:
                if list[j][6] < list[j + 1][6]:
                    list[j], list[j + 1]= list[j + 1], list[j]

    # Printa o resultado
    for i in range(len(list)):
        print("{} - {}".format(i+1, list[i][0]))

criticidade(list)