def inverter_vetor(vetor): #Função auxiliar para a função dez_para_binario.
    vfinal = []
    saida = ""
    i = len(vetor)-1
    while i>=0:
        vfinal.append(vetor[i])
        i = i - 1
    for a in range(len(vfinal)):
        saida += str(vfinal[a])
    return saida

def dez_para_binario(numero):#Função para converter decimal para binario (só usada no expoente).
    num = int(numero)
    inverso = []
    binario = ""
    while num >= 2:
        inverso.append(num%2)
        num = int(num/2)
    inverso.append(num)
    binario = inverter_vetor(inverso)
    return binario
    
    
def casos_especiais(entrada): #Imprime no formato IEEE754 e Retorna True se for um caso especial.
    if entrada=='0' or entrada=='+0':
        print('SINAL: 0 EXPOENTE: 00000000 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='-0':
        print('SINAL: 1 EXPOENTE: 00000000 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='+inf':
        print('SINAL: 0 EXPOENTE: 11111111 MANTISSA: 00000000000000000000000')
        return True
    elif entrada=='-inf':
        print('SINAL: 1 EXPOENTE: 11111111 MANTISSA: 00000000000000000000000')
        return True
    #elif 1 not in separado[0]:
    #    print('SINAL:0 ou 1  EXPOENTE: 00000000 MANTISSA: 00000000000000000000000 ')
    else:
        return False

def remove_sinal(entrada):#Remove o sinal Negativo da entrada se a mesma possui-lo.
    if entrada[0]=='-':
        return entrada[0+1:]
    else:
        return entrada

def bit_sinal(entrada):#Verifica sinal E retorna o bit resultante:
    if entrada[0]=='-':
        return 1
    else:
        return 0

def expoente(entrada):  #Função calcula o expoente e pode retornar tanto o numero de casas , quanto o expoente com excesso em binário. Prints temporarios.
    exp=entrada.split(',')#separa a entrada em dois vetores , o [0] é a esquerda da vírgula e o [1] á direita.
    primeiro=0 #Variavel para guardar o indice do primeiro '1' á esquerda da vírgula.
    casas=0    #Variavel das casas que andou e , consequentemente o expoente (sem o excesso de 127)
    #print(exp)
    if '1' in exp[0]:
        for i in range(len(exp[0])):
            if exp[0][i]!='0':#Se encontrar '1' ANTES da vírgula , vai andar até o primeiro '1' para a ESQUERDA.
                primeiro=i
                for j in range(primeiro+1,len(exp[0])): #Percorre até alcançar o primeiro '1' e conta quantas casas andou para a esquerda (expoente positivo).
                    casas+=1
                decimal=casas+127 #Expoente em decimal (COM excesso de 127)
                #print('Andou',casas,'casas para esquerda')
                #print(decimal)
                #print(dez_para_binario(int(decimal)))
                break
        return(dez_para_binario(int(decimal)))
    else:
        for j in range(len(exp[1])):#Se encontrar '1' DEPOIS da vírgula , vai andar até o primeiro '1' para a DIREITA.
            if exp[1][j]!='0':
                primeiro=j
                break
        casas=primeiro+1   #Numero de casas que andou para direita.
        decimal=-casas+127 #Expoente NEGATIVO em decimal (COM excesso de 127)
        #print('Andou',casas,'casas para direita')
        #print(decimal)
        #print(dez_para_binario(int(decimal)))
        return(dez_para_binario(int(decimal)))
def mantissa(entrada):#Função que retorna a Mantissa no formato Precisão simples (23 bits)
    manti_final=23*['0'] #Mantissa Final
    separado=entrada.split(',')
    primeiro=0
    tamanho=len(separado[0])
    if '1' in separado[0]:#Se a virgula anda para a Esquerda:
        for i in range(len(separado[0])):
            if separado[0][i]!='0':#Se encontrar '1' ANTES da vírgula , vai andar até o primeiro '1' para a ESQUERDA.
                primeiro=i
                break
        #print(len(separado))
        if len(separado)==2:#Se a entrada for no formato 1010,1010 por exemplo. Separado por vírgula
            if separado[0][0]=='0':   #Se O primeiro elemento da string do lado esquerdo da virgula for 0:
                manti=separado[0][primeiro:]+separado[1] #Atribui a 'Manti' , a string a partir do primeiro '1' até o final + o restante da string (Mantissa completa)
            else: #Se o primeiro elemento da string do lado esquerdo da virgula for 1 , ele não entra na mantissa:
                manti=separado[0][primeiro+1:]+separado[1]#Atribui a 'Manti' a string a partir do elemento depois do '1' (ou seja , só os que estão do lado direito daq vírgula)
        else:
            manti=separado[0][primeiro+1:]
        for i in range(len(manti)):
            manti_final[i]=manti[i]
        #print(manti_final)
        return ''.join(manti_final)
    else:#Se a vírgula anda para direita:
        for i in range(len(separado[1])):#Se encontrar '1' DEPOIS da vírgula , vai andar até o primeiro '1' para a DIREITA.
            if separado[1][i]!='0':
                primeiro=i
                break
        manti=separado[1][primeiro+1:]
        for i in range(len(manti)):
            manti_final[i]=manti[i]
        #print(''.join(manti_final))
        return ''.join(manti_final)


#Inicio do Programa:
entrada=input("Insira o Número na base 2 separado por vírgula:")#Entrada
if casos_especiais(entrada)== False:#Verifica se é um caso especial:
    print('SINAL:',bit_sinal(entrada),'EXPOENTE:',expoente(remove_sinal(entrada)),'MANTISSA:',mantissa(remove_sinal(entrada)))
