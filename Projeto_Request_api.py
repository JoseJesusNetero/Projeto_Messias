# import de biblioteca necessaria
import os
import requests

######################################################
#Corpo das funcoes a serem utilizadas 

os.system( 'cls' if os.name == 'nt' else 'clear' )

##################

def solicitacao_de_conselhos( qtde) :
    
    
    contar = 0
    ####
    while( contar < qtde ) :
    
        traco = '  ----------------------------  '
        ####
        pedido_url = "https://api.adviceslip.com/advice"
        
        resposta = requests.get( pedido_url)
        
        id = resposta.json()['slip']
        
        
        print( '\n     ' + id['advice'] + traco + 'Id do Conselho ' + str(id['id']) + '\n' )
        
        contar += 1
        
        dicio[ str( id [ 'id'] ) ] =  id['advice']
        
        #######
        
        print("\n--- Voce quer guardar este conselho ? --- \n")

        s = input()

        if ( s.upper()  == 'SIM' ) :
    
            arq.close()
            guardar_conselho(  dicio.popitem() )
            
        else : 
            
            continue
            ###############
    
    
###################################################
def guardar_conselho( tupla ) :
    
    
    arq = open( "teste_1.txt" , 'a')
    
    arq.write( tupla[0] + ' ' + '--- ' + tupla[1]  +  '\n' )
    
########

########################################
def resgatar_conselho( id ) :
    
    
    arq = open( "teste_1.txt" , 'r')
    ####
    
    leitura = arq.readline()
    #######
    i = leitura.index(' ')
    ####
    
    while(  (leitura[ : i]  !=  id)  and  ( leitura ) )  :
        
        i = leitura.index(' ') 
        leitura = arq.readline()
        
    ####
    print(f"O conselho requerido e : { leitura[ i : ] } \n")
    print( "                     ----------------- Este e um bom conselho :) -------------")
    
###########


######################################
#Inicio do programa em si
    
print( "----- Bom dia ! Seja bem vindo à Cachaçaria do Seu Zé ! ! -------- \n") 
print( "----- Depois de uma boa nada melhor do querer buscar orientação na vida não é mesmo -----!? :) :)\n")
print( "----- Diga quantos conselhos deseja -------\n ")

conselhos = int(input())

dicio = dict()  # Para armazenar os conselhos com seu id
####################

arq = open("teste_1.txt" , 'w') #arquivo a ser usado

####################

solicitacao_de_conselhos( conselhos )

###################

print("---- Voce deseja resgatar algum conselho ------ ?\n")

s = input('\n')

if ( s.upper() == 'SIM' ) :
    
    arq.close()
    ##
    
    print("\nDigite o id \n" )
    id = input()
    
    resgatar_conselho( str(id) )
    
#####################################




