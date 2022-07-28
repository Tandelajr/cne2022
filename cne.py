######################################################################################################
# Titulo: Sistema de Votação CNE 2022                                                                #
# Author: Abilio Tandela                                                                             #
# Website : https://abiliotandela.me                                                                 #
######################################################################################################


from rich import print
import os
import sys
import time


print ("""[on blue3] 

 .o88b. d8b   db d88888b      .d888b.  .d88b.  .d888b. .d888b. 
d8P  Y8 888o  88 88'          VP  `8D .8P  88. VP  `8D VP  `8D 
8P      88V8o 88 88ooooo         odD' 88  d'88    odD'    odD' 
8b      88 V8o88 88~~~~~       .88'   88 d' 88  .88'    .88'   
Y8b  d8 88  V888 88.          j88.    `88  d8' j88.    j88.    
 `Y88P' VP   V8P Y88888P      888888D  `Y88P'  888888D 888888D
[/]""")

z = """ 
        [+]████████████████████████████████████████████████████████████████████[+]



"""




for c in z:
    sys.stdout.write(c)
    sys.stdout.flush()
    time.sleep(0.02)




#Partidos

VOTOS_PHA = 0
VOTOS_PJANGO = 0
VOTOS_UNITA = 0
VOTOS_FNLA = 0
VOTOS_CASACE = 0
VOTOS_APN = 0
VOTOS_PRS = 0
VOTOS_MPLA = 0


while True:
    print('#' * 50)
    print(f'[on gray]Total PHA:[/]{VOTOS_PHA}{os.linesep}[on blue3]Total PJANGO:[/]{VOTOS_PJANGO}{os.linesep}[on green4]Total UNITA:[/]{VOTOS_UNITA}{os.linesep}[on white]Total FNLA:[/]{VOTOS_FNLA}{os.linesep}[on yellow]Total CASACE:[/]{VOTOS_CASACE}{os.linesep}[on purple]Total APN:{VOTOS_APN}{os.linesep}[on black]Total PRS:[/]{VOTOS_PRS}{os.linesep}[on red]Total MPLA:[/]{VOTOS_MPLA}')
    print('#' * 50)

    voto = int(input(f'BOLETIM DE VOTOS:{os.linesep}1 - PHA{os.linesep}2 - PJANGO{os.linesep}3 - UNITA{os.linesep}4 - FNLA{os.linesep}5 - CASACE{os.linesep}6 - APN{os.linesep}7 - PRS{os.linesep}8 - MPLA{os.linesep} Votação: '))
    


    os.system('clear')