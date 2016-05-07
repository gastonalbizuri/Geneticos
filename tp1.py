#bloque definicion de ctes

coef = pow(2,30)-1
pCross = 0.75
pMut = 0.05

#bloque importacion de modulos

import random
import matplotlib.pyplot as plt 


#bloque definicion funciones

def funcionObj(x):
    return pow((x/float (coef)),2)

def funcionFitness(crom, tot):
    fitness = crom/float (tot)
    return fitness

def cargaRuleta(fit):
    return (fit*100)

def crossover(cromosoma1,cromosoma2,punto):
    hijo = cromosoma1[:punto] + cromosoma2[punto:]

    return hijo
    
    

#programa principal

cromosomaList = []
cromBinList = []
cromObj = []
listMax = []
listMin = []
listProm = []

for i in xrange(10):
    cromosoma = random.randint(0,coef) #genero random de 0 a coef
    cromosomaList.append(cromosoma)
    cromosomaBin = bin(cromosoma)[2:].zfill(30) #convierto el int en binario
    cromBinList.append(cromosomaBin)

    cromObj.append(funcionObj(cromosoma)) #aplico funcion obj al cromosoma

    
for i in xrange(2000):
    
    fitnessCrom = []
    ruleta = []
    ruletaList = []
    nuevaPoblacionBin = []
    nuevaPoblacionInt = []
    
    suma = sum(cromObj)

    for i in cromObj:
        fitness = funcionFitness(i,suma)
        fitnessCrom.append(fitness) #genero lista con los fitness de cada cromosoma

    
      
     
    for i in xrange(5): #tiro la ruleta 5 veces, por pares
        sumFitness = 0
        tirada1 = random.random()
        
        for n in xrange(10):
            if((tirada1 > sumFitness) & (tirada1 < (sumFitness + fitnessCrom[n]))):
                elegido1 = n
                break
            else:
                sumFitness = sumFitness + fitnessCrom[n]
        
        sumFitness = 0
        tirada2 = random.random()
        
        for n in xrange(10):
            if((tirada2 > sumFitness) & (tirada2 < (sumFitness + fitnessCrom[n]))):
                elegido2 = n
                break
            else:
                sumFitness = sumFitness + fitnessCrom[n]   

        crom1 = cromBinList[elegido1]    #le asigno el indice que fue seleccionado al azar, el cual hace corresponder su cromosoma
        crom2 = cromBinList[elegido2]

        
        crossRandom = random.random()  #genero un nro random para el cross [0,1]

        if crossRandom <= pCross:        #aplico crossover
            puntoCorte = random.randint(0,29)

            hijo1 = crossover(crom1,crom2,puntoCorte)
            hijo2 = crossover(crom2,crom1,puntoCorte)
        else:
            hijo1 = crom1
            hijo2 = crom2
            
        mutacion1 = random.random()
        mutacion2 = random.random()
        
        if mutacion1 < pMut: #si es menor la prob

            posGen = random.randint(0,29)

            if (hijo1[posGen] == '0'):
                hijo1 = hijo1[:posGen] + '1' + hijo1[posGen+1:]
            else:
                hijo1 = hijo1[:posGen] + '0' + hijo1[posGen+1:]

        if mutacion2 < pMut: #si es menor la prob

            posGen = random.randint(0,29)

            if (hijo2[posGen] == '0'):
                hijo2 = hijo2[:posGen] + '1' + hijo2[posGen+1:]
            else:
                hijo2 = hijo2[:posGen] + '0' + hijo2[posGen+1:]

        nuevaPoblacionBin.append(hijo1) #agrego hijos a la nueva poblacion
        nuevaPoblacionBin.append(hijo2)
    
    for x in xrange(10):    #convierto los binarios en entero
        entero = nuevaPoblacionBin[x]
        nuevaPoblacionInt.append(int(entero, base=2))

    cromosomaList = list(nuevaPoblacionInt)
    cromBinList = list(nuevaPoblacionBin)

    
    maximo = max(cromObj)
    minimo = min(cromObj)
    promedio = sum(cromObj)/len(cromObj)

    cromObj = [] #reincializo la lista con cromosomas objetivo
    
    for j in cromosomaList:
        cromObj.append(funcionObj(j)) #aplico funcion obj al cromosoma

    listMax.append(maximo)
    listMin.append(minimo)
    listProm.append(promedio)



    
plt.plot(listMax)
plt.plot(listMin)
plt.plot(listProm)
plt.ylabel('Evolucion')
plt.show()

