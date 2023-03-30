import random

def gene_cb():
    '''Gera um gene válido para o problema das caixas binárias.
    
    Return:
        Um valor zero ou um.
    '''
    #lista = [0, 1]
    #gene = random.choice(lista)
    #return gene
    
    return random.choice([0, 1])


def individuo_cb(n):
    '''Gera um individuo para o problema das caixas binárias.
    
    Args:
        n: número de genes do indivíduo.
    
    Return:
        Uma lista com n genes. Cada gene é um valor zero ou um.
    '''
    #individuo = []
    #for i in range(n):
    #    gene = gene_cb()
    #    individuo.append(gene)
    #return gene

    return [gene_cb() for i in range(n)]


def populacao_cb(tamanho, n):
    '''Cria uma população no problema das caixas binárias.
    
    Args:
        tamanho: tamanho da população;
        n: número de genes de um individuo.
    
    Returns:
        Uma lista onde cada item é um individuo. Um individuo é uma lista com n genes.
    '''
    populacao = []
    for _ in range(tamanho):
        populacao.append(individuo_cb(n))
    return populacao


def selecao_roleta_max(populacao, fitness):
    '''Seleciona individuos de uma população usando o método da roleta.
    
    Nota: apenas funciona para problemas de maximização.
    
    Args:
        populacao: lista com todos os individuos da população;
        fitness: lista com o valor da função objetivo dos individuos da população.
    
    Returns:
        População dos individuos selecionados.
    '''
    populacao_selecionada = random.choices(populacao, weights=fitness, k=len(populacao))
    return populacao_selecionada


def cruzamento_ponto_simples(pai, mae):
    ''' Operador de cruzamento de ponto simples.
    
    Args:
        Pai: uma lista representando um individuo.
        Mãe: uma lista representando um individuo.
    Returns:
        Duas listas, sendo que cada uma representa um filho dos pais que foram os argumentos
    '''
    ponto_de_corte= random.randint(1, len(pai) - 1)
    
    filho1 = pai[:ponto_de_corte] + mae[ponto_de_corte:]
    filho2 = mae[:ponto_de_corte] + pai[ponto_de_corte:]
    
    return filho1, filho2


