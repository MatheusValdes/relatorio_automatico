
# consumo per capta de água no DF
consumo_per_capta_DF = {
    'ano':[2013,2014,2015,2016,2017,2018,2019],
    'consumo':[165,163,152,151,134,133,140]
}
# consumo per capta de água por Regiao administrativa
consumo_per_capta_RA = {
    'RA':['Lago Sul','Lago Norte','Plano Piloto','Park Way','Guará','Águas Claras','Taguatinga'],
    'consumo':[399,323,226,224,137,136,134]
}
ref_OMS = 110

def valores(consumo,hab):

    return consumo_per_capta_RA

def conta(consumo,num=1):#volume total e numero de economias
        vol = consumo/num # volume por economia
        faixas = { #faixas das tarifas cobrada pela CAESB
            'faixa':[[1,7],[8,13],[14,20],[21,30],[31,45],[46,9999999]],
            'volume':[7,6,7,10,15,None],
            'tarifa':[2.99,3.59,7.10,10.66,17.05,23.87],
            'tarifa-fixa':[16],
        }
        aux = list()#variavel auxiliar para volume de cada faixa
        aux2 = list() # receber valor percentual de cada faixa
        valor = list()#variavel auxiliar para valor de cada faixa
        label = list()
        if faixas['tarifa-fixa']:
            valor.append(faixas['tarifa-fixa'][0]*num)
            label.append('tarifa fixa')
        for i in range(len(faixas['faixa'])):# calcular o valor de cada faixa 
            if vol > faixas['faixa'][i][1]:            
                aux.append(faixas['volume'][i]*num)
                valor.append(aux[i]*faixas['tarifa'][i]*2)
                label.append(str(faixas['tarifa'][i]))
            else:
                aux.append((vol-faixas['faixa'][i][0]+1)*num)
                valor.append(aux[i]*faixas['tarifa'][i]*2)
                label.append(str(faixas['tarifa'][i]))
                break
        
           
        for i in range(len(aux)):
            aux2.append(aux[i]/(faixas['volume'][i]*num))
        
        # economia para cair de tarifa
        reducao = [consumo-sum(aux[:i]),(consumo-sum(aux[:i]))/consumo]
        eco = [sum(valor)-sum(valor[:-1]),(sum(valor)-sum(valor[:-1]))/sum(valor)]
        
        
        
        output = {
            'valor':round(sum(valor),2),
            'media':round(vol,2),
            'percent_faixa':aux2,
            'faixa':round(faixas['tarifa'][i],2),
            'reducao_abs':str(reducao[0])+'m³',
            'reducao_percent':str(round(100*reducao[1],2))+'%',
            'economia_abs':' R$'+ str(round(eco[0],2)),
            'economia_percent': str(round(100*eco[1],2))+'%',
            'gasto_faixas':valor,
            'faixas':label
        }
        return output #round(sum(valor),2),aux2,faixas['tarifa'][i],reducao,eco