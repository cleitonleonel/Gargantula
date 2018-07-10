from pyfiglet import Figlet
from data.icons_lib import *
from data.utils import *
from data.char import *
from data.item_lib import *
import time
import random
import colorama
import os

#Fore: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Back: BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
#Style: DIM, NORMAL, BRIGHT, RESET_ALL

def game_start():
    loading(main_menu)

def loading(next_menu):
    dicas = [
            "Não monte num burrico bêbado!",
            "Cuidado ao apertar a mão de um goblin, ele pode ter \ncutucado o nariz segundos antes!",
            "Nunca pegue numa espada pela lâmina!",
            "Nunca aponte a ponta de um cajado contra o próprio rosto!",
            "Se você receber itens demais, desconfie, o boss está próximo!",
            icons["hal"]+" I'M SORRY DAVE. I'M AFRAID I CAN'T LET YOU DO THAT.",
            ]
    dica = random.randint(0, len(dicas)-1)
    for i in range(101):
        print("\n" * 100)
        print(icons["warn"]+"  DICA DO DIA:")
        print(dicas[dica])
        print("")
        print("CARREGANDO")
        print(str(i)+"%",colorama.Back.GREEN+colorama.Style.BRIGHT+" "*int((i/100.0)*73)+colorama.Style.RESET_ALL)
        time.sleep(1/random.randint(10,40))
    if next_menu == main_menu:
        main_menu()
    else:
        pass

def main_menu():
    verdade = True
    erro = ""
    while verdade:
        banner = Figlet(font='ogre')
        print("\n" * 100)
        print(colorama.Fore.GREEN+colorama.Style.BRIGHT+ banner.renderText('   Gargantula') + colorama.Style.RESET_ALL)
        print("   RPG baseado em texto - Thiago Monteiro 2018")
        print("")
        print("")
        print("  ", icons["play"]," (1)"+colorama.Fore.YELLOW +" NOVO JOGO" + colorama.Style.RESET_ALL)
        print("")
        print("  ", icons["load"],"(2)"+colorama.Fore.YELLOW +" CARREGAR" + colorama.Style.RESET_ALL)
        print("")
        print("  ", icons["about"]," (3)"+colorama.Fore.YELLOW +" AJUDA" + colorama.Style.RESET_ALL)
        print("")
        print("  ", icons["exit"],"(4)"+colorama.Fore.YELLOW +" SAIR" + colorama.Style.RESET_ALL)
        print("")
        print("")
        print("")
        print("| SELECIONE (DIGITE A OPÇÃO ABAIXO)")
        print(erro)
        escolha = input(">> ").upper()
        if escolha in ["SAIR", "EXIT", "QUIT", "Q", "4"]:
            verdade = False
            menu_sair()
        elif escolha in ["AJUDA", "HELP", "3"]:
            verdade = False
            menu_help()
        elif escolha in ["CARREGAR", "LOAD", "2"]:
            erro = colorama.Back.RED + "AINDA NÃO IMPLEMENTADO!" + colorama.Style.RESET_ALL
            #menu_load()
        elif escolha in ["NOVO JOGO", "NOVO", "1"]:
            verdade = False
            intro_scene()
        elif escolha in ["RESTART","RESET","R"]:
            verdade = False
            game_start()
        else:
            erro = colorama.Back.RED+"INSIRA UMA OPÇÃO VÁLIDA!"+colorama.Style.RESET_ALL

def menu_load():
    pass

def menu_sair():
    os.system("clear")
    quit()

def menu_help():
    print("\n" * 100)
    texto = text_reader("ajuda.txt")
    print("\n" * 100)
    verdade = True
    erro = ""
    while verdade:
        print(texto)
        print("")
        print("| DIGITE \'1\' PARA LER DENOVO\n| DIGITE \'Q\' PARA VOLTAR PARA O MENU")
        print(erro)
        escolha = input(">> ").upper()
        if escolha in ["1","LER"]:
            verdade = False
            menu_help()
        elif escolha in ["Q","MENU","SAIR"]:
            verdade = False
            main_menu()
        else:
            erro = colorama.Back.RED+"INSIRA UMA OPÇÃO VÁLIDA!"+colorama.Style.RESET_ALL

