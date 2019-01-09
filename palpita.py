def palpite(qtde,bolas,minimo,dataframe):
    """
    Função que retorna a quantidade de palpites solicitada
    requerimento:
        qtde = qtde de palpites que deve ser retornado
        bolas = qtde de bolas que devem ser sorteadas no palpite
        minimo = qtde minima de bolas para o tipo de jogo que será processado, usado tambem para percorrer as dezenas do df
        dataframe = dataframe que será processado
    retorna: palpites de jogos com base nos numeros da base
    """
    # Importando as bibliotecas
    
    import random
    import pandas as pd
    
    # Primeira parte - montar um DF com os numeros mais sorteados em cada posição
    
    dezenas = pd.DataFrame()
    pos = 1
    if bolas < minimo: #se a quantidade de palpites pedida for menor que o minimo
        bolas = minimo
    for i in range(minimo):
        bola = str(pos) #nome da coluna
        dezenas[pos] = dataframe[bola].value_counts().nlargest(bolas).index #nlargest para pegar os numeros com maior ocorrência
        pos += 1
    
    # Segunda parte - elaborar os palpites de forma randomica com os numeros do dataframe gerado 
    
    for palpite in range(qtde): #iremos rodar a mesma quantidade de palpites pedido
        jogo = [] #lista para armazenar os numeros
        pos = 1 #para percorrer as dezenas do df
        while len(jogo) < bolas: #enquanto a qtde de numeros for menor que 15 (que é o qtde de numeros que podemos jogar)
            n = str(random.choice(dezenas[pos])) #selecionar um numero randomico no df de numeros mais sorteados
            if n not in jogo: #se o numero sorteado não estiver no palpite
                jogo.append(n) #vamos incluir
                pos += 1 #passar para a próxima dezena
                if pos > minimo:
                    pos = 1
       
        # Impressão do palpite
        
        print('Palpite', palpite + 1)
        for num in jogo:
            print(num,'- ',end='')
        print('\n')
            
    return
