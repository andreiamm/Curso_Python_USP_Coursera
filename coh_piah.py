import re

def le_assinatura():
    '''A funcao le os valores dos tracos linguisticos do modelo e devolve uma assinatura a ser comparada com os textos fornecidos'''
    print("Bem-vindo ao detector automático de COH-PIAH.")
    print("Informe a assinatura típica de um aluno infectado:\n")

    wal = float(input("Entre o tamanho médio de palavra: "))
    ttr = float(input("Entre a relação Type-Token: "))
    hlr = float(input("Entre a Razão Hapax Legomana: "))
    sal = float(input("Entre o tamanho médio de sentença: "))
    sac = float(input("Entre a complexidade média da sentença: "))
    pal = float(input("Entre o tamanho medio de frase: "))

    return [wal, ttr, hlr, sal, sac, pal]

def le_textos():
    '''A funcao le todos os textos a serem comparados e devolve uma lista contendo cada texto como um elemento'''
    i = 1
    textos = []
    texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("\nDigite o texto " + str(i) +" (aperte enter para sair): ")

    return textos

def separa_sentencas(texto):
    '''A funcao recebe um texto e devolve uma lista das sentencas dentro do texto'''
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas

def separa_frases(sentenca):
    '''A funcao recebe uma sentenca e devolve uma lista das frases dentro da sentenca'''
    return re.split(r'[,:;]+', sentenca)

def separa_palavras(frase):
    '''A funcao recebe uma frase e devolve uma lista das palavras dentro da frase'''
    return frase.split()