def intro_scene():
    verdade = True
    erro = ""
    while verdade:
        print("\n" * 100)
        print("| DESEJA VER A INTRODUÇÃO? (SIM ou NÃO)")
        print(erro)
        escolha = input(">> ").upper()
        if escolha in ["SIM","S"]:
            verdade = False
            texto = text_reader("intro.txt")
            create_char()
        if escolha in ["NÃO","NAO","N"]:
            verdade = False
            create_char()
        else:
            erro = colorama.Back.RED + "INSIRA UMA OPÇÃO VÁLIDA!" + colorama.Style.RESET_ALL

def create_char():
    pick_race()

def pick_race():
    verdade = True
    erro = ""
    while verdade:
        print("\n"*100)
        print(" RAÇA")
        print("\n" * 2)
        print(" ", icons["humano"],colorama.Fore.YELLOW +" HUMANO" + colorama.Style.RESET_ALL)
        print("      São medianos em todos atributos, porém começam com um equipamento melhor.")
        print("")
        print(" ", icons["elfo"],colorama.Fore.YELLOW +" ELFO" + colorama.Style.RESET_ALL)
        print("      Possuem DES e INT mais altos, porém CON e FOR mais baixos.")
        print("")
        print(" ", icons["fada"],colorama.Fore.YELLOW +" FADA" + colorama.Style.RESET_ALL)
        print("      Possuem atributos baixos, porém SOR é muito alto. Não precisam de poções.")
        print("")
        print(" ", icons["vampiro"],colorama.Fore.YELLOW +" VAMPIRO" + colorama.Style.RESET_ALL)
        print("      Começam com péssimo equipamento, porém todo ataque recupera parte da vida.")
        print("")
        print(" ", icons["zora"],colorama.Fore.YELLOW +" ZORA" + colorama.Style.RESET_ALL)
        print("      Começam com péssimo equipamento, porém seus ataques não gastam MP.")
        print("\n")
        print("| ESCOLHA SUA RAÇA:")
        print(erro)
        escolha = input(">> ").lower()
        if escolha in ["humano","vampiro","fada","elfo","zora"]:
            verdade = False
            jogador["Raça"] = escolha.capitalize()
            pick_class()
        else:
            erro = colorama.Back.RED + "INSIRA UMA OPÇÃO VÁLIDA!" + colorama.Style.RESET_ALL

def pick_class():
    verdade = True
    erro = ""
    while verdade:
        print("\n"*100)
        print(" CLASSE")
        print("\n" * 2)
        print(" ", icons["guerreiro"],colorama.Fore.YELLOW +" GUERREIRO" + colorama.Style.RESET_ALL)
        print("      Empunham espadas e armaduras pesadas. Utilizam pouca magia.")
        print("")
        print(" ", icons["ladino"],colorama.Fore.YELLOW +" LADINO" + colorama.Style.RESET_ALL)
        print("      Empunham arcos e armaduras médias. Utilizam alguma magia.")
        print("")
        print(" ", icons["mago"],colorama.Fore.YELLOW +" MAGO" + colorama.Style.RESET_ALL)
        print("      Empunham orbes e armaduras leves. Utilizam muita magia.")
        print("\n" * 7)
        print("| ESCOLHA SUA CLASSE:")
        print(erro)
        escolha = input(">> ").lower()
        if escolha in ["guerreiro","ladino","mago"]:
            verdade = False
            jogador["Classe"] = escolha.capitalize()
            change_name()
        else:
            erro = colorama.Back.RED + "INSIRA UMA OPÇÃO VÁLIDA!" + colorama.Style.RESET_ALL

def change_name():
    verdade = True
    erro = ""
    while verdade:
        print("\n"*100)
        print(" NOME")
        print("\n" * 18)
        print("| ESCOLHA SEU NOME:")
        print(erro)
        escolha = input(">> ").capitalize()
        if escolha.isalpha():
            verdade = False
            jogador["Nome"] = escolha
            roll_dice()
        else:
            erro = colorama.Back.RED + "INSIRA UMA OPÇÃO VÁLIDA!" + colorama.Style.RESET_ALL


