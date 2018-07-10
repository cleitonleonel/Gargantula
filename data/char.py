from data.icons_lib import *
from data.item_lib import *

jogador = {
            "Nome": "",
            "Raça": "",
            "Classe": "",
            "CON": 0,
            "DES": 0,
            "FOR": 0,
            "INT": 0,
            "RES": 0,
            "SOR": 0,
            "Dinheiro": 0,
            "Local": "???",
            "Armadura": {"Nome":"", "Icone":""},
            "Arma": {"Nome":"", "Icone":""},
            "Accs": {"Nome":"", "Icone":""},
            "HP": 0,
            "MP": 0,
            "ATK": 0,
            "DEF": 0,
            "EVA": 0,
            "HIT": 0
          }

jogador_zerado = {
            "Nome": "",
            "Raça": "",
            "Classe": "",
            "CON": 0,
            "DES": 0,
            "FOR": 0,
            "INT": 0,
            "RES": 0,
            "SOR": 0,
            "Dinheiro": 0,
            "Local": "???",
            "Armadura": {"Nome":"", "Icone":""},
            "Arma": {"Nome":"", "Icone":""},
            "Accs": {"Nome":"", "Icone":""},
            "HP": 0,
            "MP": 0,
            "ATK": 0,
            "DEF": 0,
            "EVA": 0,
            "HIT": 0
          }


jogador_atributos = {"CON":jogador["CON"],"DES":jogador["DES"],"FOR":jogador["FOR"],"INT":jogador["INT"],"RES":jogador["RES"],"SOR":jogador["SOR"]}
jogador_equipamentos = {"Armadura":jogador["Armadura"],"Accs":jogador["Accs"],"Arma":jogador["Arma"]}

classes = {
            "guerreiro":
            { # 5 pra cada, 30 no total, 15 no maximo
                "CON": 3,
                "DES": 1,
                "FOR": 4,
                "INT": 1,
                "RES": 5,
                "SOR": 1,
                "Armadura": item["100"],
                "Arma": item["000"],
                "Accs": item["200"],
                "icon": icons["guerreiro"],
                "att": "FOR"
            },
            "mago":
            { # 5 pra cada, 30 no total, 15 no maximo
                "CON": 2,
                "DES": 2,
                "FOR": 1,
                "INT": 5,
                "RES": 1,
                "SOR": 4,
                "Armadura": item["101"],
                "Arma": item["001"],
                "Accs": item["200"],
                "icon": icons["mago"],
                "att": "INT"
            },
            "ladino":
            { # 5 pra cada, 30 no total, 15 no maximo
                "CON": 1,
                "DES": 5,
                "FOR": 1,
                "INT": 1,
                "RES": 2,
                "SOR": 5,
                "Armadura": item["102"],
                "Arma": item["002"],
                "Accs": item["200"],
                "icon": icons["ladino"],
                "att": "DES"
            }}



racas = {
            "humano":
            { # 3 pra cada, 18 no total, 12 no maximo (2+2+2+2+2+2 = 12)
                "CON": 2,
                "DES": 2,
                "FOR": 2,
                "INT": 2,
                "RES": 2,
                "SOR": 2,
                "icon": icons["humano"]
            },
            "elfo":
            { # 3 pra cada, 18 no total, 12 no maximo
                "CON": 1,
                "DES": 3,
                "FOR": 1,
                "INT": 3,
                "RES": 2,
                "SOR": 2,
                "icon": icons["elfo"]
            },
            "fada":
            { # 3 pra cada, 18 no total, 12 no maximo (fada é exceção)
                "CON": 1,
                "DES": 1,
                "FOR": 1,
                "INT": 1,
                "RES": 1,
                "SOR": 6,
                "icon": icons["fada"]
            },
            "vampiro":
            { # 3 pra cada, 18 no total, 12 no maximo
                "CON": 3,
                "DES": 2,
                "FOR": 2,
                "INT": 3,
                "RES": 1,
                "SOR": 1,
                "icon": icons["vampiro"]
            },
            "zora":
            { # 3 pra cada, 18 no total, 12 no maximo (2+2+2+2+2+2 = 12)
                "CON": 1,
                "DES": 2,
                "FOR": 3,
                "INT": 1,
                "RES": 3,
                "SOR": 2,
                "icon": icons["zora"]
            }}