def n_palavras_unicas(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras que aparecem uma unica vez'''
    freq = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            if freq[p] == 1:
                unicas -= 1
            freq[p] += 1
        else:
            freq[p] = 1
            unicas += 1

    return unicas

def n_palavras_diferentes(lista_palavras):
    '''Essa funcao recebe uma lista de palavras e devolve o numero de palavras diferentes utilizadas'''
    freq = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in freq:
            freq[p] += 1
        else:
            freq[p] = 1

    return len(freq)

def compara_assinatura(as_a, as_b):
    ''' Essa funcao recebe duas assinaturas de texto e deve devolver o grau de similaridade nas assinaturas.'''
    # Subtrai os itens da lista as_a pelos itens que se encontram na mesma posição em as_b.
    # Aplica o módulo (função abs()), tornando todos os resultados positivos.
    subtracao_fa_fb = []
    valor = 0
    for i in range(len(as_b)):
        valor = as_a[i] - as_b[i]
        subtracao_fa_fb.append(abs(valor))
        valor = 0

    # Soma todos os elementos da lista que resultou da subtração de as_a por as_b.
    soma = 0
    for i in range(len(subtracao_fa_fb)):
        soma = soma + subtracao_fa_fb[i]

    # Divide por 6 a soma todos os elementos da lista que resultou da subtração de as_a por as_b.
    sab = soma / 6
    return sab

def calcula_assinatura(texto):
    ''' Essa funcao recebe um texto e deve devolver a assinatura do texto.'''
    #print("texto = ", texto)
    ''' Separa o texto em sentenças e armazena o resultado em uma lista. '''
    lista_sentencas = separa_sentencas(texto)
    qtde_sentencas = len(lista_sentencas)
    #print("lista_sentencas: ", lista_sentencas)
    #print("qtde de sentencas: ", qtde_sentencas)

    ''' Calcula quantos caracteres tem cada sentença e armazena o resultado em uma lista. '''
    lista_tamanho_sentencas = []
    for i in range(len(lista_sentencas)):
        lista_tamanho_sentencas.append(len(lista_sentencas[i]))
    #print("lista_tamanho_sentencas: ", lista_tamanho_sentencas)

    ''' Tira os espaços em branco das sentenças'''
    #sentencas_sem_espaco = []
    #for i in range(len(lista_sentencas)):
    #    for j in range(len(lista_sentencas[i])):
    #        sentencas_sem_espaco.append(lista_sentencas[i][j].replace(" ", ""))
    #print("sentencas_sem_espaco: ", sentencas_sem_espaco)

    ''' Calcula quantos caracteres tem cada sentença e armazena o resultado em uma lista. '''
    #lista_tamanho_sentencas = []
    #for i in range(len(sentencas_sem_espaco)):
    #    lista_tamanho_sentencas.append(len(sentencas_sem_espaco[i]))
    #print("lista_tamanho_sentencas: ", lista_tamanho_sentencas)

    ''' Soma o total de caracteres de todas as sentenças e armazena o resultado em uma variável '''
    soma_caracteres_sentenca = 0
    for i in range(len(lista_tamanho_sentencas)):
        soma_caracteres_sentenca = soma_caracteres_sentenca + lista_tamanho_sentencas[i]
    #print("soma_caracteres_sentenca: ", soma_caracteres_sentenca)

    ''' Separa as sentenças em frases e armazena o resultado em uma lista. '''
    lista_frases = []
    for i in range(len(lista_sentencas)):
           lista_frases.append(separa_frases(lista_sentencas[i]))
    #print("lista_frases: ", lista_frases)

    ''' Coloca cada frase em uma linha da lista. '''
    lista_frases_isoladas = []
    for i in range(len(lista_frases)):
        for j in range(len(lista_frases[i])):
            lista_frases_isoladas.append(lista_frases[i][j])
    qtde_frases = len(lista_frases_isoladas)
    #print("lista_frases_isoladas: ", lista_frases_isoladas)

    ''' Calcula quantos caracteres tem cada frase e armazena o resultado em uma lista. '''
    lista_tamanho_frases = []
    for i in range(len(lista_frases_isoladas)):
        lista_tamanho_frases.append(len(lista_frases_isoladas[i]))
    #print("lista_tamanho_frases: ", lista_tamanho_frases)

    ''' Soma o total de caracteres de todas as frases e armazena o resultado em uma variável '''
    soma_caracteres_frase = 0
    for i in range(len(lista_tamanho_frases)):
        soma_caracteres_frase = soma_caracteres_frase + lista_tamanho_frases[i]
    #print("soma_caracteres_frase: ", soma_caracteres_frase)

    ''' Separa as frases em palavras e armazena o resultado em uma lista. '''
    lista_palavras = []
    for i in range(len(lista_frases_isoladas)):
        lista_palavras.append(separa_palavras(lista_frases_isoladas[i]))

    ''' Coloca cada palavra em uma linha da lista. '''
    lista_palavras_isoladas = []
    for i in range(len(lista_palavras)):
        for j in range(len(lista_palavras[i])):
            lista_palavras_isoladas.append(lista_palavras[i][j])
    total_palavras = len(lista_palavras_isoladas)
    #print("lista_palavras_isoladas: ", lista_palavras_isoladas)

    ''' Calcula quantos caracteres tem cada palavra e armazena o resultado em uma lista. '''
    lista_tamanho_palavras = []
    for i in range(len(lista_palavras_isoladas)):
        lista_tamanho_palavras.append(len(lista_palavras_isoladas[i]))

    ''' Soma o total de caracteres de todas as palavras e armazena o resultado em uma variável '''
    soma_caracteres = 0
    for i in range(len(lista_tamanho_palavras)):
        soma_caracteres = soma_caracteres + lista_tamanho_palavras[i]

    ''' Calcula o tamanho médio das palavras (soma dos tamanhos das palavras dividida pelo número total de palavras). '''
    tamanho_medio_palavra = soma_caracteres / total_palavras

    ''' Calcula a relação type-token (número de palavras diferentes dividido pelo número total de palavras). '''
    relacao_type_token = n_palavras_diferentes(lista_palavras_isoladas) / total_palavras

    ''' Calcula a Razão Hapax Legomana (número de palavras que aparecem uma única vez dividido pelo total de palavras). '''
    hapax_legomana = n_palavras_unicas(lista_palavras_isoladas) / total_palavras

    ''' Calcula o tamanho médio de sentença (soma dos números de caracteres em todas as sentenças dividida pelo número de sentenças). '''
    tamanho_medio_sentenca = soma_caracteres_sentenca / qtde_sentencas
    #print("tamanho médio de sentença: ", tamanho_medio_sentenca)

    ''' Calcula a complexidade de sentença (número total de frases divido pelo número de sentenças). '''
    complexidade_sentenca = qtde_frases / qtde_sentencas

    ''' Calcula o tamanho médio de frase (soma do número de caracteres em cada frase dividida pelo número de frases no texto). '''
    tamanho_medio_frase = soma_caracteres_frase / qtde_frases

    fb = [tamanho_medio_palavra, relacao_type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca,
          tamanho_medio_frase]
    #print("fb = ", fb)
    return fb

def avalia_textos(textos, ass_cp):
    '''IMPLEMENTAR. Essa funcao recebe uma lista de textos e uma assinatura ass_cp e deve devolver o numero (1 a n) do texto com maior probabilidade de ter sido infectado por COH-PIAH.'''

    ''' Recebe a assinatura de cada texto (fb) e armazena em uma lista'''
    lista_assinaturas = []
    for i in range(len(textos)):
        lista_assinaturas.append(calcula_assinatura(textos[i]))
    #print("Lista de assinaturas:", lista_assinaturas)

    ''' Aplica a fórmula para comparar as assinaturas'''
    lista_resultado_comparacao = []
    for i in range(len(lista_assinaturas)):
        lista_resultado_comparacao.append(compara_assinatura(ass_cp, lista_assinaturas[i]))
    #print("lista resultado comparacao =", lista_resultado_comparacao)

    ''' Procura entre as comparações aquela que possui o menor valor (quanto mais similares os textos forem, menor será Sab)'''
    menor = lista_resultado_comparacao[0]
    indice_menor = 0
    for i in range(1, len(lista_resultado_comparacao)):
        if lista_resultado_comparacao[i] < menor:
            menor = lista_resultado_comparacao[i]
            indice_menor = i
    print(f"\nO autor do texto {indice_menor + 1} está infectado com COH-PIAH")
    return indice_menor + 1


# Recebe a assinatura do usuário
fa = le_assinatura()
#fa = [4.51, 0.693, 0.55, 70.82, 1.82, 38.5]
#print("fa:", fa)

''' Armazena os textos em uma lista. '''
lista_textos = le_textos()
#lista_textos = ['Obrigada. Volte sempre, meu querido!', 'O gato miava muito, sem parar. Parecia que ele estava cantando! Eu sempre gostri muito de gatos.']
#lista_textos = ['Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.']
#lista_textos = ['Num fabulário ainda por encontrar será um dia lida esta fábula: A uma bordadora dum país longínquo foi encomendado pela sua rainha que bordasse, sobre seda ou cetim, entre folhas, uma rosa branca. A bordadora, como era muito jovem, foi procurar por toda a parte aquela rosa branca perfeitíssima, em cuja semelhança bordasse a sua. Mas sucedia que umas rosas eram menos belas do que lhe convinha, e que outras não eram brancas como deviam ser. Gastou dias sobre dias, chorosas horas, buscando a rosa que imitasse com seda, e, como nos países longínquos nunca deixa de haver pena de morte, ela sabia bem que, pelas leis dos contos como este, não podiam deixar de a matar se ela não bordasse a rosa branca. Por fim, não tendo melhor remédio, bordou de memória a rosa que lhe haviam exigido. Depois de a bordar foi compará-la com as rosas brancas que existem realmente nas roseiras. Sucedeu que todas as rosas brancas se pareciam exactamente com a rosa que ela bordara, que cada uma delas era exactamente aquela. Ela levou o trabalho ao palácio e é de supor que casasse com o príncipe. No fabulário, onde vem, esta fábula não traz moralidade. Mesmo porque, na idade de ouro, as fábulas não tinham moralidade nenhuma.','Voltei-me para ela; Capitu tinha os olhos no chão. Ergueu-os logo, devagar, e ficamos a olhar um para o outro... Confissão de crianças, tu valias bem duas ou três páginas, mas quero ser poupado. Em verdade, não falamos nada; o muro falou por nós. Não nos movemos, as mãos é que se estenderam pouco a pouco, todas quatro, pegando-se, apertando-se, fundindo-se. Não marquei a hora exata daquele gesto. Devia tê-la marcado; sinto a falta de uma nota escrita naquela mesma noite, e que eu poria aqui com os erros de ortografia que trouxesse, mas não traria nenhum, tal era a diferença entre o estudante e o adolescente. Conhecia as regras do escrever, sem suspeitar as do amar; tinha orgias de latim e era virgem de mulheres.','Senão quando, estando eu ocupado em preparar e apurar a minha invenção, recebi em cheio um golpe de ar; adoeci logo, e não me tratei. Tinha o emplasto no cérebro; trazia comigo a idéia fixa dos doidos e dos fortes. Via-me, ao longe, ascender do chão das turbas, e remontar ao Céu, como uma águia imortal, e não é diante de tão excelso espetáculo que um homem pode sentir a dor que o punge. No outro dia estava pior; tratei-me enfim, mas incompletamente, sem método, nem cuidado, nem persistência; tal foi a origem do mal que me trouxe à eternidade. Sabem já que morri numa sexta-feira, dia aziago, e creio haver provado que foi a minha invenção que me matou. Há demonstrações menos lúcidas e não menos triunfantes. Não era impossível, entretanto, que eu chegasse a galgar o cimo de um século, e a figurar nas folhas públicas, entre macróbios. Tinha saúde e robustez. Suponha-se que, em vez de estar lançando os alicerces de uma invenção farmacêutica, tratava de coligir os elementos de uma instituição política, ou de uma reforma religiosa. Vinha a corrente de ar, que vence em eficácia o cálculo humano, e lá se ia tudo. Assim corre a sorte dos homens.']
#print("lista de textos:", lista_textos)

avalia_textos(lista_textos, fa)