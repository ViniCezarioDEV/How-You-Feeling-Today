import os
def FeelingToday():
    myFeeling = int(input('como vc esta se sentindo hoje?'))
    observation = input('digite um texto (opcional)')
    # 1 muito triste
    # 2 triste
    # 3 neutro
    # 4 feliz
    # 5 muito feliz
    if myFeeling == 1:
        return 1, observation
    elif myFeeling == 2:
        return 2, observation
    elif myFeeling == 3:
        return 3, observation
    elif myFeeling == 4:
        return 4, observation
    elif myFeeling == 5:
        return 5, observation

def Data():
    if os.path.exists('data.txt'):
        print('existe')
    else:
        os.system('echo Contagem: 0 > data.txt')
        os.system(fr'attrib +H data.txt') #oculta

def GetContagem():
    with open('data.txt', 'r') as file:
        contagem = file.readlines()[0] #apenas a primeira linha
        if "Contagem:" in contagem:
          partes = contagem.split("Contagem: ")
          if len(partes) > 1 and partes[1].strip().isdigit():
            return int(partes[1].strip())
    return 0

def VerifyContagem():
    contagem = GetContagem()
    if contagem > 7:
        pass
        #gerar o grafico
        #feedback mediante grafico
        #apagar o arquivo data.txt

        #assim que executar o script pela segunda vez com 1 registro,
        #o data.txt ainda estará aqui, mas quando der 7 registros,
        #apagará o data.txt, pois assim, é so executar o script dnv sem nenhum problema


def UpdateContagem():
    with open('data.txt', 'r') as file:
        linhas = file.readlines()

    # Atualiza a contagem na primeira linha
    contagem_atual = GetContagem()  # Pega a contagem atual
    nova_contagem = contagem_atual + 1
    linhas[0] = f"Contagem: {nova_contagem}\n"

    # Escreve as linhas de volta no arquivo
    os.system(fr'attrib -H data.txt') #desoculta
    with open('data.txt', 'w') as file:
        file.writelines(linhas)
    os.system(fr'attrib +H data.txt') #oculta


def SetData():
    with open('data.txt', 'a') as file:
        data = FeelingToday()
        file.write(f'{data[0]}:{data[1]}\n')

# Fluxo do programa
Data()
SetData()
UpdateContagem()

