import os
def init():
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

#today = init()
#print(today) #retornando tipo tuple

def verifyData():
    if os.path.exists('data.txt'):
        print('existe')
    else:
        os.system('echo Contagem: 0 > data.txt')
        os.system(fr'attrib -H C:\Users\{os.getlogin()}\MirandaAV\serial_key.txt') #desoculta
        os.system(fr'attrib +H C:\Users\{os.getlogin()}\MirandaAV\serial_key.txt') #oculta

def getContagem():
    file = open('data.txt', 'r')
    contagem = file.readlines()
    file.close()
    contagem = contagem[0][-3]
    return contagem

# contagem = getContagem()
# print(contagem)