def mutacao_cb(individuo):
    ''' Realiza a mutação em um gene no problema das caixas binárias.
    
    Args:
        individuo: uma lista representado um individuo no problema das caixas binárias.
        
    Return:
        Um individuo com um gene mutado.
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo) - 1)
    individuo[gene_a_ser_mutado] = gene_cb()
    
    return individuo


def funcao_objetivo_cb(individuo):
    '''Computa a função objetivo no problema das caixas binárias.
    
    Args:
        individuo: lista contendo os genes das caixas binárias.
    
    Return:
        Um valor representando a soma dos genes do individuo.
    '''
    return sum(individuo) + 1


def funcao_objetivo_pop_cb(populacao):
    '''Calcula a função objetivo para todos os membros de uma população.
    
    Args:
        populacao: lista com todos os individuos da população.
    
    Returns:
        Lista de valores representando a fitness de cada individuo da população.
    '''
    fitness = []
    for individuo in populacao:
        fobj = funcao_objetivo_cb(individuo)
        fitness.append(fobj)
    
    return fitness
    
def populacao_cnb(tamanho_da_populacao, numero_genes, valor_max_caixa):
    '''Cria uma populacao de individuos para o problema das caixas nao binarias
    Args:
        tamanho_da_populacao: numero de individuos da populacao
        numero_genes: numero de genes do individuo
        valor_max_caixa: valor maximo que cada caixa pode assumir
    Returns:
        Uma lista onde cada item representa um individuo
    
    '''
    populacao = []
    for _ in range(tamanho_da_populacao):
        individuo = individuo_cnb(numero_genes,valor_max_caixa)
        populacao.append(individuo)
    return populacao

def funcao_objetivo_cnb(individuo):
    '''Calcula o fitness do individuo para o problema das caixas nao binarias
    Args:
        individuo: lista que representa um individuo dentro do problema das caixas nao binarias
    Retuns:
        Um valor que representa o fitness do individuo
    '''
    fitness = sum(individuo)
    return fitness

def funcao_objetivo_pop_cnb(populacao):
    '''Calcula o fitness da populacao completa
    Args:
        populacao: lista com todos os individuos da populacao
    Returns:
        Uma lista com o fitness de cada individuo em ordem
    '''
    fitness_pop = []
    for individuo in populacao:
        fitness_ind = funcao_objetivo_cnb(individuo)
        fitness_pop.append(fitness_ind)
    return fitness_pop
    
def mutacao_cnb(individuo, valor_max_caixa):
    '''Realiza a mutacao do indivduo
    Args:
        individuo: individuo que deve sofrer mutacao
        valor_max_caixa: valor maximo que a caixa pode assumir
    Returns:
        Individuo que sofreu mutacao
    '''
    gene_a_ser_mutado = random.randint(0, len(individuo)-1)
    individuo[gene_a_ser_mutado] = gene_cnb(valor_max_caixa)
    return individuo
    
    
def gene_cnb(valor_max_caixa):
    '''Gera um gene valido para problema cnb
    Args:
        valor_max_caixa: n int repreesetnando maior numero possivel
    Returns:
        Um valor entre zero a valor max
    '''
    gene = random.randint(0,valor_max_caixa)
    return gene

def individuo_cnb(n_genes, valor_max_caixa):
    """Gera um individuo para o problema das caixas não-binárias.
    Args:
      n_genes: número de genes do indivíduo.
      valor_max_caixa: maior número inteiro possível dentro de uma caixa
    Return:
       Uma lista com n genes. Cada gene é um valor entre zero e
       `valor_max_caixa`.
    """
    individuo = []
    for i in range(n_genes):
        gene = gene_cnb(valor_max_caixa)
        individuo.append(gene)
    return individuo

def mutacao_senha (individuo, letras):
    """Realiza a mutação de genes no problema das senhas
    Args:
        individuo: uma lista representando um individuo no problema das senhas
        letras: caracteres possiveis de serem sorteados
    Return:
        Um individuo (senha) com gene mutado
    """
    gene = random.randint(0, len(individuo)-1)
    individuo[gene] = gene_letra(letras)
    return individuo


def funcao_objetivo_pop_senha(populacao, senha_verdadeira):
    """Computa a funcao objetivo de uma populaçao no problema da senha.
    Args:
      populacao: lista com todos os individuos da população
      senha_verdadeira: a senha que você está tentando descobrir
    Returns:
      Lista contendo os valores da métrica de distância entre senhas.
    """
    resultado = []

    for individuo in populacao:
        resultado.append(funcao_objetivo_senha(individuo, senha_verdadeira))

    return resultado




#funcoes que eu estava testando e nao deram certo

#def funcao_objetivo_pop_senha(populacao, senha):
#    '''Calcula a função objetivo para todos os membros de uma população.
    
#    Args:
#        populacao: lista com todos os individuos da população.
#        senha: string representando a senha que se quer descobrir.
#    
#    Returns:
#        Lista de valores representando a fitness de cada individuo da população.
#    '''
#    fitness = []
#    for individuo in populacao:
#        acertos = sum(1 for i in range(len(senha)) if individuo[i] == senha[i])
#        fitness.append(acertos)
#    return fitness


def gene_letra(letras):
    """Função auxiliar que sorteia uma letra do alfabeto.
    Args:
        letras: caracteres possiveis de serem sorteados
    Return:
        Um caractere escolhido aleatoriamente entre as letras passadas.
    """
    return random.choice(letras)

def selecao_torneio_min(populacao, fitness, num_comb):
    """Seleciona o indivíduo com menor fitness em um torneio.
    Args:
        populacao: lista com todos os individuos da população
        fitness: valor do individuo
        num_comb: número de combatentes do torneio
    Return:
        O individuo vencedor do problema
    """
    combatentes = random.sample(populacao, num_comb)
    fitness_comb = [fitness[populacao.index(c)] for c in combatentes]
    vencedor = combatentes[fitness_comb.index(min(fitness_comb))]
    return vencedor





def populacao_inicial_senha(tam_pop, letras, num_genes):
    """Gera uma população inicial para o problema da senha."""
    populacao = []
    for i in range(tam_pop):
        individuo = [gene_letra(letras) for _ in range(num_genes)]
        populacao.append(individuo)
    return populacao


