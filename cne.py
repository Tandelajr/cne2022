######################################################################################################
# Titulo: Sistema de Votação CNE 2022                                                                #
# Author: Abilio Tandela                                                                             #
# Website : https://abiliotandela.me                                                                 #
######################################################################################################


from rich import print
import os
import sys
import ctypes

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
    print('#' * 100)
    print(f'[on gray]Total PHA:[/]{VOTOS_PHA}{os.linesep}[on blue3]Total PJANGO:[/]{VOTOS_PJANGO}{os.linesep}[on green4]Total UNITA:[/]{VOTOS_UNITA}{os.linesep}[on white]Total FNLA:[/]{VOTOS_FNLA}{os.linesep}[on yellow]Total CASACE:[/]{VOTOS_CASACE}{os.linesep}[on purple]Total APN:{VOTOS_APN}{os.linesep}[on black]Total PRS:[/]{VOTOS_PRS}{os.linesep}[on red]Total MPLA:[/]{VOTOS_MPLA}')
    print('#' * 100)

    voto = int(input(f'Vota em:?{os.linesep}1 - PHA{os.linesep}2 - PJANGO{os.linesep}3 - UNITA{os.linesep}4 - FNLA{os.linesep}5 - CASACE{os.linesep}6 - APN{os.linesep}7 - PRS{os.linesep}8 - MPLA{os.linesep} Seu voto:Quem gostaria de votar: '))




os.system('cls' if os.name == 'nt' else 'clear')