def roll_dice():
    verdade = True
    erro = ""
    rolagem = 0
    while verdade:
        print("\n"*100)
        print("|",jogador["Nome"].upper(),"("+icons[jogador["Raça"].lower()],jogador["Raça"],icons[jogador["Classe"].lower()],jogador["Classe"]+")","("+icons["dinheiro"],str(jogador["Dinheiro"])+"$"+")","("+icons["Local"],jogador["Local"]+")")
        print("")
        for i in ["HP","MP"]:
            print("|", icons[i],jogador[i],i)
        print("")
        print("|","ATK:",jogador["ATK"],"DEF:",jogador["DEF"])
        print("|","HIT:",str(jogador["HIT"])+"%","EVA:",str(jogador["EVA"])+"%")
        print("")
        for i in ["CON","DES","FOR","INT","RES","SOR"]:
            print("|",i, icons[i], jogador[i])
        print("")
        print("| EQUIPAMENTO")
        print("")
        print(jogador["Arma"]["Icone"], jogador["Arma"]["Nome"])
        print(jogador["Armadura"]["Icone"],jogador["Armadura"]["Nome"])
        print(jogador["Accs"]["Icone"], jogador["Accs"]["Nome"])
        print("")
        print("| DIGITE O QUE DESEJA FAZER (ROLAR, CONTINUAR, RECOMEÇAR) (REROLLS: %i)" %(10-rolagem))
        print(erro)

        escolha = input(">> ").lower()
        if escolha in ["continuar","2"]:
            if rolagem < 1:
                erro = colorama.Back.RED + "VOCÊ TEM QUE ROLAR OS DADOS PELO MENOS UMA VEZ!" + colorama.Style.RESET_ALL
            else:
                erro = ""
                verdade = False
                primeiro_mapa()
        elif escolha in ["rolar","1",""]:
            erro = ""
            if rolagem > 9:
                erro = colorama.Back.RED + "DESCULPE, MAS JÁ ROLOU MUITAS VEZES!" + colorama.Style.RESET_ALL
            else:
                for n in range(7):
                    print("\n" * 100)
                    print("| Rolando", icons["dice"] * n)
                    time.sleep(0.3)
                for equipamento in jogador_equipamentos:
                    jogador[equipamento] = classes[jogador["Classe"].lower()][equipamento]
                for atributo in jogador_atributos:
                    jogador[atributo] = classes[jogador["Classe"].lower()][atributo] + (
                        racas[jogador["Raça"].lower()][atributo]) * 2 + random.randint(0, 2) + jogador["Accs"][atributo]
                jogador["HP"] = int(jogador["CON"]) * 20 + 50
                jogador["MP"] = int(jogador["INT"]) * 20
                jogador["ATK"] = jogador["Arma"]["ATK"] + jogador["Armadura"]["ATK"] + jogador[
                    classes[jogador["Classe"].lower()]["att"]]
                jogador["DEF"] = jogador["Arma"]["DEF"] + jogador["Armadura"]["DEF"] + jogador["RES"]
                jogador["HIT"] = int(
                    (jogador["Arma"]["HIT"] * 10 + jogador["Armadura"]["HIT"] * 10 + jogador["SOR"]) * 1.2 + jogador[
                        "DES"])
                jogador["EVA"] = int(
                    (jogador["Arma"]["EVA"] * 10 + jogador["Armadura"]["EVA"] * 10 + jogador["SOR"]) * 1.2 + jogador[
                        "DES"])
                jogador["Dinheiro"] = (jogador["SOR"] * 10) + 50
                jogador["Local"] = "Terrine"
                rolagem += 1
        elif escolha in ["recomeçar", "3"]:
            erro = ""
            verdade = False
            for i in jogador:
                jogador[i] = jogador_zerado[i]
            intro_scene()
        else:
            erro = colorama.Back.RED + "INSIRA UMA OPÇÃO VÁLIDA!" + colorama.Style.RESET_ALL

def primeiro_mapa():
    print("\n" * 100)
    print("Apartir daqui não está pronto, mas começa a aventura!")
    print("")
    for i in jogador:
        if i in ["Arma","Armadura","Accs"]:
            print(i + ":", jogador[i]["Nome"])
        else:
            print(i+":",jogador[i])