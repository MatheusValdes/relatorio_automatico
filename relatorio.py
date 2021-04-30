##### Rotina para gerar relatório de consumo
##### Inserção manual dos dados
##### instalar o pacote FPDF (pip install fpdf )

import pandas as pd
import matplotlib.pyplot as plt
from funcoes import conta
from modelo_pdf import PDF

###### ENTRADAS #######
consumo = 716 # consumo de água em m³ 
n_eco = 37 #numero de economias
n_quartos = 2 #numero de quartos por apt
####### DADOS #####
consumo_per_capta_RA = {
    'RA':['Lago Sul','Lago Norte','Plano Piloto','Park Way','Guará','Águas Claras','Taguatinga'],
    'consumo':[399,323,226,224,137,136,134]
}

##### programacao #####
saida = conta(consumo,n_eco)
c_percapta = [[],[]]

for k in range(n_quartos,n_quartos+3):
    c_percapta[1].append(round((1000/(k*30))*saida['media'],2))
    c_percapta[0].append(f'{k} pessoas por apt')
    consumo_per_capta_RA['RA'].append(f'{k} pessoas por apt')
    consumo_per_capta_RA['consumo'].append(round((1000/(k*30))*saida['media'],2))

df = pd.DataFrame.from_dict(consumo_per_capta_RA)

#### Plotar graficos comparativos 
labels = df.sort_values(by=['consumo'])['RA'].tolist()
values = df.sort_values(by=['consumo'])['consumo'].tolist()

# Change the bar colors here
color = list()
for j in range(len(values)):
    if labels[j][0].isdigit():
        color.append('red')
    else:
        color.append('blue')
plt.figure(figsize=(12, 7))

plt.barh(labels, values, color=color)
for index, value in enumerate(values):
    plt.text(value, index, str(value),fontsize=12)
# plt.xticks(labels, rotation=90)
plt.tick_params(axis='x', which='major', labelsize=13)
plt.tick_params(axis='y', which='major', labelsize=13)
# plt.ylabel('Regiões administrativas')
plt.xlabel('Consumo (litros)',fontsize=13)
plt.title('Consumo diário per capta (litros/dia)',fontsize=14)
plt.savefig('consumo.png', dpi=300, bbox_inches='tight')

#### Plotar grafico das tarifas

fig = plt.figure()
ax = fig.add_axes([0,0,1,1])
x = saida['faixas']
y = saida['gasto_faixas']
ax.grid(axis='y')
ax.bar(x,y)
for index, value in enumerate(y):
    plt.text(index, value,'R$'+str(round(value,2)),fontsize=12,horizontalalignment='center',verticalalignment='bottom')
plt.ylabel('Gasto em reais',fontsize=16)
plt.xlabel('Faixa de tarifação',fontsize=16)
plt.xticks(fontsize=16)
plt.yticks(fontsize=14)
plt.savefig('plot1.png', dpi=300, bbox_inches='tight')
# plt.show()

#### Conteudo #####

#### Introdução
oracao1 = 'Este relatório tem como objetivo analisar de forma simples os níveis de consumo da edificação e comparar ao de consumo de outras regiões administrativas.'
oracao2 = 'Também analisamos as faixas de tarifação da CAESB e mostramos em qual faixa o consumo do edifício se encaixa, por fim mostramos quanto cada faixa custa e quanto seu edifício deve reduzir para ficar em uma faixa abaixo da atual.'
oracao3 = 'Com isso é possível identificar o potencial de economia de água e gastos mensais ao se adotar boas práticas de gestão e consumo dos recursos hídricos.'
introducao =f'{oracao1} {oracao2} {oracao3}'
##### analise de consumo
plus1 = f"De acordo com as informações fornecidas, o consumo médio por apartamento é de {saida['media']} m³/mês. "
plus2 = f"Para comparar com o consumo diário médio per capta com algumas Regiões Administrativas, precisamos estimar a quantidade de habitantes do edifício, desta forma consideramos três cenários: média de {n_quartos} a {k} habitantes por apartamento."
plus3 = "O gráfico abaixo mostra o consumo diário per capta das pessoas do edifício analisado em três cenários (vermelho) e os compara com as Regiões Admnistrativas que mais consomem água no DF (azul)."
plus4 = "Ressalta-se o fato dos valores mostrados na análise serem valores médios, ou seja, há pessoas no prédio que consomem mais do que o valor mostrado."
conteudo_consumo = f'{plus1} {plus2} {plus3} {plus4}'

#### analise de tarifa
conteudo3 = 'A CAESB possui vários tipos de tarifação, para a tafiração residencial, o faturamento da conta de água segue a tabela abaixo. De acordo com sua conta, seu condomínio está na faixa de tarifação de R$'
conteudo3 = conteudo3 + str(saida['faixa'])+'. '

conteudo4 = 'Para ficar em uma faixa de consumo mais baixa, o consumo deve diminuir em '+str(saida['reducao_abs'])+ ' (redução de '+saida['reducao_percent']+' ). '
conteudo5 = 'Caso essa medida seja adotada, o valor economizado será de R$ '+saida['economia_abs']+' (redução de '+saida['economia_percent']+'). '



#### gerar PDF ####

pdf = PDF('P','mm','A4')
pdf.set_auto_page_break(auto=True,margin=15)
pdf.add_page()
pdf.intro(introducao)
pdf.consumo(texto=conteudo_consumo,consumo=c_percapta)
pdf.add_page()
pdf.tarifas(conteudo3+conteudo4+conteudo5)

pdf.output('pdf_1.pdf')