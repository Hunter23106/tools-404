import os
import time
import sys
import time

from datetime import datetime

now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

#collors
Azul = '\033[94m'
Verde = '\033[92m'
Amarelo = '\033[93m'
Vermelho = '\033[91m'
Fim = '\033[0m'

os.system("clear")
print ("INICIANDO SISTEMA")
time.sleep(0.5)
print ("CARREGANDO SISYEMA")
os.system("cd toll-croacia")
time.sleep(1)
os.system("clear")
print ("TUDO PRONTO CARREGANDO A FERRAMENTA")
os.system("clear")

print ('''                 \033[94m.@@:       !@@@@:       .@@@
     !@@:     .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.     :@@!
   .@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@#
  @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
  .#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@.
    :@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
     !@@@@@@@@@@@@@@:                    .@@@@@@@@@@@@@@!
       @@#:                                         #@@\033[0m
       \033[91m#.        ##@@@#@@@.        .@@@@@@#@@         !
       #.        ###@@@@@#.        .##@@@@@@#         !
       #.        ##@@@@@##.        .@@@@@###@         !
       #.        #@@@@@@@#.        .#@@@@@@@@         !
       #@#@@@#@@@         !@@@@@@@@!         @@@#@@@@@@
       ##@@@@@@@@         !@#@@@@@@!         @@@@@@#@@@
       ##@@@@@##@         !@##@#@@@!         @@@@@@@@@@
       #.        !@@@#@#@@.        .@#@@@@#@@         !
       #.        !@@@@@#@@.        .@@@@@@@@#         !
       #.        !@#@#@@@@.        .@@@@@@@@#         !
       :.        :########.        .#########         !
       :@#@@@@@#@         !@@@@@#@#!         ###@@@###.
        :#@#@@#@@         !@@@@@##@!         @@@@@@@@!
         .#@@@#@@         !@@@##@@@!         ##@@@@#
            !.   !@@@#@@@@.        .@@@@@#@@#   .#.
              .# !@@@@@@@#.        .#@@@@#@##.#.
                  :#@@@#@@.        .#@@@@@@!
                         .:\033[0m ''')

print ("\033[92mBem Vindo\033[0m")

opcao = int(input(" SUA ESCOLHA E : "))

if opcao == 1:
    os.system("git clone https://github.com/Tuhinshubhra/RED_HANK")
elif opcao == 2:
    os.system("git clone --depth 1 https://github.com/sqlmappro")
elif opcao == 3:
    os.system("apt install php")
if opcao == 4:
   os.system("apt install python")
elif opcao == 5:
   os.system("git clone https://github.com/b3-v3r/Hunner")
elif opcao == 6:
   os.system("git clone http://github.com/Screetsec/Brutal")
if opcao == 7:
   os.system("apt install python2")
elif opcao == 8:
   os.systsm("apt install python3")
