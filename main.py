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

today = init()
print(today) #retornando tipo tuple

