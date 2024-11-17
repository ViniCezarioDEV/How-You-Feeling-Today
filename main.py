import os
import plotly.graph_objects as go
from datetime import date

def FeelingToday():
    myFeeling = int(input('Como você está se sentindo hoje?\n>>> '))
    # 1 muito triste
    # 2 triste
    # 3 neutro
    # 4 feliz
    # 5 muito feliz
    if myFeeling == 1:
        return 1
    elif myFeeling == 2:
        return 2
    elif myFeeling == 3:
        return 3
    elif myFeeling == 4:
        return 4
    elif myFeeling == 5:
        return 5

def Data():
    if os.path.exists('data.txt'):
        pass
    else:
        os.system('echo Contagem: 0 > data.txt')
        os.system(fr'attrib +H data.txt')  # oculta

def GetContagem():
    with open('data.txt', 'r') as file:
        contagem = file.readlines()[0]  # apenas a primeira linha
        if "Contagem:" in contagem:
            partes = contagem.split("Contagem: ")
            if len(partes) > 1 and partes[1].strip().isdigit():
                return int(partes[1].strip())
    return 0

def VerifyContagem():
    contagem = GetContagem()
    if contagem > 6:
        GenerateGraph()

def UpdateContagem():
    with open('data.txt', 'r') as file:
        linhas = file.readlines()

    # Atualiza a contagem na primeira linha
    contagem_atual = GetContagem()  # Pega a contagem atual
    nova_contagem = contagem_atual + 1
    linhas[0] = f"Contagem: {nova_contagem}\n"

    # Escreve as linhas de volta no arquivo
    os.system(fr'attrib -H data.txt')  # desoculta
    with open('data.txt', 'w') as file:
        file.writelines(linhas)
    os.system(fr'attrib +H data.txt')  # oculta

def SetData():
    with open('data.txt', 'a') as file:
        data = FeelingToday()
        file.write(f'{data}\n')

def GenerateGraph():
    days = ['Segunda-feira', 'Terça-feira', 'Quarta-feira', 'Quinta-feira', 'Sexta-feira', 'Sábado', 'Domingo']
    # Dados do gráfico
    x = []  # dias da semana
    y = []  # sentimentos

    today = date.today()
    weekdayNumber = today.weekday()  # monday == 0, sunday == 6
    for i in range(7):  # executa 7 vezes
        weekday = (weekdayNumber - i) % 7  # Ajusta a indexação dos dias
        x.append(days[weekday])
    x.reverse()  # para reverter a lista, para quando criar o gráfico mostrar desde quando você começou a fazer os registros

    with open('data.txt', 'r') as file:
        lines = file.readlines()
        for i in range(7):  # itera 7 vezes, pois terão 7 registros
            feeling = lines[i + 1]  # soma 1, pois a primeira linha é contador
            y.append(int(feeling.strip()))  # Adiciona os sentimentos como inteiros
    y.reverse()  # para reverter a lista, assim acompanhando a lista x

    # Criando o gráfico
    fig = go.Figure()
    fig.add_trace(go.Scatter(
        x=x, y=y,  # Agora passando os valores diretamente para o gráfico
        mode='lines+markers',
        name='Feelings',
        marker=dict(
            color='purple',  # Define a cor dos marcadores
            size=10           # Tamanho das bolinhas
        )
    ))

    fig.update_layout(
        title='Resumo dos sentimentos ao decorrer da semana',
        xaxis_title='Dias',
        yaxis_title='Sentimento',
        template='plotly_dark',
        yaxis=dict(
            tickmode='array',
            tickvals=[1, 2, 3, 4, 5],  # Valores numéricos no eixo Y
            ticktext=['Muito triste', 'Triste', 'Neutro', 'Feliz', 'Muito feliz'],  # Texto correspondente
        )
    )

    fig.show()
    DeleteData()
    exit()

def DeleteData():
    os.remove('data.txt')

# Fluxo do programa
Data()
SetData()
UpdateContagem()
VerifyContagem()
