#Função Que calcula o expoente tanto NEGATIVO quanto POSTIVO , e também aceita valores sem vírgula para calcular o expoente! 
#Ou seja , a função está funcionando corretamente com todos os valores possíveis de entrada.
#Os prints são temporários , a intenção é printar apenas o Expoente em binário já para representação ou retornar o mesmo.

#-------Inicio---------

def expoente(entrada):  #Função calcula o expoente e pode retornar tanto o numero de casas , quanto o expoente com excesso em binário.
    exp=entrada.split(',')#separa a entrada em dois vetores , o [0] é a esquerda da vírgula e o [1] á direita.
    primeiro=0 #Variavel para guardar o indice do primeiro '1' á esquerda da vírgula.
    casas=0    #Variavel das casas que andou e , consequentemente o expoente (sem o excesso de 127)
    if '1'in exp[0]:
        for i in range(len(exp[0])):
            if exp[0][i]!='0':#Se encontrar '1' ANTES da vírgula , vai andar até o primeiro '1' para a ESQUERDA.
                primeiro=i
                for j in range(primeiro+1,len(exp[0])): #Percorre até alcançar o primeiro '1' e conta quantas casas andou para a esquerda (expoente positivo).
                    casas+=1
                decimal=casas+127 #Expoente em decimal (COM excesso de 127)
                print('Andou',casas,'casas para esquerda')
                print(decimal)
                print(dec_to_bin(decimal))
                break
    else:
        for j in range(len(exp[1])):#Se encontrar '1' DEPOIS da vírgula , vai andar até o primeiro '1' para a DIREITA.
            if exp[1][j]!='0':
                primeiro=j
                break
        casas=primeiro+1   #Numero de casas que andou para direita.
        decimal=-casas+127 #Expoente NEGATIVO em decimal (COM excesso de 127)
        print('Andou',casas,'casas para direita')
        print(decimal)
        print(dec_to_bin(decimal))
