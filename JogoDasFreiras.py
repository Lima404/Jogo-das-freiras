nome = input("Eae jogador, qual seu nome? ")

print (nome ,'É o seguinte preciso da sua ajuda para resolver um problema!!! ')

print ('''Três freiras e três índios canibais precisam ir de uma fazenda localizada na zona rural da cidade da Caixa prego até o centro da cidade. Porém, no meio do caminho, surgiu um problema, há um rio cuja travessia precisa ser realizada de canoa e na canoa só há espaço para duas pessoas em cada viagem.

Os índios costumam ser obedientes e seguir as ordens das freiras. Porém, se perceberem que estão em vantagem numérica (existam mais índios do que freiras em um local), poderão atacar!

Portanto, o desafio é encontrar uma estratégia que permita transportar freiras e canibais até a outra margem do rio, impedindo que os índios canibais fiquem em maior número do que as freiras em qualquer das margens, o que representaria um risco para as freiras.

Encontre uma solução para transportar freiras e canibais de uma margem do rio para a outra, garantindo a segurança do grupo.''')



lista_direita = ["c1","c2","c3","f1","f2","f3"]
lista_esquerda = []
barco = [] 

  ### LADO DIREITO

  ### conferenci do lado direito ###

c1d = lista_direita.count("c1")
c2d = lista_direita.count("c2")
c3d = lista_direita.count("c3")
totalcd = c1d + c2d + c3d

  #print("total de canibais do lado direito",totalcd)

f1d = lista_direita.count("f1")
f2d = lista_direita.count("f2")
f3d = lista_direita.count("f3")
totalfd = f1d + f2d + f3d
  
  #print ("total de freiras do lado direito",totalfd)


  ### LADO ESQUERDO ####

c1e = lista_esquerda.count("c1")
c2e = lista_esquerda.count("c2")
c3e = lista_esquerda.count("c3")
totalce = c1e + c2e + c3e

f1e = lista_esquerda.count("f1")
f2e = lista_esquerda.count("f2")
f3e = lista_esquerda.count("f3")
totalfe = f1d + f2d + f3d
njdpe = 1
njepd = 0
while (totalcd >= 1) or (totalfd >= 1) and (totalce != 3) or (totalfe != 3) :
 njdpe= njdpe+1
 

 lista_concerto= barco + lista_direita
 lista_direita = lista_concerto
 barco.clear()
 print("lado direito do rio ", lista_direita)
 print("--" * 30)
 print(" ~" * 29)
 print("~ " * 29)
 print("--" * 30)
 print("lado esquerdo do rio ", lista_esquerda)

  ############## tripulantes LADO DIREITO #########
  
 trip1 = input( "Ok,estamos do lado direito, vamos lá, adicione 1 personagem de cada vez no barco. \nQuem será o primeiro?  ")
 lista_direita.remove(trip1)
 barco.append(trip1)
 print(barco)
 trip2 = (input("quem será o proximo? "))
 barco.append(trip2)
 lista_direita.remove(trip2)
  
  #######verificação lado direito
  ### conferenci do lado direito ###
  
 c1d = lista_direita.count("c1")
 c2d = lista_direita.count("c2")
 c3d = lista_direita.count("c3")
 totalcd = c1d + c2d + c3d
  
  #print("total de canibais do lado direito",totalcd)
  
 f1d = lista_direita.count("f1")
 f2d = lista_direita.count("f2")
 f3d = lista_direita.count("f3")
 totalfd = f1d + f2d + f3d
  
  #print ("total de freiras do lado direito",totalfd)
  
 if totalcd > totalfd and totalfd != 0: 
   totalcd = 0
   totalfd = 0
   erro1 = "\n\n\n\nvocê perdeu pois deixou os canibais em maior quantidade no lado direito\n\n\n\n"
   print(erro1)
   print("\nreinicie o programa e tente novamente\n")  

### vitoria
   
 elif totalcd == 0 and totalfd == 0 :
   lista_concerto = barco + lista_esquerda
   lista_esquerda = lista_concerto
   print()
   print("lado direito do rio ", lista_direita)
   print("--" * 30)
   print(" ~" * 29)
   print("~ " * 29)
   print("--" * 30)
   print("lado esquerdo do rio ", lista_esquerda)
   
   
   print("\nvocê venceu\n")
    
   ########## print rio 
   
 else:    
   print("lado direito do rio ", lista_direita)
   print("--" * 30)
   print(" ~" * 11, barco, " ~" * 11)
   print("~ " * 29)
   print("--" * 30)
   print("lado esquerdo do rio ", lista_esquerda)
 
   print ()
   print ()
   print("\nVamos atravessar!\n")
   print("lado direito do rio ", lista_direita)
   print("--" * 30)
   print(" ~" * 29)
   print("~ " * 11, barco, " ~" * 11)
   print("--" * 30)
   print("lado esquerdo do rio ", lista_esquerda)


   ######### tripulantes LADO DIREITO #####
  
   print () 
   print ()
   print("chegamos no lado esquerdo do rio e estamos da seguinte maneira ")
   lista_de_concerto = lista_esquerda + barco
   lista_esquerda = lista_de_concerto
   print("lado direito do rio ", lista_direita)
   print("--" * 30)
   print(" ~" * 29)
   print("~ " * 29)
   print("--" * 30)
   print("lado esquerdo do rio ", lista_esquerda)
   barco.clear()
 
  #### VOLTA ####

   quantos_voltam = int(input("quantos irão voltar para pegar o restante? responda com 1 ou 2 \n"))
   if quantos_voltam == 1:
      trip1 = input("lembresse que o barco vai da esquerda para direita do rio \nQuem volta para pegar os outros ? " )
      lista_esquerda.remove(trip1)
      barco.append(trip1) 
      njepd= njepd + 1 
            
      
   else:
      trip1 = input("Lembresse que estamos do lado esquerdo do rio \nQuem será o primeiro tripulante? ")
      lista_esquerda.remove(trip1)
      barco.append(trip1)
      trip2 = input("E quem será o segundo ? ")
      lista_esquerda.remove(trip2)
      barco.append(trip2)
      print ()
      njepd= njepd + 1 
  
     ### LADO ESQUERDO ####
     
      c1e = lista_esquerda.count("c1")
      c2e = lista_esquerda.count("c2")
      c3e = lista_esquerda.count("c3")
      totalce = c1e + c2e + c3e
    
      f1e = lista_esquerda.count("f1")
      f2e = lista_esquerda.count("f2")
      f3e = lista_esquerda.count("f3")
      totalfe = f1e + f2e + f3e
     
     
      if totalce > totalfe and totalfe != 0: 
       totalcd = 0
       totalfd = 0
       erro2 = "você perdeu pois deixou os canibais em maioria quantidade no lado esquerdo"
       print(erro2)
       print("\nreinicie o programa e tente novamente\n")

print("fim de jogo\n")
print("você precisou ir da direita para a esquerda {}".format(njdpe))
print("você precisou ir da esquerda para a direita {}".format(njepd))
total_de_jogadas=njepd+njdpe
print("você jogou {} vezes".format(total_de_jogadas))