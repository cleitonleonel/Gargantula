# coding: utf-8

from data.icons_lib import *

item = {
    #ARMAS
    '000': {"Nome": "Faca de cozinha", "Peso": "1", "Icone": icons["sword"], "Tipo": "Arma", "ATK": 10,"DEF": 1,"HIT": 1,"EVA": 0},
    '001': {"Nome": "Bolinha de gude", "Peso": "0.5", "Icone": icons["orb"], "Tipo": "Arma", "ATK": 10,"DEF": 0,"HIT": 1,"EVA": 1},
    '002': {"Nome": "Estilingue de feijão", "Peso": "0.1", "Icone": icons["bow"], "Tipo": "Arma", "ATK": 10,"DEF": 0,"HIT": 2,"EVA": 0},
    #ARMADURAS
    '100': {"Nome": "Colete de paintball", "Peso": "1", "Icone": icons["armor"], "Tipo": "Armadura", "ATK": 0,"DEF": 10,"HIT": 0,"EVA": 0},
    '101': {"Nome": "Biquíni cavadão", "Peso": "1", "Icone": icons["bikini"], "Tipo": "Armadura", "ATK": 0,"DEF": 2,"HIT": 1,"EVA": 2},
    '102': {"Nome": "Camisola da vovó", "Peso": "1", "Icone": icons["camisola"], "Tipo": "Armadura", "ATK": 0,"DEF": 5,"HIT": 1,"EVA": 1},
    #ACESSORIOS
    '200': {"Nome": "Colar de coquinho", "Peso": "1", "Icone": icons["necklace"], "Tipo": "Acessório", "FOR": 1, "CON": 1, "DES": 0, "INT": -1, "RES": 0, "SOR": 2},
    #CONSUMIVEIS
    '300': {"Nome": "Poção de Vida", "Peso": "0.1", "Icone": icons["potion"], "Tipo": "Consumível", "Vida": "100", "Mana": "0"},
    #MISC
    '400': {"Nome": "Mapa de Rutapria", "Peso": "0.1", "Icone": icons["Local"], "Tipo": "Misc", "Info": "| Um mapa do continente. Use-o com \n| sabedoria durante sua jornada! "},
}

def infoitem(id):
    print(item[id]["Icone"],"",item[id]["Nome"],"("+item[id]["Tipo"]+")",icons["weight"],"",item[id]["Peso"],"kg")
    print("")
    if item[id]["Tipo"] == "Arma" or item[id]["Tipo"] == "Armadura" or item[id]["Tipo"] == "Acessório":
        print("| FOR:   +", item[id]["FOR"])
        print("| CON:   +", item[id]["CON"])
        print("| DES:   +", item[id]["DES"])
        print("| INT:   +", item[id]["INT"])
        print("| RES:   +", item[id]["RES"])
        print("| SOR:   +", item[id]["SOR"])
    if item[id]["Tipo"] == "Consumível":
        print("| HP:   +", item[id]["Vida"])
        print("| MP:   +", item[id]["Mana"])
    if item[id]["Tipo"] == "Misc":
        print("| INFORMAÇÕES:")
        print(item[id]["Info"])
    print("")
    return
